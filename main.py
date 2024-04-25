from src.M5Handler import OMOP_Client
from src.DBConnector import DBConnector


## connect to your local database and choose your database system (supported DBs: Oracle, PostgreSQL, MicrosoftSQL)--> Case sensitive
con = DBConnector(db_system="Oracle")
connection =con.DatabaseConnector(user=user,password=password,server=server, port=port,SID=SID)

## extract Mapping information from MDR RestApi
m5 = OMOP_Client()
M5_fetch = m5.mapping_data(dictionary='OMOP')

## insert metadata into your local database, therefore metadata schema is used (please use = CREATE SCHEMA metadata;)
M5_fetch.to_sql(
    name="Test", con=connection, schema="metadata", if_exists="replace"
)

# close database connection
connection.dispose()

    