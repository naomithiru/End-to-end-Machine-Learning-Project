import numpy as np
import pandas as pd

def process_terrace(df_selected):
    df = df_selected['terrace']
    df = df.astype(str)
    df = df.replace(['True', 'TRUE'], '1')
    df = df.replace(['False', '2.0', '3.0', '4.0'], '0')
    df = df.replace('nan', '-999')
    df = df*1
    df = df.astype(int)
    return df

def process_terrace_area(df_selected):
    df = df_selected['terrace_area']
    df = df.replace(['None', 'TRUE', 'Yes', 'South', 'North West', 'South East',
       'South West', 'North East', 'East', 'West'], '0') 
    df = df.replace(['0'], '-999')
    df = df.replace(np.NaN, '-999')
    df = df.astype(int)
    return df

def process_building_state(df_selected):
    df = df_selected['building_state']
    df.convert_dtypes()
    df = df.replace(['None', '0', 'not_specified', 'not_specified'],'-999')
    df = df.fillna('-999')
    df = df.str.lower()
    df = df.str.replace(" ", "_")
    df = df.replace(['to_be_done_up', 'to_restore', 'to be done up', 'to restore', 'to renovate'],'to_renovate')
    return df

def house_is(df_selected):
    df = df_selected['house_is']
    df = df*1
    return df

#function to clean property_subtypes column
def process_property_types(df):

    values = [ '2008','1994', '2015', '2007', '2009', '2014', '1992', '1997','133,000 sqft', '1983', '1971', '4', '2019', '1989','1995', '1900', '1990', '1993', '2020', '2016','2004', '1991', '2012', '1965', '1979','1982', '1963', '1988', '2006', '1962', '1924', '3', '1986','2010', '2003', '76,000 sqft', '1981', '2011','5', '1', '2005', '1975', '1984','1974', '1976', '2018', '2002', '1957', '1998','1972', '1966', '1961', '1973', '1996','1987', '2022', '1978', '1870','2017', '1969', '1956', '2013', '1985','1930', '2', '1861', '1850', '2001', '2000','1927', '1999','1959', '1980', '1967', '6', '1901',  '16','25,700.4 sqft', '1899', '1915', '1832', '1867','1977', '9999', '1968', '1931', '1910', '1970','1914', '1960','9,364.6 sqft', '1926', '1853', '1928', '1929', '1921','1938', '1945', '1964', '1913', '1881', '1925', '1875', '1911', '7,409.88 sqft']

    property_df = df[df['property_subtype'].isin(values)]
    property_df = property_df.rename(columns={'property_subtype': 'sale_'})
    property_df = property_df.rename(columns={'sale':'property_subtype'})
    property_df = property_df.rename(columns={'sale_':'sale'})

    #move columns back
    col1='property_subtype'
    col2='sale'
    property_df[[col1 if col == col2 else col2 if col == col1 else col for col in property_df.columns]]
    df.update(property_df)

    df['property_subtype'] = df['property_subtype'].str.lower()
    df['property_subtype'] = df['property_subtype'].str.replace("-", "_").str.replace(" / ", "_").str.replace(" ", "_")

    #swap values in property_subtypes and sale columns 
    values = ['other', 'finca', 'special_property']
    property_df = df[df['property_subtype'].isin(values)]
    property_df = property_df.rename(columns={'property_subtype': 'sale_'})
    property_df = property_df.rename(columns={'sale':'property_subtype'})
    property_df = property_df.rename(columns={'sale_':'sale'})

    col1='property_subtype'
    col2='sale'
    property_df[[col1 if col == col2 else col2 if col == col1 else col for col in property_df.columns]].head()
    df.update(property_df)

    #fill null values
    df['property_subtype'].fillna('-999', inplace=True)

    #standardize the spellings in groups
    df['property_subtype'] = df['property_subtype'].replace(['maison', 'huis', ' Maison', ' House', 'ander(e)'], 'house')
    df['property_subtype'] = df['property_subtype'].replace([' apartment', 'appartement', '_apartment', 'appartamento', ' apartamento', 'apartamento', 'Appartement', '_apartment', '_apartamento', ' Apartment', 'ground_floor_apartment', 'wohnung', '_wohnung', 'flat', 'etagenwohnung'], 'apartment')
    df['property_subtype'] = df['property_subtype'].replace(['établissement_historique','historische_pand'], 'historic_estate')
    df['property_subtype'] = df['property_subtype'].replace(['appartamento_duplex', 'dúplex'], 'duplex')
    df['property_subtype'] = df['property_subtype'].replace(['vrijstaande_woning'], 'detached_house')
    df['property_subtype'] = df['property_subtype'].replace(['loft_zolder', 'loft_attic', 'loft_dachgeschoss','loft_ático', 'loft_mansarde','attico'], 'loft')
    df['property_subtype'] = df['property_subtype'].replace(['investment_residential_investment', 'investering_woon__en_werkruimte'], 'investment_property')

    #standardize the spellings individually
    replace_values = {'maison_détachée': 'detached_house', 'maisonette_duplex':'duplex', 'investissement': 'investment_property', 'immeuble_spécial': 'special_property', 'duplex_apartment':'duplex', 'autre':'other'}

    df['property_subtype'] = df['property_subtype'].replace(replace_values)

    #swap values in property_subtypes and sale columns 
    values = ['investment_property']
    property_df = df[df['property_subtype'].isin(values)]
    property_df = property_df.rename(columns={'property_subtype': 'sale_'})
    property_df = property_df.rename(columns={'sale':'property_subtype'})
    property_df = property_df.rename(columns={'sale_':'sale'})

    col1='property_subtype'
    col2='sale'
    property_df[[col1 if col == col2 else col2 if col == col1 else col for col in property_df.columns]].head()
    df.update(property_df)

    #replace values
    replace_values = [' House', ' Huis', ' Maison']
    df['property_subtype'] = df['property_subtype'].replace(replace_values)

    return df['property_subtype']

