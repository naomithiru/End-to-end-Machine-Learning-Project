import numpy as np
import pandas as pd

def postcodes_fun(df):
    "This function extracts postcodes from locality and adds them into null postcodes"

    # Extract postcodes from locality and add them to postcode column
    df["loc_code"] = df["locality"].str.extract(r"(\b[0-9]{4}\b)")
    df.loc[df.postcode.isnull(), "postcode"] = df.loc_code

    # Fill null vales with '-999'
    df["postcode"].fillna("-999", inplace=True)

    # Delete dummy column
    del df["loc_code"]

    # Return column
    return df["postcode"]


def bool_to_bin(x, final_type, df):
    """This function converts a True/False column into a 0/1"""

    df[x] = df[x].astype(str)
    df[x] = df[x].map({"False": 0, "True": 1, "nan": -999})
    df[x].fillna(-999, inplace=True)
    df[x] = df[x].astype(final_type)
    return df[x]


def facades_num(df):
    """This function cleans facades_number by covnerting values into integers
    and assign '0', 'nan' and 'none' to -999 (=treat as null)"""

    df["facades_number"] = df["facades_number"].apply(str)
    df.facades_number.replace("(\.0)", "", regex=True, inplace=True)
    df["facades_number"] = df.facades_number.replace(
        ["nan", "None", "0"], -999
    )  # maybe treat 0 as -999 too?
    df["facades_number"] = df["facades_number"].astype(int)
    return df["facades_number"]