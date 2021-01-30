from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3
import datetime

count = 0
skipped = 0
duplicate = 0
ids = []
type_of_property = []
type_properties = []
type_subproperties = []
prices = []
localities = []
netHabitableSurfaces = []
nr_bedrooms = []
kitchen_installeds = []
latitude = []
longitude = []
nr_facades = []
hasGardens = []
garden_m2s = []
hasTerraces = []
terrace_m2s = []
furnished_YNs = []
swimpool_YNs = []
type_of_sales = []
lands = []
basements = []
buildings = []
fireplaceExists = []


def demo(param=0):
    global count
    global skipped
    global duplicate
    global ids
    global type_properties
    global type_subproperties
    global prices
    global localities
    global netHabitableSurfaces
    global nr_bedrooms
    global kitchen_installeds
    global latitude
    global longitude
    global nr_facades
    global hasGardens
    global garden_m2s
    global hasTerraces
    global terrace_m2s
    global furnished_YNs
    global swimpool_YNs
    global type_of_sales
    global lands
    global basements
    global buildings
    global fireplaceExists
    # fields to add to a list
    global id
    global type_of_property
    global subtype_of_property
    global price
    global location
    global netHabitableSurface
    global bedroomCount
    global kitchen
    global facadeCount
    global hasGarden
    global gardenSurface
    global hasTerrace
    global terraceSurface
    global isFurnished
    global hasSwimmingPool
    global type_of_sale
    global land
    global basement
    global building
    global fireplaceExist
    global data
    conn = sqlite3.connect("db/mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""select "index" from news""")
    df = pd.DataFrame(cursor.fetchall())
    conn.close()
    count = 0
    skipped = 0
    duplicate = 0
    ids = []
    type_of_property = []
    type_properties = []
    type_subproperties = []
    prices = []
    localities = []
    netHabitableSurfaces = []
    nr_bedrooms = []
    kitchen_installeds = []
    latitude = []
    longitude = []
    nr_facades = []
    hasGardens = []
    garden_m2s = []
    hasTerraces = []
    terrace_m2s = []
    furnished_YNs = []
    swimpool_YNs = []
    type_of_sales = []
    lands = []
    basements = []
    buildings = []
    fireplaceExists = []
    for link in df[0]:
        # print("link----", count, len(links))
        count += 1
        # if "8887719" in link:
        if count >= 1000*param+1 and count <= 1000*(1+param):
            # if count >= 1 and count <= len(df[0])-1:
            # print("count >= 1 and count <= len(links):")
            try:
                no_data = False
                response = requests.get(
                    f"http://www.immoweb.be/en/classified/{link}")
                s = BeautifulSoup(response.content, 'lxml')
                k = 0
                print(count, "======", link)
                for script in s.find_all('script'):
                    k += 1
                    if k == 8:
                        # question_mark = link.index('?')
                        # id = link[question_mark-7:question_mark]
                        # if id in ids:
                        #     duplicate += 1
                        #     break  # id is in the list then skip
                        type_of_property = ""
                        subtype_of_property = ""
                        price = 0
                        location = 0
                        netHabitableSurface = 0
                        bedroomCount = 0
                        kitchen = False
                        longit = 0
                        latitu = 0
                        facadeCount = 0
                        hasGarden = False
                        gardenSurface = 0
                        hasTerrace = False
                        terraceSurface = 0
                        isFurnished = False
                        hasSwimmingPool = False
                        type_of_sale = ""
                        land = 0
                        basement = 0
                        building = ""
                        fireplaceExist = False
                        index = script.string.index('=')
                        indexNV = []
                        for i in range(0, len(script.string)):
                            if script.string[i] == ";":
                                indexNV.append(i)
                        index2 = indexNV[len(indexNV)-1]
                        null = ""
                        true = True
                        false = False
                        try:
                            i_window = script.string.index(
                                'window.classified')  # 237
                            i_media = script.string.index('"media"')
                            i_property = script.string.index('"property"')
                            data = eval(script.string[index+1:i_media] +
                                        script.string[i_property:index2])
                            id = link  # data['id']
                            pass
                        except ValueError:
                            no_data = True
                            pass
                        if data['flags']['isLifeAnnuitySale'] == False and not no_data and not 'HOUSE_GROUP' in data['property']['type'] and not 'APARTMENT_GROUP' in data['property']['type']:
                            for x in data['flags']:
                                if data['flags'][x]:
                                    type_of_sale = x
                            for x in data['transaction']['sale']:
                                if x == 'price':
                                    if data['transaction']['sale']['price'] == "":
                                        c = 'cluster'
                                        u = 'units'
                                        i = 'items'
                                        p = 'price'
                                        if data['flags']['isSoldOrRented'] == True:
                                            price = 0
                                        else:
                                            if data[c] == "":
                                                price = 0
                                            else:
                                                for a in data[c][u][0][i]:
                                                    if a['saleStatus'] == 'AVAILABLE':
                                                        price = int(a[p])
                                    else:
                                        price = int(
                                            data['transaction']['sale'][x])
                                elif x == 'isFurnished':
                                    if data['transaction']['sale'][x] == True:
                                        isFurnished = True
                                    else:
                                        isFurnished = False
                            for x in data['property']:
                                if x == 'location':
                                    try:
                                        location = int(
                                            data['property'][x]['postalCode'])
                                        pass
                                    except:
                                        location = 0
                                        pass
                                    try:
                                        latitu = float(
                                            data['property'][x]['latitude'])
                                        longit = float(
                                            data['property'][x]['longitude'])
                                        pass
                                    except:
                                        latitu = 0
                                        longit = 0
                                        pass

                                elif x == 'type':
                                    if data['property'][x] == "HOUSE":
                                        type_of_property = 1
                                    else:
                                        type_of_property = 0
                                elif x == 'subtype':
                                    subtype_of_property = data['property'][x]
                                elif x == 'bedroomCount':
                                    if data['property'][x] == "":
                                        if data['cluster'] == "":
                                            bedroomCount = 0
                                        else:
                                            bedroomCount = int(
                                                data['cluster']['units'][0]['items'][0]['bedroomCount'])
                                    else:
                                        bedroomCount = int(data['property'][x])
                                elif x == 'netHabitableSurface':
                                    if data['property'][x] == "":
                                        c = 'cluster'
                                        u = 'units'
                                        i = 'items'
                                        s = 'surface'
                                        if data[c] == "":
                                            netHabitableSurface = 0
                                        else:
                                            for a in data[c][u][0][i]:
                                                if a['saleStatus'] == 'AVAILABLE':
                                                    netHabitableSurface = int(
                                                        a[s])
                                    else:
                                        netHabitableSurface = int(
                                            data['property'][x])
                                elif x == 'kitchen':
                                    if len(data['property'][x]) > 0:
                                        kitchen = True
                                    else:
                                        kitchen = False
                                elif x == 'fireplaceExists':
                                    if data['property'][x] == "False" or data['property'][x] == False:
                                        fireplaceExist = False
                                    else:
                                        fireplaceExist = True
                                elif x == 'hasTerrace':
                                    if data['property'][x] == "" or data['property'][x] == "False" or data['property'][x] == "false":
                                        hasTerrace = False
                                    else:
                                        if data['property'][x] == "False" or data['property'][x] == False:
                                            hasTerrace = False
                                        else:
                                            hasTerrace = True
                                        if data['property']['terraceSurface']:
                                            terraceSurface = int(
                                                data['property']['terraceSurface'])
                                        else:
                                            terraceSurface = 0
                                elif x == 'hasGarden':
                                    if data['property']['gardenSurface'] == "":
                                        hasGarden = False
                                    else:
                                        if data['property'][x] == "False" or data['property'][x] == False:
                                            hasGarden = False
                                        else:
                                            hasGarden = True
                                        if data['property']['gardenSurface']:
                                            gardenSurface = int(
                                                data['property']['gardenSurface'])
                                        else:
                                            gardenSurface = 0
                                elif x == 'land':
                                    if len(data['property'][x]) > 0:
                                        if data['property']['land']['surface'] == "" or data['property']['land']['surface'] == null or data['property']['land']['surface'] == None:
                                            land = 0
                                        else:
                                            land = int(
                                                data['property'][x]['surface'])
                                    else:
                                        land = 0
                                elif x == 'facadeCount':
                                    facadeCount = int(data['property'][x])
                                elif x == 'hasSwimmingPool':
                                    if data['property'][x] == True:
                                        hasSwimmingPool = True
                                    else:
                                        hasSwimmingPool = False
                                elif x == 'building':
                                    if data['property'][x] == "":
                                        building = "Not specified"
                                    else:
                                        building = data['property'][x]['condition']
                                elif x == 'basement':  # Surface area of the plot of land
                                    if data['property']['basement'] == "":
                                        if data['property']['land'] == "":
                                            basement = 0
                                        else:
                                            if data['property']['land']['surface'] == "" or data['property']['land']['surface'] == null or data['property']['land']['surface'] == None:
                                                basement = 0
                                            else:
                                                basement = int(
                                                    data['property']['land']['surface'])
                                    elif data['property']['basement']['surface']:
                                        basement = int(
                                            data['property']['basement']['surface'])
                                    else:
                                        basement = 0
                        else:
                            skipped += 1
                        if type_of_property == "":
                            skipped += 1
                        else:
                            ids.append(id)
                            type_properties.append(type_of_property)
                            type_subproperties.append(subtype_of_property)
                            prices.append(price)
                            localities.append(location)
                            netHabitableSurfaces.append(netHabitableSurface)
                            nr_bedrooms.append(bedroomCount)
                            kitchen_installeds.append(kitchen)
                            longitude.append(longit)
                            latitude.append(latitu)
                            nr_facades.append(facadeCount)
                            hasGardens.append(hasGarden)
                            garden_m2s.append(gardenSurface)
                            hasTerraces.append(hasTerrace)
                            terrace_m2s.append(terraceSurface)
                            furnished_YNs.append(isFurnished)
                            swimpool_YNs.append(hasSwimmingPool)
                            type_of_sales.append(type_of_sale)
                            lands.append(land)
                            if basement == 0:
                                if land == 0:
                                    basements.append(netHabitableSurface)
                                else:
                                    basements.append(land)
                            else:
                                basements.append(basement)
                            buildings.append(building)
                            fireplaceExists.append(fireplaceExist)
                pass
            except:
                skipped += 1
                pass
    print("skipped=", skipped, "duplicate = ", duplicate)
    data = {'index': ids, 'house_is': type_properties, 'property_subtype': type_subproperties, 'price': prices,
            'postcode': localities, 'area': netHabitableSurfaces,
            'rooms_number': nr_bedrooms, 'kitchen_has': kitchen_installeds,
            'garden': hasGardens, 'garden_area': garden_m2s, 'terrace': hasTerraces, 'terrace_area': terrace_m2s,
            'furnished': furnished_YNs, 'swimming_pool_has': swimpool_YNs,
            'land_surface': lands, 'land_plot_surface': basements, 'building_state': buildings, 'open_fire': fireplaceExists, 'longitude': longitude, 'latitude': latitude, 'datum': datetime.datetime.now()
            }
    df_new = pd.DataFrame(
        data, columns=['index', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
                       'rooms_number', 'kitchen_has', 'garden', 'garden_area', 'terrace', 'terrace_area',
                       'furnished', 'swimming_pool_has',
                       'land_surface', 'land_plot_surface', 'building_state', 'open_fire', 'longitude', 'latitude', 'datum'])
    conn = sqlite3.connect("db/mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""select * from scrapped""")
    df_old = pd.DataFrame(cursor.fetchall(), columns=['index', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
                                                      'rooms_number', 'kitchen_has', 'garden', 'garden_area', 'terrace', 'terrace_area',
                                                      'furnished', 'swimming_pool_has',
                                                      'land_surface', 'land_plot_surface', 'building_state', 'open_fire', 'longitude', 'latitude', 'datum'])
    # df_old['datum'] = datetime.datetime.now()
    df_old['datum'] = pd.to_datetime(
        df_old['datum'], infer_datetime_format=True)
    # print("----- old -------", df_old.shape, df_old.info())
    df_old = df_old.append(df_new)
    df_old = df_old.reset_index(drop=True)
    # print("----- old 2 -------", df_old, df_old.info())
    # print("----- new -------", df_new.shape, df_new, df_new.info())
    df_old["index"] = pd.to_numeric(
        df_old["index"], downcast="integer")
    df_old["house_is"] = pd.to_numeric(
        df_old["house_is"], downcast="integer").astype('bool')
    df_old["price"] = pd.to_numeric(
        df_old["price"], downcast="integer")
    df_old["postcode"] = pd.to_numeric(
        df_old["postcode"], downcast="integer")
    df_old["area"] = pd.to_numeric(df_old["area"], downcast="integer")
    df_old["rooms_number"] = pd.to_numeric(
        df_old["rooms_number"], downcast="integer")
    df_old["kitchen_has"] = pd.to_numeric(
        df_old["kitchen_has"], downcast="integer").astype('bool')
    df_old["garden"] = pd.to_numeric(
        df_old["garden"], downcast="integer").astype('bool')
    df_old["garden_area"] = pd.to_numeric(
        df_old["garden_area"], downcast="integer")
    df_old["terrace"] = pd.to_numeric(
        df_old["terrace"], downcast="integer").astype('bool')
    df_old["terrace_area"] = pd.to_numeric(
        df_old["terrace_area"], downcast="integer")
    df_old["furnished"] = pd.to_numeric(
        df_old["furnished"], downcast="integer").astype('bool')
    df_old["swimming_pool_has"] = pd.to_numeric(
        df_old["swimming_pool_has"], downcast="integer").astype('bool')
    df_old["land_surface"] = pd.to_numeric(
        df_old["land_surface"], downcast="integer")
    df_old["land_plot_surface"] = pd.to_numeric(
        df_old["land_plot_surface"], downcast="integer")
    df_old["open_fire"] = pd.to_numeric(
        df_old["open_fire"], downcast="integer").astype('bool')
    df_old["longitude"] = pd.to_numeric(
        df_old["longitude"], downcast="float")
    df_old["latitude"] = pd.to_numeric(
        df_old["latitude"], downcast="float")
    df_old["datum"] = pd.to_datetime(df_old["datum"])
    df_old.to_sql(name='scrapped', con=conn,
                  if_exists='replace', index=False)
    conn.close()
    print(len(df_new), " new records added to scrapped and total scrapped is", len(df_old))
    # print("Finished records = ", len(ids), len(type_properties), len(type_subproperties), len(prices), len(localities), len(netHabitableSurfaces), len(nr_bedrooms), len(kitchen_installeds), len(nr_facades),
    #       len(hasGardens), len(garden_m2s), len(hasTerraces), len(terrace_m2s), len(furnished_YNs), len(swimpool_YNs), len(type_of_sales), len(lands), len(basements), len(buildings), len(fireplaceExists))


