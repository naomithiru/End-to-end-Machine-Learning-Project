# Preprocessing with json schema
# Import libraries for JSON input management and validation
from jsonschema.validators import Draft7Validator
from preprocessing.json_schema_file import json_schema
from preprocessing.gps import longitude_latitude
import pandas as pd
import sqlite3

json_input_2 = {  # Json Example
    "data": {
        "area": 5,
        "property-type": "APARTMENT",
        "rooms-number": 2,
        "zip-code": 1050,  # only 4 integers, >1000 & <9999
        "land-area": 56,  # Optional
        "garden": True,  # Optional
        # "garden-area": 34,  # Optional
        # "equipped-kitchen": False,  # Optional
        # "full-address": "djfg",  # Optional
        "swimmingpool": True,  # Optional
        "furnished": False,  # Optional
        "open-fire": True,  # Optional
        "terrace": False,  # Optional
        "terrace-area": 98,  # Optional
        "facades-number": 16,  # >1 & <10 #Optional
        # ["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        "property-subtype": "VILLA",
        "building-state": "NEW",
    }
}


def preprocess(json_input):
    """Check whether there are errors related to JSON input format"""

    # 1. Set validator variable to validate the input according to the draft version 7 JSON schema
    validator = Draft7Validator(schema=json_schema)

    # 2. Show input errors in a readable, user-friendly way
    readable_input_errors = []
    global error
    for error in validator.iter_errors(instance=json_input):
        if len(error.path) == 0:
            readable_input_errors.append(f"In 'properties': {error.message}. ")
        else:
            readable_input_errors.append(
                f"In '{str(error.path[-1])}': {error.message}. "
            )

    # 3. Input validation. If no errors are found, preprocess the input data.
    global message
    message = ""

    if readable_input_errors:
        error = True
        message = readable_input_errors

    else:
        error = False
        message = "SUCCESS: Your data is valid."

        """Once data is valid, start preprocessing"""
        # 1. Handle with null (None) values: replace by default ones

        jid = json_input["data"]

        boolean_variables = [
            "garden",
            "equipped-kitchen",
            "swimmingpool",
            "furnished",
            "open-fire",
            "terrace",
        ]
        integer_variables = [
            "terrace-area",
            "garden-area",
            "facades-number",
            "land-area",
        ]

        # Numeric variables
        for num1 in integer_variables:
            try:
                if jid[num1] < 1:
                    jid[num1] = 0
                elif num1 == "facades-number":
                    if jid[num1] > 4:
                        jid[num1] = 4
            except:
                jid[num1] = 1

        # Boolean variables

        for bool1 in boolean_variables:
            try:
                if jid[bool1] in [True]:
                    jid[bool1] = 1
                else:
                    jid[bool1] = 0
            except:
                jid[bool1] = 0

        # Property-type
        try:
            jid_pt = jid["property-subtype"]
        except:
            jid_pt = jid["property-subtype"] = 0
        conn = sqlite3.connect("db/mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""select * from property_subtype""")
        df = pd.DataFrame(cursor.fetchall())
        conn.commit()
        conn.close()
        for col1 in df[0]:
            # for col1 in subtype:
            try:
                if jid_pt == col1:
                    jid["col1_" + col1] = 1
                else:
                    jid["col1_" + col1] = 0
            except:
                jid["col1_" + col1] = 0

        # Building-state

        try:
            jid_bs = jid["building-state"]
        except:
            jid_bs = jid["building-state"] = 0
        conn = sqlite3.connect("db/mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""select * from building_state_agg""")
        df = pd.DataFrame(cursor.fetchall())
        conn.commit()
        conn.close()
        # if int(ids[i]) not in [int(x) for x in df[0]]:
        for col2 in df[0]:
            # for col2 in ["AS_NEW", "GOOD", "JUST_RENOVATED", "TO_RENOVATE", "TO_RESTORE"]:
            # print("col2 in df[0]", col2)
            try:
                if jid_bs == col2:
                    jid["col2_" + col2] = 1
                else:
                    jid["col2_" + col2] = 0
            except:
                jid["col2_" + col2] = 0

        # Full-address
        try:  # 186,Kloosterstraat,Dilbeek,1702 = format
            if jid["full-address"] != "":
                longitude, latitude = longitude_latitude(jid["full-address"])
                jid["latitude"] = latitude
                jid["longitude"] = longitude
            else:
                jid["latitude"] = 0
                jid["longitude"] = 0
        except:
            jid["latitude"] = 0
            jid["longitude"] = 0
            jid["full-address"] = ""
        # print("jid['latitude'], jid['longitude']",
            #   jid["latitude"], jid["longitude"])
        jid.pop("property-subtype")
        jid.pop("building-state")
        jid.pop("facades-number")
        # jid.pop("property-type")
        jid.pop("full-address")
    # print("###################################### JSON",
    #       len(json_input["data"].keys()))
    return error, message, json_input


if __name__ == "__main__":
    error, message, json_input_cleaned = preprocess(json_input_2)
    print({"error": error, "message": message}, json_input_cleaned)
