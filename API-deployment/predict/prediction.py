import pandas as pd
import sqlite3


def predict(model, json_input):    # print(json_input)
    demo1 = pd.json_normalize(json_input["data"])
    demo = {}  # this line gets only feautures we need from input json
    conn = sqlite3.connect("db/mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""select * from model""")
    df = pd.DataFrame(cursor.fetchall())
    conn.commit()
    conn.close()
    for column in json_input["data"].keys():
        demo[column] = demo1[column]
    demo = pd.json_normalize(demo)
    demo['rooms_number'] = demo['rooms-number']
    demo['postcode'] = demo['zip-code']
    demo['land_surface'] = demo['land-area']
    demo['garden_area'] = demo['garden-area']
    demo['terrace_area'] = demo['terrace-area']
    demo['equipped_kitchen_has'] = demo['equipped-kitchen']
    demo['open_fire'] = demo['open-fire']
    demo['swimming_pool_has'] = demo['swimmingpool']
    demo = demo.drop(['rooms-number', 'zip-code', 'land-area', 'garden-area',
                      'terrace-area', 'equipped-kitchen', 'open-fire', 'swimmingpool'], axis=1)
    demo = demo[df[0].array]
    cleaned_input = demo
    return {"prediction": int(model.predict(cleaned_input)[0])}
