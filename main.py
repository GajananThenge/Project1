# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 18:11:47 2018

@author: hp-pc
"""

import sqlite3 
import pandas as pd
from sklearn.tree import DecisionTreeRegressor 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error 
from math import sqrt
# Create your connection. 
try:
    cnx = sqlite3.connect('data\database.sqlite') 
    df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)
    dataset = df.loc[:,['overall_rating','potential', 'short_passing', 'long_passing', 'volleys','dribbling',
       'ball_control','reactions', 'shot_power','strength', 'long_shots', 'aggression', 'interceptions',
       'positioning', 'vision', 'penalties']]
    
    dataset.dropna(inplace=True)
    
    # count the number of NaN values in each column
    print(dataset.isnull().sum())
    #preferred_foot [Right,left]
#    attacking_work_rate [high,medium,None ]
#    defensive_work_rate [medium,low] 
    
    '''['id', 'player_fifa_api_id', 'player_api_id', 'date',
       'overall_rating', 'potential', 'preferred_foot',
       'attacking_work_rate', 'defensive_work_rate', 'crossing',
       'finishing', 'heading_accuracy', 'short_passing', 'volleys',
       'dribbling', 'curve', 'free_kick_accuracy', 'long_passing',
       'ball_control', 'acceleration', 'sprint_speed', 'agility',
       'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions',
       'positioning', 'vision', 'penalties', 'marking', 'standing_tackle',
       'sliding_tackle', 'gk_diving', 'gk_handling', 'gk_kicking',
       'gk_positioning', 'gk_reflexes']'''
    
    X = dataset[['potential', 'short_passing', 'long_passing',
       'ball_control','reactions', 'shot_power','strength', 'long_shots', 'volleys','dribbling','aggression', 'interceptions',
       'positioning', 'vision', 'penalties']].values
    
    y = dataset['overall_rating'].values
    
     #Splittinvg thedataset into train_test_split
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=.25,random_state=0)
    
    
    model = LinearRegression()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    
    resulf_df = pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
    print(model.score(X_test,y_test))
    
except Exception as e:
    print(e)
    
finally:
    print("Closing Db Connection")
    cnx.close()