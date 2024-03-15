from src.mdrHandler import mdrClient
from src.DBConnector import DBConnector


## connect to your local database
con = DBConnector(db_system="MicrosoftSQL")
connection =con.DatabaseConnector(server="UCCH-OUMUAMUA",database="MEDBASE_STAGE",trusted_con=True)


## extract Mapping information from MDR RestApi
mdr = mdrClient()
Meta_fetch = mdr.mapping_data(dictionary='OMOP')

## insert metadata into your local database, therefore metadata schema is used (please use = CREATE SCHEMA metadata;)
Meta_fetch.to_sql(
    name="Test", con=connection, schema="metadata", if_exists="replace"
)

# close database connection
connection.dispose()