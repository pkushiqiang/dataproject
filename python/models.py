# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:38:35 2015

@author: dlmu__000
"""
from sklearn import linear_model

# instantiate, fit
model = linear_model.LinearRegression()
model = linear_model.LinearRegression(normalize=True)
model = linear_model.Lasso(alpha = 0.1)
model = linear_model.Lasso(alpha = 0.3, normalize=True)
model = linear_model.Lasso(alpha = 1)
model = linear_model.Ridge (alpha = .5)
alphas = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
model = linear_model.RidgeCV (alphas = alphas) 
model = linear_model.LassoLarsCV() 
model = linear_model.LassoLars() 
model = linear_model.ElasticNetCV(l1_ratio=0.8, alphas = alphas) 

model = linear_model.BayesianRidge()
model = linear_model.Perceptron()


from sklearn import svm
model = svm.SVR(kernel='linear')
model = svm.SVR(kernel='poly')
model = svm.SVR(kernel='rbf')

from sklearn import tree
model = tree.DecisionTreeRegressor()
model = tree.ExtraTreeRegressor()


from sklearn import ensemble 
model = ensemble.RandomForestRegressor(n_estimators=100, max_depth=None,min_samples_split=1, random_state=0)

model = ensemble.ExtraTreesRegressor(n_estimators=20, max_depth=None,min_samples_split=1, random_state=0)

model = ensemble.AdaBoostRegressor(n_estimators=100)

model = ensemble.GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,  max_depth=1, random_state=0, loss='ls')

