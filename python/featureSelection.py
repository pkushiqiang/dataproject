# -*- coding: utf-8 -*-
"""
Created on Wed May 06 22:47:21 2015

@author: dlmu__000
"""
from functions import * 
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

df_dummies= pd.read_csv('..\\data\\df_dummies.csv')
feature_cols = [ 'yearsExperience', 'milesFromMetropolis', 'degree_DOCTORAL', 'degree_HIGH_SCHOOL', 'degree_MASTERS', 
                 'degree_NONE', 'major_BUSINESS', 'major_CHEMISTRY', 'major_COMPSCI', 'major_ENGINEERING', 'major_LITERATURE', 'major_MATH', 'major_NONE', 'major_PHYSICS',
                 'jobType_CFO','jobType_CTO','jobType_JANITOR','jobType_JUNIOR','jobType_MANAGER','jobType_SENIOR','jobType_VICE_PRESIDENT',
                 'industry_EDUCATION','industry_FINANCE','industry_HEALTH','industry_OIL','industry_SERVICE','industry_WEB']

trainX = df_dummies[feature_cols]
trainY = df_dummies.salary  

def f_regression(X,Y):
   import sklearn
   return sklearn.feature_selection.f_regression(X,Y,center=False) #center=True (the default) would not work ("ValueError: center=True only allowed for dense data") but should presumably work in general

model = SelectKBest(score_func=f_regression, k=4).fit(trainX, trainY)
scores = zip(feature_cols, model.scores_)
sorted_scores = sorted(scores, key=lambda tup: tup[1])

from sklearn.linear_model import Lasso
lasso = Lasso(alpha=.3)
lasso.fit(trainX, trainY)

scores = zip(feature_cols, lasso.coef_)
sorted_scores = sorted(scores, key=lambda tup: tup[1])

from sklearn.linear_model import Ridge
ridge = Ridge(alpha=10)
ridge.fit(trainX, trainY)
scores = zip(feature_cols, ridge.coef_)
sorted_scores = sorted(scores, key=lambda tup: tup[1])

from sklearn.linear_model import LassoCV
cv = LassoCV()
cv.fit(trainX, trainY)

scores = zip(feature_cols, cv.coef_)
sorted_scores = sorted(scores, key=lambda tup: tup[1])

#cv.alpha_ = 0.33281631279467694