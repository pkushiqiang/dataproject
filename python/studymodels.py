# -*- coding: utf-8 -*-
"""
Created on Tue May 05 00:10:43 2015

@author: dlmu__000
"""
from functions import * 
import pandas as pd

df_dummies= pd.read_csv('..\\data\\df_dummies.csv')
feature_cols = [ 'yearsExperience', 'milesFromMetropolis', 'degree_DOCTORAL', 'degree_HIGH_SCHOOL', 'degree_MASTERS', 
                 'degree_NONE', 'major_BUSINESS', 'major_CHEMISTRY', 'major_COMPSCI', 'major_ENGINEERING', 'major_LITERATURE', 'major_MATH', 'major_NONE', 'major_PHYSICS',
                 'jobType_CFO','jobType_CTO','jobType_JANITOR','jobType_JUNIOR','jobType_MANAGER','jobType_SENIOR','jobType_VICE_PRESIDENT',
                 'industry_EDUCATION','industry_FINANCE','industry_HEALTH','industry_OIL','industry_SERVICE','industry_WEB']

from sklearn.linear_model import LinearRegression

# instantiate, fit
model = LinearRegression()

from sklearn import linear_model
model = linear_model.Ridge (alpha = .5)
model = linear_model.Lasso(alpha = 0.5)
result = split_evaluate(model, df_dummies, feature_cols)  

print result