def p1(param):  # limits just x1000 record  parameter will set which order of 1000 record from news
    global count
    count = 0
    skipped = 0
    duplicate = 0
    ids = []
    type_properties = []
    type_subproperties = []
    prices = []
    localities = []
    netHabitableSurfaces = []
    nr_bedrooms = []
    kitchen_installeds = []
    latitude = []
    longitude = []
    nr_facades = []
    hasGardens = []
    garden_m2s = []
    hasTerraces = []
    terrace_m2s = []
    furnished_YNs = []
    swimpool_YNs = []
    type_of_sales = []
    lands = []
    basements = []
    buildings = []
    fireplaceExists = []
    # fields to add to a list
    id = 0
    type_of_property = ""
    subtype_of_property = ""
    price = 0
    location = 0
    netHabitableSurface = 0
    bedroomCount = 0
    kitchen = False
    facadeCount = 0
    hasGarden = False
    gardenSurface = 0
    hasTerrace = False
    terraceSurface = 0
    isFurnished = False
    hasSwimmingPool = False
    type_of_sale = ""
    land = 0
    basement = 0
    building = ""
    fireplaceExist = False

    try:
        demo(param)
    except KeyboardInterrupt:
        # print("skipped=", skipped, "duplicate = ", duplicate)
        data = {'index': ids, 'house_is': type_properties, 'property_subtype': type_subproperties, 'price': prices,
                'postcode': localities, 'area': netHabitableSurfaces,
                'rooms_number': nr_bedrooms, 'kitchen_has': kitchen_installeds,
                'garden': hasGardens, 'garden_area': garden_m2s, 'terrace': hasTerraces, 'terrace_area': terrace_m2s,
                'furnished': furnished_YNs, 'swimming_pool_has': swimpool_YNs,
                'land_surface': lands, 'land_plot_surface': basements, 'building_state': buildings, 'open_fire': fireplaceExists, 'longitude': longitude, 'latitude': latitude, 'datum': datetime.datetime.now()
                }
        df_new = pd.DataFrame(data, columns=['index', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
                                             'rooms_number', 'kitchen_has', 'garden', 'garden_area', 'terrace', 'terrace_area',
                                             'furnished', 'swimming_pool_has',
                                             'land_surface', 'land_plot_surface', 'building_state', 'open_fire', 'longitude', 'latitude', 'datum'])
        conn = sqlite3.connect("db/mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""select * from scrapped""")
        df_old = pd.DataFrame(cursor.fetchall(), columns=['index', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
                                                          'rooms_number', 'kitchen_has', 'garden', 'garden_area', 'terrace', 'terrace_area',
                                                          'furnished', 'swimming_pool_has',
                                                          'land_surface', 'land_plot_surface', 'building_state', 'open_fire', 'longitude', 'latitude', 'datum'])
        # df_old['datum'] = datetime.datetime.now()
        df_old['datum'] = pd.to_datetime(
            df_old['datum'], infer_datetime_format=True)
        # print("----- old -------", df_old.shape, df_old.info())
        df_old = df_old.append(df_new)
        df_old = df_old.reset_index(drop=True)
        # print("----- old 2 -------", df_old, df_old.info())
        # print("----- new -------", df_new.shape, df_new, df_new.info())
        df_old["index"] = pd.to_numeric(
            df_old["index"], downcast="integer")
        df_old["house_is"] = pd.to_numeric(
            df_old["house_is"], downcast="integer").astype('bool')
        df_old["price"] = pd.to_numeric(
            df_old["price"], downcast="integer")
        df_old["postcode"] = pd.to_numeric(
            df_old["postcode"], downcast="integer")
        df_old["area"] = pd.to_numeric(df_old["area"], downcast="integer")
        df_old["rooms_number"] = pd.to_numeric(
            df_old["rooms_number"], downcast="integer")
        df_old["kitchen_has"] = pd.to_numeric(
            df_old["kitchen_has"], downcast="integer").astype('bool')
        df_old["garden"] = pd.to_numeric(
            df_old["garden"], downcast="integer").astype('bool')
        df_old["garden_area"] = pd.to_numeric(
            df_old["garden_area"], downcast="integer")
        df_old["terrace"] = pd.to_numeric(
            df_old["terrace"], downcast="integer").astype('bool')
        df_old["terrace_area"] = pd.to_numeric(
            df_old["terrace_area"], downcast="integer")
        df_old["furnished"] = pd.to_numeric(
            df_old["furnished"], downcast="integer").astype('bool')
        df_old["swimming_pool_has"] = pd.to_numeric(
            df_old["swimming_pool_has"], downcast="integer").astype('bool')
        df_old["land_surface"] = pd.to_numeric(
            df_old["land_surface"], downcast="integer")
        df_old["land_plot_surface"] = pd.to_numeric(
            df_old["land_plot_surface"], downcast="integer")
        df_old["open_fire"] = pd.to_numeric(
            df_old["open_fire"], downcast="integer").astype('bool')
        df_old["longitude"] = pd.to_numeric(
            df_old["longitude"], downcast="float")
        df_old["latitude"] = pd.to_numeric(
            df_old["latitude"], downcast="float")
        df_old["datum"] = pd.to_datetime(df_old["datum"])
        df_old.to_sql(name='scrapped', con=conn,
                      if_exists='replace', index=False)
        conn.close()
        # print("Finished records = ", len(ids), len(type_properties), len(type_subproperties), len(prices), len(localities), len(netHabitableSurfaces), len(nr_bedrooms), len(kitchen_installeds), len(nr_facades),
        print(
            len(df_new), " new records added to scrapped and total scrapped is", len(df_old))
        #   len(hasGardens), len(garden_m2s), len(hasTerraces), len(terrace_m2s), len(furnished_YNs), len(swimpool_YNs), len(type_of_sales), len(lands), len(basements), len(buildings), len(fireplaceExists))
