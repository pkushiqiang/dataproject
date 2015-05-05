# -*- coding: utf-8 -*-
"""
Created on Sat May 02 11:56:40 2015

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


def createInduData():
    industries=["OIL","WEB","AUTO", "SERVICE", "EDUCATION", "FINANCE","HEALTH"]
         
    for indu in industries:
        df_in = df_web = df3[  df3.industry == indu ]
        degree_dummies = pd.get_dummies(df_in.degree, prefix='degree').iloc[:, 1:]
        major_dummies = pd.get_dummies(df_in.major, prefix='major').iloc[:, 1:]
        jobtype_dummies = pd.get_dummies(df_in.jobType, prefix='jobType').iloc[:, 1:]
        df_dummies = pd.concat([df_in, degree_dummies,major_dummies, jobtype_dummies], axis=1)
        df_dummies.to_csv('.\\data\\df_'+ indu.lower() + '_dummies.csv', index=False)


df_web = df3[  df3.industry== 'WEB' ]
degree_dummies = pd.get_dummies(df_web.degree, prefix='degree').iloc[:, 1:]
major_dummies = pd.get_dummies(df_web.major, prefix='major').iloc[:, 1:]
jobtype_dummies = pd.get_dummies(df_web.jobType, prefix='jobType').iloc[:, 1:]

df_web_dummies = pd.concat([df_web, degree_dummies,major_dummies, jobtype_dummies], axis=1)
df_web_dummies.to_csv('.\\data\\df_web_dummies.csv', index=False)
del df, df2, df3
del df_web, degree_dummies, major_dummies, jobtype_dummies

df_web_dummies= pd.read_csv('.\\data\\df_web_dummies.csv')
feature_cols = [ 'yearsExperience', 'milesFromMetropolis', 'degree_DOCTORAL', 'degree_HIGH_SCHOOL', 'degree_MASTERS', 
                 'degree_NONE', 'major_BUSINESS', 'major_CHEMISTRY', 'major_COMPSCI', 'major_ENGINEERING', 'major_LITERATURE', 'major_MATH', 'major_NONE', 'major_PHYSICS',
                 'jobType_CFO','jobType_CTO','jobType_JANITOR','jobType_JUNIOR','jobType_MANAGER','jobType_SENIOR','jobType_VICE_PRESIDENT']
                 