import numpy as np
import pandas as pd
import re

def clean_hyperlink_column(data_new):

    data_new.hyperlink.fillna(-999, inplace=True)
    for u in range(len(data_new.hyperlink)):
        if 'realo' in str(data_new.hyperlink[u]):
            data_new.hyperlink[u] = -999
        elif 'immoweb' in str(data_new.hyperlink[u]):
            code = [re.findall(r'\d+', ti) for ti in str(data_new.hyperlink[u]).split("/")]
            for ti in code:
                try:
                    if len(ti[0]) == 7:
                        data_new.hyperlink[u] = ti[0]
                except:
                    pass
        else:
            pass
        
    return data_new.hyperlink


def clean_price_column(data_new):

    price_list = []
    for dat in data_new.price:
        try:
            dat = str(dat)
            if dat.startswith("€"):
                if int(dat[1: ]) < 2500:
                    dat = int(dat[1: ]) * 1000
                else:
                    dat = int(dat[1: ])
                price_list.append(dat)
            elif "€" in dat:
                if int(dat[ 0 : dat.index("€")]) < 2500:
                    dat = int(dat[ 0 : dat.index("€")]) * 1000
                else:
                    dat = int(dat[ 0 : dat.index("€")])
                price_list.append(dat)
            else:
                if int(dat) < 2500:
                    dat = int(dat) * 1000
                else:
                    dat = int(dat)
                price_list.append(dat)
                
        except:
            price_list.append(-999)
    
    data_new.price = price_list        
    data_new.price = data_new.price.replace([0], -999)

    return data_new.price


def clean_garden_column(data_new):
        
    data_new.garden.replace({'\d+': 0}, regex=True, inplace = True)    
    data_new.garden.replace(to_replace =["False"],  value = 0, inplace = True)
    data_new.garden.replace(to_replace =["True"], value = 1, inplace =  True)
    data_new.garden.fillna(-99, inplace=True)

    return data_new.garden


def clean_garden_area(data_new):
    
    data_new.garden_area.fillna(-999, inplace=True)
    data_new.garden_area.replace(to_replace =['None'],  value = -999, inplace = True)

    return data_new.garden_area


def clean_sale_column(data_new):
    
    data_new.sale.fillna(-999, inplace=True)
    data_new.sale.replace(to_replace =['None'],  value = -999, inplace = True)

    return data_new.sale


def clean_swimming_pool(data_new):
    
    data_new.swimming_pool_has.fillna(-999, inplace=True)
    data_new.swimming_pool_has.replace(to_replace =['True'],  value = 1, inplace = True)
    data_new.swimming_pool_has.replace(to_replace =['TRUE'],  value = 1, inplace = True)
    data_new.swimming_pool_has.replace(to_replace =['False'],  value = 0, inplace = True)
    data_new.swimming_pool_has.replace(to_replace =['FALSE'],  value = 0, inplace = True)

    return data_new.swimming_pool_has
