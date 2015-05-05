# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:26:46 2015

@author: dlmu__000
"""
%cd C:\eclipse-workspace\dataproject
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

degree_dummies = pd.get_dummies(df3.degree, prefix='degree').iloc[:, 1:]
major_dummies = pd.get_dummies(df3.major, prefix='major').iloc[:, 1:]
jobtype_dummies = pd.get_dummies(df3.jobType, prefix='jobType').iloc[:, 1:]
industry_dummies = pd.get_dummies(df3.industry, prefix='industry').iloc[:, 1:]

df_dummies = pd.concat([df3, degree_dummies,major_dummies,jobtype_dummies,industry_dummies], axis=1)
df_dummies.to_csv('.\\data\\df_dummies.csv', index=False)

df_ceo=df3[df3.jobType == 'CEO']
df_web_ceo = df3[ (df3.jobType == 'CEO') & (df3.industry== 'WEB') ]
df_web_ceo.to_csv('.\\data\\web_ceo.csv', index=False)

df_web_ceo = pd.read_csv('.\\data\\web_ceo.csv')
df_comp4 = df_web_ceo[ df_web_ceo.companyId == 'COMP4' ]
df_comp4.drop(["jobId", "companyId", "jobType","industry" ], axis=1,inplace=True)
degree_dummies = pd.get_dummies(df_comp4.degree, prefix='degree').iloc[:, 1:]
major_dummies = pd.get_dummies(df_comp4.major, prefix='major').iloc[:, 1:]
df_comp4_dummies = pd.concat([df_comp4, degree_dummies,major_dummies], axis=1)

%cd C:\eclipse-workspace\dataproject
import pandas as pd
df_web_ceo = pd.read_csv('.\\data\\web_ceo.csv')
degree_dummies = pd.get_dummies(df_web_ceo.degree, prefix='degree').iloc[:, 1:]
major_dummies = pd.get_dummies(df_web_ceo.major, prefix='major').iloc[:, 1:]
df_web_ceo_dummies = pd.concat([df_web_ceo, degree_dummies,major_dummies], axis=1)
del df_web_ceo
feature_cols = [ u'yearsExperience', u'milesFromMetropolis', u'degree_DOCTORAL', u'degree_HIGH_SCHOOL', u'degree_MASTERS', u'degree_NONE', u'major_BUSINESS', u'major_CHEMISTRY', u'major_COMPSCI', u'major_ENGINEERING', u'major_LITERATURE', u'major_MATH', u'major_NONE', u'major_PHYSICS']


df_dummies= pd.read_csv('.\\data\\df_dummies.csv')
feature_cols = [ 'yearsExperience', 'milesFromMetropolis', 'degree_DOCTORAL', 'degree_HIGH_SCHOOL', 'degree_MASTERS', 
                 'degree_NONE', 'major_BUSINESS', 'major_CHEMISTRY', 'major_COMPSCI', 'major_ENGINEERING', 'major_LITERATURE', 'major_MATH', 'major_NONE', 'major_PHYSICS',
                 'jobType_CFO','jobType_CTO','jobType_JANITOR','jobType_JUNIOR','jobType_MANAGER','jobType_SENIOR','jobType_VICE_PRESIDENT',
                 'industry_EDUCATION','industry_FINANCE','industry_HEALTH','industry_OIL','industry_SERVICE','industry_WEB']




