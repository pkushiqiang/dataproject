# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:38:35 2015

@author: dlmu__000
"""

from sklearn.linear_model import LinearRegression
# instantiate, fit
lm = LinearRegression()
feature_cols = [ u'yearsExperience', u'milesFromMetropolis', u'degree_DOCTORAL', u'degree_HIGH_SCHOOL', u'degree_MASTERS', u'degree_NONE', u'major_BUSINESS', u'major_CHEMISTRY', u'major_COMPSCI', u'major_ENGINEERING', u'major_LITERATURE', u'major_MATH', u'major_NONE', u'major_PHYSICS']

result = cross_evaluate(lm, df_web_ceo_dummies, feature_cols)  



from sklearn import linear_model
model = linear_model.Ridge (alpha = .5)

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
model = linear_model.Lasso(alpha = 0.1)
model = linear_model.BayesianRidge()
model = linear_model.Perceptron()


from sklearn import svm

model = svm.SVR()
model = svm.SVR(kernel='linear')
model = svm.SVR(kernel='poly')

res = predict(model, df_web_ceo_dummies,  feature_cols )
result = cross_evaluate(model, df_web_ceo_dummies, feature_cols)  

from sklearn import tree
model = tree.DecisionTreeRegressor()

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=10, max_depth=None,min_samples_split=1, random_state=0)

from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor(n_estimators=10, max_depth=None,min_samples_split=1, random_state=0)

from  sklearn.ensemble import  AdaBoostRegressor
model =  AdaBoostRegressor(n_estimators=100)

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,  max_depth=1, random_state=0, loss='ls')