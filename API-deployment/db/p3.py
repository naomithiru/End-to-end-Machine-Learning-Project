# an example use of the SalesDataCleaner class to write to another CSV file the cleaned DataFrame obtained from an original CSV file
from db.SalesDataCleaner import SalesDataCleaner
import sqlite3
import pandas as pd


def p3():
    conn = sqlite3.connect("db/mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""select * from scrapped""")
    df = pd.DataFrame(
        cursor.fetchall(),
        columns=[
            "index",
            "house_is",
            "property_subtype",
            "price",
            "postcode",
            "area",
            "rooms_number",
            "kitchen_has",
            "garden",
            "garden_area",
            "terrace",
            "terrace_area",
            "furnished",
            "swimming_pool_has",
            "land_surface",
            "land_plot_surface",
            "building_state",
            "open_fire",
            "longitude",
            "latitude",
            "datum"
        ]
    )
    conn.commit()
    df["index"] = pd.to_numeric(df["index"], downcast="integer")
    df["house_is"] = pd.to_numeric(
        df["house_is"], downcast="integer").astype('bool')
    df["price"] = pd.to_numeric(df["price"], downcast="integer")
    df["postcode"] = pd.to_numeric(df["postcode"], downcast="integer")
    df["area"] = pd.to_numeric(df["area"], downcast="integer")
    df["rooms_number"] = pd.to_numeric(df["rooms_number"], downcast="integer")
    df["kitchen_has"] = pd.to_numeric(
        df["kitchen_has"], downcast="integer").astype('bool')
    df["garden"] = pd.to_numeric(
        df["garden"], downcast="integer").astype('bool')
    df["garden_area"] = pd.to_numeric(df["garden_area"], downcast="integer")
    df["terrace"] = pd.to_numeric(
        df["terrace"], downcast="integer").astype('bool')
    df["terrace_area"] = pd.to_numeric(df["terrace_area"], downcast="integer")
    df["furnished"] = pd.to_numeric(
        df["furnished"], downcast="integer").astype('bool')
    df["swimming_pool_has"] = pd.to_numeric(
        df["swimming_pool_has"], downcast="integer").astype('bool')
    df["land_surface"] = pd.to_numeric(df["land_surface"], downcast="integer")
    df["land_plot_surface"] = pd.to_numeric(
        df["land_plot_surface"], downcast="integer")
    df["open_fire"] = pd.to_numeric(
        df["open_fire"], downcast="integer").astype('bool')
    df["longitude"] = pd.to_numeric(df["longitude"], downcast="float")
    df["latitude"] = pd.to_numeric(df["latitude"], downcast="float")
    df["datum"] = pd.to_datetime(df["datum"])
    df = df.drop_duplicates()
    df.to_sql(name='scrapped', con=conn,
              if_exists='replace', index=False)
    conn.commit()
    df.to_sql(name='scrapped', con=conn,
              if_exists='replace', index=False)
    conn.commit()
    conn.close()
    sdc = SalesDataCleaner(df)
    cleaned_data = sdc.clean()
    conn = sqlite3.connect("db/mydatabase.db")
    cleaned_data["price"] = cleaned_data["price"].astype('int')
    cleaned_data["area"] = cleaned_data["area"].astype('int')
    cleaned_data.to_sql(name="cleaned", con=conn,
                        index=False,  if_exists="replace")
    conn.commit()
    conn.close()
