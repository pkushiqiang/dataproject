# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:39:28 2015

@author: dlmu__000
"""

from sklearn import metrics 
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression

X = df_comp4_dummies[feature_cols]
Y = df_comp4_dummies.salary
lm = LinearRegression() 

scores = cross_validation.cross_val_score(lm, X, Y ,cv=10, scoring='mean_squared_error')
np.mean(scores)   

scores = cross_validation.cross_val_score(lm, X, Y ,cv=10, scoring='mean_absolute_error')
np.mean(scores)                             
                          

# scoring 
#  mean_absolute_error  	metrics.mean_absolute_error	 
#mean_squared_error  	metrics.mean_squared_error	 
#r2 	 