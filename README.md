# M5-OMOP-Client
A python client to extract metadata from the M5-REST API, furthermore it provides the possibility to automatically import the OMOP Metadata into a relational database (supported systems: **PostgreSQL, ORACLE, SQL SERVER**)

## Requirements
- Access to M5 REST API [https://mdrdev2.iam-extern.de/m5.rest/api/]

- Supported Databases
    - Microsoft SQL Server (Windows Athentification + SQL Server Authentification)
    - ProstgreSQL
    - Oracle (Attention: python-oracledb driver only accepts password verifiers 11G and later)


## Application

1. Do the Database Configuration in main.py (more information about database configuration [[(src/DBConnector.py)]]). 

```python
con = DBConnector(db_system="Oracle")
connection =con.DatabaseConnector(user=user,password=password,server=server, port=port,SID=SID)
```

2. Run the OMOP_Client class in main.py and save output in *M5_fetch*

```python
m5 = OMOP_Client()
M5_fetch = m5.mapping_data(dictionary='OMOP')
```

3. Import *M5_fetch* into your local database, using your database configuration defined in step 1, and close connection

```python
M5_fetch.to_sql(
    name="Test", con=connection, schema="metadata", if_exists="replace"
)
connection.dispose()
```

