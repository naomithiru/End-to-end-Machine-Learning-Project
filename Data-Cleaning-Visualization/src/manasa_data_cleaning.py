import numpy as np
import pandas as pd

def process_open_fire_col(data_new):
    dt = data_new['open_fire']
    dt.convert_dtypes()
    dt = dt.str.lower()
    dt = dt.map({'false': 0, 'true': 1, 'nan': 2, '0': 2})
    dt.fillna(2, inplace=True)
    dt = dt.astype(int)
    return dt


def process_area_col(data_new):
    data_area = data_new['area']
    data_area = pd.to_numeric(data_area, errors='coerce')
    data_area.fillna(np.nan, inplace=True)
    return data_area


def process_land_surf_col(data_new):
    data_land_surf = data_new['land_surface']
    data_land_surf = pd.to_numeric(data_land_surf, errors='coerce')
    data_land_surf.fillna(np.nan, inplace=True)
    return data_land_surf


def process_land_plot_col(data_new):
    data_land_plot = data_new['land_plot_surface']
    data_land_plot = pd.to_numeric(data_land_plot, errors='coerce')
    data_land_plot.fillna(np.nan, inplace=True)
    return data_land_plot

def process_num_rooms_col(data_new):
    data_rmo = data_new['rooms_number']
    data_rmo = pd.to_numeric(data_rmo, errors='coerce')
    data_rmo.fillna(np.nan, inplace=True)
    data_rmo=data_rmo.astype('Int64')
    return data_rmo

# data_new['open_fire']=process_open_fire_col()
# data_new['area']=process_area_col()
# data_new['land_surface']=process_land_surf_col()
# data_new['land_plot_surface']=process_land_plot_col()
# data_new['rooms_number']=process_num_rooms_col()