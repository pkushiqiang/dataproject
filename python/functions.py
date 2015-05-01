# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:17:34 2015

@author: dlmu__000
"""
from sklearn import metrics 
from sklearn import cross_validation
import numpy as np
import pandas
import random
import numpy
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def split_evaluate(model, df,   feature_cols ):    
    
    count =  df.shape[0]
    train_size = count*7/10    
    rows = random.sample(df.index, train_size)    
    df_train = df.ix[rows]
    df_test = df.drop(rows)    
    
    trainX = df_train[feature_cols]
    trainY = df_train.salary    
    testX = df_test[feature_cols]
    testY = df_test.salary   
    
    model.fit(trainX, trainY)
    predictY = model.predict(testX)
    
    result ={}
    result["mean absolute error"] = mean_absolute_error(testY, predictY)
    result["mean squared error"] = mean_squared_error(testY, predictY)
    result["r2"] = r2_score(testY, predictY)
    
    return result

def cross_evaluate(model, df, feature_cols ):
    
    X = df[feature_cols]
    Y = df.salary
    lm = model 
    result = {};
    scores = cross_validation.cross_val_score(lm, X, Y ,cv=10, scoring='mean_squared_error')     
    result["mean_squared_error"] = np.mean(scores)  
    scores = cross_validation.cross_val_score(lm, X, Y ,cv=10, scoring='mean_absolute_error')
    result["mean_absolute_error"] = np.mean(scores) 
    scores = cross_validation.cross_val_score(lm, X, Y ,cv=10, scoring='r2')
    result["r2"] = np.mean(scores)      
    
    return result
    
from sklearn.linear_model import LinearRegression
# instantiate, fit
lm = LinearRegression()
feature_cols = [ u'yearsExperience', u'milesFromMetropolis', u'degree_DOCTORAL', u'degree_HIGH_SCHOOL', u'degree_MASTERS', u'degree_NONE', u'major_BUSINESS', u'major_CHEMISTRY', u'major_COMPSCI', u'major_ENGINEERING', u'major_LITERATURE', u'major_MATH', u'major_NONE', u'major_PHYSICS']

result = cross_evaluate(lm, df_web_ceo_dummies, feature_cols)  


result = split_evaluate(model, df_web_ceo_dummies, feature_cols)  
