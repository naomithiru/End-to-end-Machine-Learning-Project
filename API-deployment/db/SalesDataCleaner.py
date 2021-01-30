import pandas as pd
import re


class SalesDataCleaner:
    """ Utility class that cleans real estate sale offers data from a CSV file into a pandas DataFrame for further work on it"""

    def __init__(self, url):
        self.sales_data = url

    def clean(self):
        self.import_and_format()  # now it just formats, it doesn't import
        self.delete_land_plot_surface_column()
        # self.delete_sale_column()
        self.clean_property_subtype_column()
        self.clean_price_column()
        self.clean_area_column()
        self.clean_area_land_surface_columns()
        self.clean_building_state_column()
        self.sales_data.rename(columns={"kitchen_has": "equipped_kitchen_has"})
        # self.clean_facades_number_column()
        self.clean_house_is()
        self.remove_duplicate_records()
        self.remove_na_records()
        return self.sales_data

    def import_and_format(self):
        columns_types = {
            "postcode": int,
            "house_is": bool,
            "property_subtype": str,
            "rooms_number": int,
            "garden_area": int,
            "land_surface": int,
            "building_state": str,
        }

    @staticmethod
    def price_converter(x):
        # removing non-digit heading and trailiong characters
        x = re.sub(r"\D+$", "", re.sub(r"^\D+", "", x))
        # removing trailing non-digit and dot characters until the last '€' character
        x = re.sub(r"€(.|\D)*$", "", x)
        x = x.replace(",", "")
        # we expect only digits or a dot after replacing commas with an empty string, so we should be able to convert if
        # if not possible we catch the exceptionproperty_subtype
        try:
            return int(x)
        except ValueError:
            return None

    @staticmethod
    # expected boolean are transformed into bool even if originally were strings or numbers
    def bool_or_keep(x):
        output = None
        try:
            if isinstance(x, str):
                if (x == "1") or (x.upper() == "TRUE"):
                    output = True
                elif (x == "0") or (x.upper() == "FALSE"):
                    output = False
            elif x.isnumeric():
                if x == 1:
                    output = True
                elif x == 0:
                    output = False
            elif isinstance(x, bool):
                output = x
            return output
        except ValueError:
            return None

    @staticmethod
    # expected float values are converted into float even if originally were wrongly coded as boolean or number
    def float_or_zero(x):
        try:
            float(x)
            return float(x)
        except ValueError:
            # keeping information of terrace if lost
            if x == True or x == 1 or x == "True" or x == "TRUE":
                return 0
            else:
                return None

    @staticmethod
    # expected float values are returned as None
    def float_or_text_to_nan(x):
        try:
            return float(x)
        # generic value error instead of isistance(x,str) to cover more cases instead of strings only.
        except ValueError:
            return None

    @staticmethod
    # a single integer number is extracted from area to remove the m2 measurement units.
    # this simple method was adopted since no commas were found in area field.
    def area_remove_m2(x):
        try:
            return int(x)
        except ValueError:
            numbers = [int(s) for s in x.split() if s.isdigit()]
            if len(numbers) == 1:
                return float(numbers[0])
            elif len(numbers) > 1:
                return False
            else:
                return None

    # def display(self):
    #     print(self.sales_data)

    # def delete_hyperlink_column(self):
    #     self.sales_data.drop('hyperlink', axis='columns', inplace=True)

    def delete_land_plot_surface_column(self):
        self.sales_data.drop("land_plot_surface", axis="columns", inplace=True)

    def delete_sale_column(self):
        self.sales_data.drop('sale', axis='columns', inplace=True)

    @staticmethod
    def to_region(postcode):
        if pd.isna(postcode):
            region = None
        else:
            postcode = int(postcode)
            if 1000 <= postcode and postcode <= 1299:
                region = "B"
            elif (1300 <= postcode and postcode <= 1499) or (
                4000 <= postcode and postcode <= 7999
            ):
                region = "W"
            else:
                region = "F"
        return region

    def clean_house_is(self):
        self.sales_data["house_is"] = [
            True if cell == "HOUSE" else False for cell in self.sales_data["house_is"]]

    def clean_property_subtype_column(self):
        to_be_deleted_subtypes = [
            "Wohnung",
            "Triplexwohnung",
            "Sonstige",
            "Loft / �tico",
            "Loft / Dachgeschoss",
            "Loft / Attic",
            "Gewerbe",
            "Etagenwohnung",
            "Erdgeschoss",
            "Attico",
            "Appartamento duplex",
            "Apartamento",
            "Altbauwohnung",
            "HOUSE_GROUP",
            "APARTMENT_GROUP",
        ]

        to_be_deleted_filter = self.sales_data["property_subtype"].apply(
            lambda x: x in to_be_deleted_subtypes
        )
        self.sales_data.loc[to_be_deleted_filter, "property_subtype"] = None

        to_be_deleted_filter = self.sales_data["property_subtype"].apply(
            lambda x: type(x) in [int, float]
        )
        self.sales_data.loc[to_be_deleted_filter, "property_subtype"] = None

        to_be_deleted_filter = self.sales_data["property_subtype"].apply(
            lambda x: "sqft" in str(x)
        )
        self.sales_data.loc[to_be_deleted_filter, "property_subtype"] = None

    def clean_price_column(self):
        to_be_deleted_filter = self.sales_data["price"].apply(
            lambda x: x == 0)
        self.sales_data.loc[to_be_deleted_filter, "price"] = None

    @staticmethod
    def categorize_state(value):
        to_renovate = [
            "TO_RENOVATE",
            "TO_BE_DONE_UP",
            "old",
            "To renovate",
            "To be done up",
        ]
        good = ["GOOD", "Good"]
        as_new = ["AS_NEW", "As new", "New"]
        renovated = ["JUST_RENOVATED", "Just renovated"]
        restore = ["To restore", "TO_RESTORE"]
        category = None  # default category (corresponds to values = '0')
        if value in to_renovate:
            category = "TO_RENOVATE"
        elif value in good:
            category = "GOOD"
        elif value in renovated:
            category = "JUST_RENOVATED"
        elif value in restore:
            category = "TO_RESTORE"
        elif value in as_new:
            category = "AS_NEW"
        return category

    def clean_building_state_column(self):
        self.sales_data["building_state_agg"] = self.sales_data["building_state"].apply(
            SalesDataCleaner.categorize_state
        )
        self.sales_data.drop("building_state", axis="columns", inplace=True)

    def clean_area_column(self):
        to_be_deleted_filter = self.sales_data["area"].apply(
            lambda x: x == 0)
        self.sales_data.loc[to_be_deleted_filter, "area"] = None

    def clean_area_land_surface_columns(self):
        self.sales_data = self.sales_data.apply(
            SalesDataCleaner.copy_from_land_surface, axis="columns"
        )

    def clean_facades_number_column(self):
        to_be_deleted_filter = self.sales_data["facades_number"].apply(
            lambda x: x == 0 or x > 4
        )
        self.sales_data.loc[to_be_deleted_filter, "facades_number"] = None

    @staticmethod
    def copy_from_land_surface(row):
        if row.area == 0 and row.land_surface > 0:
            row.area = row.land_surface
        return row

    def remove_duplicate_records(self):
        self.sales_data.drop_duplicates(
            subset=["postcode", "house_is", "price", "area"], inplace=True
        )

    def remove_na_records(self):
        # print("it was self.sales_data.dropna(axis=0, inplace=True)")
        self.sales_data.dropna(axis=0, inplace=True)


if __name__ == "__main__":
    sdc = SalesDataCleaner("mydatabase.db")
    cleaned_data = sdc.clean()
    # print(cleaned_data)
