import sqlalchemy as sq


class DBConnector:
    """
    Database Connector
    """

    def __init__(self):
        self.database = "MicrosoftSQL"

    def DatabaseConnector(self, server, database):

        # Microsoft SQL Server Configuration
        if self.database == "MicrosoftSQL":

            conn_string_msql = (
                r"Driver={ODBC Driver 17 for SQL Server};"
                f"Server= {server};"
                f"Database={database};"
                r"Trusted_Connection=yes"
                )
            connection_url = sq.URL.create("mssql+pyodbc", query={"odbc_connect": conn_string_msql})
            engine = sq.create_engine(connection_url) 
            return (engine)
        
        else:
            print("This Database is not supoorted.")




