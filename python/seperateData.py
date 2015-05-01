# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:37:26 2015

@author: dlmu__000
"""

import random
count =  df_comp4_dummies.shape[0]
train_size = count*7/10
test_size = count - train_size
rows = random.sample(df_comp4_dummies.index, train_size)

df_train = df_comp4_dummies.ix[rows]
df_test = df_comp4_dummies.drop(rows)


feature_cols = [ u'yearsExperience', u'milesFromMetropolis', u'degree_DOCTORAL', u'degree_HIGH_SCHOOL', u'degree_MASTERS', u'degree_NONE', u'major_BUSINESS', u'major_CHEMISTRY', u'major_COMPSCI', u'major_ENGINEERING', u'major_LITERATURE', u'major_MATH', u'major_NONE', u'major_PHYSICS']
trainX = df_train[feature_cols]
trainY = df_train.salary

testX = df_test[feature_cols]
testY = df_test.salary

from sklearn.linear_model import LinearRegression
# instantiate, fit
lm = LinearRegression()
lm.fit(trainX, trainY)
lm.score(testX, testY)

# print coefficients
zip(feature_cols, lm.coef_)

testX = df_test[feature_cols]
predictY = lm.predict(testX)

from sklearn.metrics import mean_squared_error
mean_squared_error(testY, predictY)  