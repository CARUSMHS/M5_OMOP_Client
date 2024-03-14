# MDR_Client
A python client to extract metadata from the RestApi of the further developed SamplyMDR

## Requirements
- Access to IAM Metadata Repository [https://mdrdev2.iam-extern.de/m5.gui/index.xhtml]

- Supported Databases
    - Microsoft SQL Server

- Authenthification
    - Trusted DB Connection must be accepted from the local DB


## Installation 
Execute Run.py to extract all neccessary mapping information in tabular manner from MDR RestApi. Before doing that you declare some variables in main.py.


- Local Database variables
server : Server name of your local staging database
database : name of your staging database
```
connection =con.DatabaseConnector(server='UCCH-OUMUAMUA', database='MEDBASE_STAGE')
```
- MDR variables
dictioanary : should be set to OMOP if not other specified
table : (optional) if you only want to extract table specific metadata in your defined dictionary
```
Meta_fetch = mdr.mapping_data(dictionary='OMOP')
```
