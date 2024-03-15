# MDR_Client
A python client to extract metadata from the RestApi of the further developed SamplyMDR

## Requirements
- Access to IAM Metadata Repository [https://mdrdev2.iam-extern.de/m5.gui/index.xhtml]

- Supported Databases
    - Microsoft SQL Server (Windows Athentification + SQL Server Authentification)
    - ProstgreSQL


## Installation 
Execute Main.py to extract all neccessary mapping information in tabular manner from M5 RestApi. Before doing that you have to declare department specific variables in main.py.


- Local Database variables
    The Database Destination for the M5 Metadata Extraction
    - server : Server name of your local staging database
    - database : name of your staging database

```
# MicrsoftSQL configuration
    # Windows Athentification
con = DBConnector(db_system="MicrosoftSQL")
connection =con.DatabaseConnector(server='your server', database='your database', trusted_con=True)

    # SQL Server Authentification
con = DBConnector(db_system="MicrosoftSQL")
connection =con.DatabaseConnector(server='your server', database='your database', user='your user', password='your password')

# PostgreSQl configuration
con = DBConnector(db_system="PostgreSQL")
connection =con.DatabaseConnector(server='your server', database='your database', user='your user', password='your password')
)

```
- MDR variables
    -   dictioanary : should be set to OMOP if not other specified
    -   table : (optional) if you only want to extract table specific metadata in your defined dictionary
```
mdr = mdrClient() 
Meta_fetch = mdr.mapping_data(dictionary='OMOP')
```
