
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

#load data
load_data = pd.read_csv('app/model/def_dataset.csv')
data = load_data.drop(['source', 'basement'], axis=1)

#fill null values with mode
data = data.fillna(data.mode().iloc[0])

#split train and test_set
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

#Set train_set to df
df = train_set

# this function defines price per area
def price_area(df1):    
    df1['coeff'] = np.where(df1['land_surface'] + df1['garden_area'] < 250, 2, np.where(df1['land_surface'] + df1['garden_area'] < 1000, 4, np.where(df1['land_surface'] + df1['garden_area'] < 5000, 8, np.where(df1['land_surface'] + df1['garden_area'] < 10000, 12, 16))))        
    df1['divisor'] = df1['area'] + df1['terrace_area'] + df1['garden_area'] / df1['coeff'] + df1['land_surface']/df1['coeff']
    df1['price_area'] = df1['price']/df1['divisor']
    f = ['open_fire', 'swimming_pool_has', 'furnished', 'equipped_kitchen_has']
    c = [-5000, -15000, -10000, -5000]
    for i in range(len(f)):
        df1['price_area'] += np.where(df1[f[i]] == True, c[i]/df1['divisor'], 0)
    factors = ['AS_NEW', 'JUST_RENOVATED', 'TO_RENOVATE', 'TO_RESTORE']
    rate = [-600, -300, 300, 600]
    for i in range(len(factors)):
        df1['price_area'] += np.where(df1['building_state_agg'] == factors[i],
                              (rate[i]*(df1['area'] + df1['terrace_area'])/df1['divisor']), 0)
    return df1

df = price_area(df)
df = df[df['price_area'] < 20000]

# filter out datapoints less than 1,000euros per area it is 3000+ records 500€=773records
# and 10,000euros per area, room_number more than 10,area more than 500sqm 
#df_filtered = df[(df['price_area'] > 500) & (df['price_area']<5500) & (df['rooms_number']<7)   & (df['area']<500)]
#df_filtered.shape

final_df = df

## Models

final_df['status']=np.where(final_df['building_state_agg'] == 'AS_NEW',(300*(final_df['area']+ final_df['terrace_area'])),np.where(final_df['building_state_agg'] == 'JUST_RENOVATED',(150*(final_df['area']+ final_df['terrace_area'])),np.where(final_df['building_state_agg'] == 'TO_RENOVATE',(-150*(final_df['area']+ final_df['terrace_area'])),np.where(final_df['building_state_agg'] == 'TO_RESTORE',(-300*(final_df['area']+ final_df['terrace_area'])),0))))
f = ['open_fire', 'swimming_pool_has', 'furnished', 'equipped_kitchen_has']
c = [5000, 25000, 20000, 10000]
for i in range(len(f)):
    final_df['status'] += np.where(final_df[f[i]] == True, c[i], 0)


#Prepare the training data
x_train = final_df.drop(['status', 'price','price_area','house_is', 'divisor', 'coeff', 'postcode', 'equipped_kitchen_has', 'garden', 'terrace'], axis=1)    

column_trans = make_column_transformer((OneHotEncoder(), ['property_subtype', 'swimming_pool_has', 'open_fire', 'building_state_agg']), remainder='passthrough')
X_train = column_trans.fit_transform(x_train)
#print("X_train: ", X_train.shape)

y_train = final_df['price']
#print("y_train: ",y_train.shape)   
                          
#Prepare the test data
x_test = test_set.drop(['price','house_is', 'postcode', 'equipped_kitchen_has', 'garden', 'terrace'], axis=1)

column_trans = make_column_transformer((OneHotEncoder(), ['property_subtype', 'swimming_pool_has', 'open_fire', 'building_state_agg']), remainder='passthrough')
X_test = column_trans.fit_transform(x_test)
print("X_test: ", X_test.shape)

y_test = test_set['price']
print("y_test: ", y_test.shape)

#linear regression model
linreg = LinearRegression().fit(X_train, y_train)
y_pred = linreg.predict(X_test)
#print('Score train:', linreg.score(X_train,y_train))
#print('Score test:', linreg.score(X_test,y_test))

##Ensemble models
#RandomForest model
from sklearn import ensemble
rfr = ensemble.RandomForestRegressor(max_depth=20, random_state=0)
rfr.fit(X_train, y_train) 
# print("RandomForestRegressor train score: ",rfr.score(X_train, y_train))
# print("RandomForestRegressor test score: ",rfr.score(X_test, y_test))

#ExtraTreesRegressor model
rfr = ensemble.ExtraTreesRegressor(n_estimators=400, random_state=5)
rfr.fit(X_train, y_train) 
# print("ExtraTreesRegressor train score: ",rfr.score(X_train, y_train))
# print("ExtraTreesRegressor test score: ",rfr.score(X_test, y_test))

#VotingRegressor model
rfr = ensemble.VotingRegressor([('lr', LinearRegression()), ('rf', ensemble.RandomForestRegressor(n_estimators=200, random_state=0))])
rfr.fit(X_train, y_train) 
# print("VotingRegressor train score: ",rfr.score(X_train, y_train))
# print("VotingRegressor test score: ",rfr.score(X_test, y_test))

#GradientBoostingRegressor model
clf = ensemble.GradientBoostingRegressor(
    n_estimators=400, max_depth=5, min_samples_split=7, learning_rate=0.1, loss='ls')
clf.fit(X_train, y_train) 
print("GradientBoostingRegressor train score: ",clf.score(X_train, y_train))
print("GradientBoostingRegressor test score: ",clf.score(X_test, y_test))


#package the model for exporting using pickle
import pickle
model_path = "./model.pkl"
pickle.dump(clf, open(model_path, 'wb'))
