import numpy as np
import pandas as pd
import re
from itertools import chain
from IPython.display import Markdown, display
from more_itertools import unique_everseen

from src.davy_data_cleaning import *
from src.manasa_data_cleaning import *
from src.naomi_data_cleaning import *
from src.sara_data_cleaning import *


if __name__ == "__main__":
    #Reading the merged raw dataset from
    data = pd.read_csv('https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv',sep=',',dtype='unicode')

    data['hyperlink'] = clean_hyperlink_column(data)
    data["postcode"] = postcodes_fun(data)
    data["house_is"] = house_is(data)
    data["property_subtype"] = process_property_types(data)
    data["price"] = clean_price_column(data)
    data["sale"] = clean_sale_column(data)
    data["rooms_number"] = process_num_rooms_col(data)
    data["area"] = process_area_col(data)
    data["kitchen_has"] = bool_to_bin("kitchen_has", int, data)
    data["furnished"] = bool_to_bin("furnished", int, data)
    data["open_fire"] = process_open_fire_col(data)
    data["terrace"] = process_terrace(data)
    data["terrace_area"] = process_terrace_area(data)
    data["garden"] = clean_garden_column(data)
    data["garden_area"] = clean_garden_area(data)
    data["land_surface"] = process_land_surf_col(data)
    data["land_plot_surface"] = process_land_plot_col(data)
    data["facades_number"] = facades_num(data)
    data["swimming_pool_has"] = clean_swimming_pool(data)
    data["building_state"] = process_building_state(data)

    #Drop duplicates
    data_dupes = data
    data_dupes = data_dupes.drop('source', axis=1)
    data_dupes = data_dupes.drop('hyperlink', axis=1)
    data_dupes = data_dupes.drop_duplicates()

    #Save the two final files
    data_dupes.to_csv('Datasets/final_with_dupes.csv')
    with open('Datasets/final_with_dupes.csv','r') as f, open('Datasets/final_no_dupes.csv','w') as out_file:
        out_file.writelines(unique_everseen(f))


    