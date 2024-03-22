import json
import pandas as pd
import requests
import numpy as np



## class
class mdrClient:
    """
    Data Extraction Client for M5 REST API
    """

    def __init__(self):
        self.url = "https://mdrdev2.iam-extern.de/m5.rest/api"

    ## extracting mapping information from mdr rest api
    def mapping_data(self, dictionary, table=np.NaN):
        """
        OMOP Metadata Extractor -- this function read all the element concept information depending on selected dict. Furthermore it enrich concepts information
        with slots (in this case the Concept Class Slot) if possible. It always chooses the last dict version dependless if it is released or in a draft
        """
        print("Fetching Metadata from IAM M5")
        # read highest dict version
        dict_endpoint = self.url + f"/{dictionary}"
        request = requests.get(dict_endpoint).json()
        dict_version = request.get("dataDictionaryVersions")
        version_list = list(map(lambda x: x["name"], dict_version))
        version = max(version_list)

        if table is not np.NaN:
            api_endpoint = self.url + f"/{dictionary}/{version}/{table}"

            json_dict = requests.get(api_endpoint).json()
        else:
            api_endpoint = self.url + f"/{dictionary}/{version}"

            # Fetching all relevant content from REST API
            api_json = requests.get(api_endpoint).json()

            # Fetching all tables from REST api
            get_tables = api_json.get("tables")
            tables = list(map(lambda x: x["name"], get_tables))

            ## loop through RESt api tables
            json_dict = []
            for table in tables:
                url = api_endpoint + "/" + str(table)
                response = requests.get(url).json()
                json_dict.append(response)

        # read element information from all REST api tables
        flat_tmp = pd.json_normalize(json_dict,record_path=['elements'], meta=['name'], record_prefix='_').reset_index()

        # Flatting all element information from REST api
        # explode dict in df and expand values to columns and keys to row
        df1 = flat_tmp.explode("_slots")["_slots"].apply(pd.Series).reset_index(names="id")
        df1_1 = df1.loc[df1["slotName"] == "[Concept Class]"]
        df2 = (
            flat_tmp.explode("_concepts")["_concepts"]
            .apply(pd.Series)
            .reset_index(names="id")
            .drop(["verified"], axis=1)
        )


        # merge exploded concepts and slots with flat df
        flat = flat_tmp.drop(columns=['_slots','_concepts','_labels']) # erheblicher performance loss wenn dict im df bleiben

        dft = pd.merge(flat, df2, left_index=True, right_on="id", how="left")
        df = pd.merge(
            dft,
            df1_1,
            left_on=["index", "conceptName"],
            right_on=["id", "slotKey"],
            how="left",
        )

        # clean flattened df
        drops = [
            0,
            "verified",
            "conceptScore",
            "definitions.en"
        ]
        drop_pref = ['_value', 'id']

        df = df.loc[:, ~df.columns.to_series().astype(str).str.startswith(tuple(drop_pref))]

        for col in df.columns:
            if col in drops:
                del df[col]

        # rename columns to make them compatible with existing etl pipeline
        df = df.rename(
            columns={
                "name": "table",
                "_name": "element",
                "_dataType": "dataType",
                "_definitions.DE": "definitions.DE",
                "__links.self.href": "links.self.href",
                "_definitions.en": "definitions.en",
                "slotValue": "source_concept_class",
                "conceptName": "source_code",
                "conceptId": "concept_id",
                "index": "element_id",
            }
        )

        print("Metadata is succesfully fecthed from M5 RestApi")

        return df





