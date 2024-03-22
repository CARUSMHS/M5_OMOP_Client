from src.mdrHandler import mdrClient
from src.DBConnector import DBConnector
from src.m5_vis import M5_vis


## connect to your local database
con = DBConnector(db_system="Oracle")
connection =con.DatabaseConnector(server="UCCH-OUMUAMUA",database="MEDBASE_STAGE",trusted_con=True)

## extract Mapping information from MDR RestApi
m5 = mdrClient()
M5_fetch = m5.mapping_data(dictionary='OMOP')

## insert metadata into your local database, therefore metadata schema is used (please use = CREATE SCHEMA metadata;)
M5_fetch.to_sql(
    name="Test", con=connection, schema="metadata", if_exists="replace"
)

# close database connection
connection.dispose()



## visulisation
vis = M5_vis(M5_fetch)

vis_dat = vis.translate_column('element') ## be careful, this can took a long time, maybe it is better to run it over night.


bar_chart = vis.bar_chart()

