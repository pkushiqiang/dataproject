# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:26:46 2015

@author: dlmu__000
"""

import pandas as pd
from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number


Location1 = r'.\ori\train_features_2013-03-07.csv'
df = pd.read_csv(Location1)
Location2 = r'.\ori\train_salaries_2013-03-07.csv'
df2 = pd.read_csv(Location2)

df3 = pd.merge(df,df2)

df_ceo=df3[df3.jobType == 'CEO']
df_web_ceo = df3[ (df3.jobType == 'CEO') & (df3.industry== 'WEB') ]


df_web_ceo.to_csv('.\\data\\web_ceo.csv', index=False)


df_web_ceo = pd.read_csv('.\\data\\web_ceo.csv')
df_comp4 = df_web_ceo[ df_web_ceo.companyId == 'COMP4' ]
df_comp4.drop(["jobId", "companyId", "jobType","industry" ], axis=1,inplace=True)
degree_dummies = pd.get_dummies(df_comp4.degree, prefix='degree').iloc[:, 1:]
major_dummies = pd.get_dummies(df_comp4.major, prefix='major').iloc[:, 1:]
df_comp4_dummies = pd.concat([df_comp4, degree_dummies,major_dummies], axis=1)





