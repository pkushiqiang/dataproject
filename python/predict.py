# -*- coding: utf-8 -*-
"""
Created on Wed May 06 22:53:43 2015

@author: dlmu__000
"""

from functions import * 
import pandas as pd

df_dummies= pd.read_csv('..\\data\\df_dummies.csv')
feature_cols = [ 'yearsExperience', 'milesFromMetropolis', 'degree_DOCTORAL', 'degree_HIGH_SCHOOL', 'degree_MASTERS', 
                 'degree_NONE', 'major_BUSINESS', 'major_CHEMISTRY', 'major_COMPSCI', 'major_ENGINEERING', 'major_LITERATURE', 'major_MATH', 'major_NONE', 'major_PHYSICS',
                 'jobType_CFO','jobType_CTO','jobType_JANITOR','jobType_JUNIOR','jobType_MANAGER','jobType_SENIOR','jobType_VICE_PRESIDENT',
                 'industry_EDUCATION','industry_FINANCE','industry_HEALTH','industry_OIL','industry_SERVICE','industry_WEB']

trainX = df_dummies[feature_cols]
trainY = df_dummies.salary  
df_test_dummies=pd.read_csv('..\\data\\df_test_dummies.csv')

testX = df_test_dummies[feature_cols]
from sklearn import linear_model

model = linear_model.Lasso(alpha = 0.3328)
#model = linear_model.LinearRegression()
model.fit(trainX, trainY)
predictY = model.predict(testX)
