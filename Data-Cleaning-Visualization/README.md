# GPT3-Challenge
Data Visualization of ImmoWeb project Data Sets 

# 1. The Project
The real estate company "ImmoEliza" wants to create a machine learning model to predict prices on Belgium's sales. This repo contains all the files that were used in this project including the raw dataset, the cleaned dataset, .ipynb files containing the code for both cleaning and analysis/visualization, and a presentation containing the results of the analysis.


## 1.1. The Team
This project was a collaborative effort between four members of the *Bouwman2* promotion at [BeCode](https://github.com/becodeorg), Brussels, in October 2020. The team comprised of [Davy Mariko](https://github.com/davymariko), [Manasa Devinoolu](https://github.com/manasanoolu7), [Sara Silvente](https://github.com/silventesa), and [Naomi Thiru](https://github.com/naomithiru)

## 1.2. Project Requirements
```pip install pandas```
```pip install numpy```
```pip install more_itertools```

# 2. Contents

This is a collection of all the properties for sale from all the regions of Belgium, to be used to create a machine learning model to predict prices on Belgium's sales for the real estate company, ImmoEliza.


## 2.1. Dataset

The data was scraped from various Belgian real-estate websites by all the members of the Bowman2 Promotion of BeCode, in September 2020.
The **raw dataset** had 93068 rows and 22 columns.

The variables in this dataset are: 
```
       'source', 'hyperlink', 'locality', 'postcode', 'house_is',
       'property_subtype', 'price', 'sale', 'rooms_number', 'area',
       'kitchen_has', 'furnished', 'open_fire', 'terrace', 'terrace_area',
       'garden', 'garden_area', 'land_surface', 'land_plot_surface',
       'facades_number', 'swimming_pool_has', 'building_state'
```

### 2.1.1. Data Cleaning
Various data cleaning operations were performed on the dataset, using **pandas** and **numpy** within [Jupyter Notebooks](https://jupyter.org/).

```
    import numpy as np
    import pandas as pd
```


Each of the 22 columns was processed using functions created specifically for their contents. An example of such a function, to clean the 'Open Fire' column is as follows:

```
def process_open_fire_col():
    dt = data_new['open_fire']
    dt.convert_dtypes()
    dt = dt.str.lower()
    dt = dt.map({'false': 0, 'true': 1, 'nan': 2, '0': 2})
    dt.fillna(2, inplace=True)
    dt = dt.astype(int)
    return dt
```

The following issues were handled as described: 

<ins> *Null Values and None* </ins>

All null values and ‘None’ values in the dataset were replaced with a value ‘-999’

<ins> *True/False Values* </ins>

All true values were replaced with the value ‘1’
All false values were replaced with the value ‘0’

<ins> *Duplicates* </ins>

The dataset had duplicated values, that were dropped.

<ins> *Blank spaces and special characters* </ins>

All blank spaces and special characters were replaced with an underscore.
All the values in the dataset were set to lowercase.

The **cleaned dataset** has 43342 rows and 24 columns.

## 2.2. Presentation

The presentation contains results of the data visualization and an interpretation of the analysis.

### 2.2.1 Data Visualization
Using [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/), visualization on a clean dataset was done to observe the correlations between the variables and the target variable.

```
    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline
```

In order to conduct analysis on the real estate dataset, we identified the target variable as ‘Price’, and used this to determine it's correlations with the other variables in the dataset.  

### 2.2.2 Interpretation
The interpretation of our results are clearly outlined in the presentation file.


# 3. Challenges and Conclusions

The dataset required a large amount of cleaning. Apart from null values, other unsuitable values were found in the dataset that were categorized as null for the sake of this analysis.
External data was integrated into the dataset to provide additional location information, such as 'city' and 'region'.

Establishing the correct datatypes to ensure smooth workflow with the data was also identified as a challenge. Working with NaN values with visualization libraries needed to be handled as well. 

