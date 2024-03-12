from src.mdrHandler import mdrClient
from src.DBConnector import DBConnector


## connect to your local database
con = DBConnector()
connection =con.DatabaseConnector(server='UCCH-OUMUAMUA', database='MEDBASE_STAGE')


## extract Mapping information from MDR RestApi
mdr = mdrClient()
Meta_fetch = mdr.mapping_data(dictionary='OMOP')

## insert metadata into your local database
Meta_fetch.to_sql(
    name="omop", con=connection, schema="metadata", if_exists="replace"
)

# close database connection
connection.dispose()