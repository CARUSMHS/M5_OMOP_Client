import sqlalchemy as sq
import oracledb


class DBConnector:
    """
    Database Connector
    """

    def __init__(self, db_system):
        self.db_system = db_system

    def DatabaseConnector(self, server, database, user: None, password= None, trusted_con= None, port= None, SID= None):

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
        
        elif self.db_system == "Oracle": # TODO: funktioniert noch nicht, DBAPI Fehler

            url_object = "oracle+oracledb://" + user +  "/" + password  + "@" + server + ":" + port + '/' + SID

            engine = sq.create_engine(url_object)

            print("Oracle Database Engine is successfully created.")
            return (engine)

        
        else:
            print("This Database is not supoorted.")





