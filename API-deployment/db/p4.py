import pickle
from numpy.lib.shape_base import column_stack
from sklearn import ensemble
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from os import path
import sqlite3


def p4():
    conn = sqlite3.connect("db/mydatabase.db")
    # update cleaned table because your model has to have the same shape
    # so property_subtype and building_state_agg should have the same size option not more
    # if these two columns have more than existed options then set for new option an old one as default
    # because we set column names based on dummy columns, if dummy options increase prediction will be crashed
    # other option is check new options from property_subtype and building_state_agg then add new dummy columns to the prediction-preprocessing-steps
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE cleaned SET property_subtype = "OTHER_PROPERTY" WHERE property_subtype is null""")
    conn.commit()
    cursor.execute(
        """UPDATE cleaned SET building_state_agg = "GOOD" WHERE building_state_agg is null""")
    conn.commit()
    conn.close()
    # not => if p3 did not make enough correct cleaning so null or blank values in dummy variables ALSO they can be crashed
    conn = sqlite3.connect("db/mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""select * from cleaned""")
    df = pd.DataFrame(cursor.fetchall(), columns=['index', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
                                                  'rooms_number', 'equipped_kitchen_has', 'garden', 'garden_area',
                                                  'terrace', 'terrace_area', 'furnished', 'swimming_pool_has',
                                                  'land_surface', 'open_fire',
                                                  'longitude', 'latitude', 'datum', 'building_state_agg'])
    df["index"] = pd.to_numeric(df["index"], downcast="integer")
    df["house_is"] = pd.to_numeric(
        df["house_is"], downcast="integer").astype('bool')
    df["price"] = pd.to_numeric(df["price"], downcast="integer")
    df["postcode"] = pd.to_numeric(df["postcode"], downcast="integer")
    df["area"] = pd.to_numeric(df["area"], downcast="integer")
    df["rooms_number"] = pd.to_numeric(df["rooms_number"], downcast="integer")
    df["equipped_kitchen_has"] = pd.to_numeric(
        df["equipped_kitchen_has"], downcast="integer").astype('bool')
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
    df["open_fire"] = pd.to_numeric(
        df["open_fire"], downcast="integer").astype('bool')
    df["longitude"] = pd.to_numeric(df["longitude"], downcast="float")
    df["latitude"] = pd.to_numeric(df["latitude"], downcast="float")
    df["datum"] = pd.to_datetime(df["datum"])
    conn.commit()
    conn.close()

    final_df = df.fillna(df.mode().iloc[0])
    X = final_df.drop(['index', 'house_is', 'datum', 'price'], axis=1)
    # print(X["furnished"])
    X["furnished"] = [True if x == "True" else False for x in X["furnished"]]
    X["swimming_pool_has"] = [True if x ==
                              "True" else False for x in X["swimming_pool_has"]]
    X["terrace"] = [True if x == "True" else False for x in X["terrace"]]
    X["garden"] = [True if x == "True" else False for x in X["garden"]]
    X["open_fire"] = [True if x == "True" else False for x in X["open_fire"]]
    X["equipped_kitchen_has"] = [True if x ==
                                 "True" else False for x in X["equipped_kitchen_has"]]

    X = pd.get_dummies(X, prefix=['col1', 'col2'])
    # X = X.drop(['col1_TRIPLEX', 'col1_VILLA'], axis=1)
    y = final_df['price']
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=2)
    # columns =
    # print(columns)
    conn = sqlite3.connect("db/mydatabase.db")
    pd.DataFrame(X.columns.values).drop_duplicates().to_sql(name='model', con=conn,
                                                            if_exists='replace', index=False)
    conn.commit()
    pd.DataFrame(df["property_subtype"].unique()).to_sql(name='property_subtype', con=conn,
                                                         if_exists='replace', index=False)
    conn.commit()
    pd.DataFrame(df["building_state_agg"].unique()).to_sql(name='building_state_agg', con=conn,
                                                           if_exists='replace', index=False)
    conn.commit()
    conn.close()
    # print("========== MODEL", len(x_train.columns.values))
    clf = ensemble.GradientBoostingRegressor(
        n_estimators=800, max_depth=6, min_samples_split=2, learning_rate=0.05, loss='ls')
    clf.fit(x_train, y_train)

    if path.exists("model/oldmodel.pkl"):
        os.remove("model/oldmodel.pkl")
        print("model removed!")

    if path.exists("model/model.pkl"):
        os.rename("model/model.pkl", "model/oldmodel.pkl")
        print("model renamed!")

    model_path = "model/model.pkl"
    pickle.dump(clf, open(model_path, 'wb'))
    print("new model saved!")
    model = pickle.load(open('./model/model.pkl', 'rb'))
    return model
