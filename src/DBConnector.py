import sqlalchemy as sq


class DBConnector:
    """
    Database Connector
    """

    def __init__(self, db_system):
        self.db_system = db_system

    def DatabaseConnector(self, server, database, user=False, password=False, trusted_con=False):

        # Microsoft SQL Server Configuration
        if self.db_system == "MicrosoftSQL":

            if trusted_con==True:

                url_object = "mssql+pyodbc://" + server + "/" + database + "?driver=ODBC+Driver+17+for+SQL+Server"

            else: 

                url_object = "mssql+pyodbc://" + user + ":" + password + "@" + server + "/" + database + "?driver=ODBC+Driver+17+for+SQL+Server"

            engine = sq.create_engine(url_object)

            print("Micrsoft SQL Database Engine is successfully created.")
            return (engine)
        
    # PostgreSQL Configuration
        elif self.db_system == "PostgreSQL":
            
            url_object = "postgresql+psycopg2://" + user + ":" + password + "@" + server + "/" + database 
            
            engine = sq.create_engine(url_object) 

            print("PostgreSQL Database Engine is successfully created.")
            return (engine)
        
        else:
            print("This Database is not supoorted.")





