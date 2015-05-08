# -*- coding: utf-8 -*-
"""
Created on Thu May 07 18:03:58 2015

@author: dlmu__000
"""
%cd C:\eclipse-workspace\dataproject\python
import pandas as pd
from pandas import DataFrame, read_csv

Location1 = r'..\ori\train_features_2013-03-07.csv'
df = pd.read_csv(Location1)
Location2 = r'..\ori\train_salaries_2013-03-07.csv'
df2 = pd.read_csv(Location2)
df3 = pd.merge(df,df2)

df["industry_major"]=df["industry"]+"_"+df["major"]

degree_dummies = pd.get_dummies(df.degree, prefix='degree').iloc[:, 1:]
major_dummies = pd.get_dummies(df.major, prefix='major').iloc[:, 1:]
jobtype_dummies = pd.get_dummies(df.jobType, prefix='jobType').iloc[:, 1:]
industry_dummies = pd.get_dummies(df.industry, prefix='industry').iloc[:, 1:]
industry_major_dummies = pd.get_dummies(df.industry_major, prefix='indumajo').iloc[:, 1:]

df_new = pd.concat([df, degree_dummies,major_dummies,jobtype_dummies,industry_dummies,industry_major_dummies], axis=1)
df_new.to_csv('..\\data\\df_new.csv', index=False)



feature_cols_all =[  u'yearsExperience', u'milesFromMetropolis', 
                     u'degree_DOCTORAL', u'degree_HIGH_SCHOOL', u'degree_MASTERS', u'degree_NONE', 
                     u'major_BUSINESS', u'major_CHEMISTRY', u'major_COMPSCI', u'major_ENGINEERING', u'major_LITERATURE', u'major_MATH', u'major_NONE', u'major_PHYSICS', 
                     u'jobType_CFO', u'jobType_CTO', u'jobType_JANITOR', u'jobType_JUNIOR', u'jobType_MANAGER', u'jobType_SENIOR', u'jobType_VICE_PRESIDENT', 
                     u'industry_EDUCATION', u'industry_FINANCE', u'industry_HEALTH', u'industry_OIL', u'industry_SERVICE', u'industry_WEB', 
                     u'indumajo_AUTO_BUSINESS', u'indumajo_AUTO_CHEMISTRY', u'indumajo_AUTO_COMPSCI', u'indumajo_AUTO_ENGINEERING', u'indumajo_AUTO_LITERATURE', u'indumajo_AUTO_MATH', u'indumajo_AUTO_NONE', u'indumajo_AUTO_PHYSICS', u'indumajo_EDUCATION_BIOLOGY', u'indumajo_EDUCATION_BUSINESS', u'indumajo_EDUCATION_CHEMISTRY', u'indumajo_EDUCATION_COMPSCI', u'indumajo_EDUCATION_ENGINEERING', u'indumajo_EDUCATION_LITERATURE', u'indumajo_EDUCATION_MATH', u'indumajo_EDUCATION_NONE', u'indumajo_EDUCATION_PHYSICS', u'indumajo_FINANCE_BIOLOGY', u'indumajo_FINANCE_BUSINESS', u'indumajo_FINANCE_CHEMISTRY', u'indumajo_FINANCE_COMPSCI', u'indumajo_FINANCE_ENGINEERING', u'indumajo_FINANCE_LITERATURE', u'indumajo_FINANCE_MATH', u'indumajo_FINANCE_NONE', u'indumajo_FINANCE_PHYSICS', u'indumajo_HEALTH_BIOLOGY', u'indumajo_HEALTH_BUSINESS', u'indumajo_HEALTH_CHEMISTRY', u'indumajo_HEALTH_COMPSCI', u'indumajo_HEALTH_ENGINEERING', u'indumajo_HEALTH_LITERATURE', u'indumajo_HEALTH_MATH', u'indumajo_HEALTH_NONE', u'indumajo_HEALTH_PHYSICS', u'indumajo_OIL_BIOLOGY', u'indumajo_OIL_BUSINESS', u'indumajo_OIL_CHEMISTRY', u'indumajo_OIL_COMPSCI', u'indumajo_OIL_ENGINEERING', u'indumajo_OIL_LITERATURE', u'indumajo_OIL_MATH', u'indumajo_OIL_NONE', u'indumajo_OIL_PHYSICS', u'indumajo_SERVICE_BIOLOGY', u'indumajo_SERVICE_BUSINESS', u'indumajo_SERVICE_CHEMISTRY', u'indumajo_SERVICE_COMPSCI', u'indumajo_SERVICE_ENGINEERING', u'indumajo_SERVICE_LITERATURE', u'indumajo_SERVICE_MATH', u'indumajo_SERVICE_NONE', u'indumajo_SERVICE_PHYSICS', u'indumajo_WEB_BIOLOGY', u'indumajo_WEB_BUSINESS', u'indumajo_WEB_CHEMISTRY', u'indumajo_WEB_COMPSCI', u'indumajo_WEB_ENGINEERING', u'indumajo_WEB_LITERATURE', u'indumajo_WEB_MATH', u'indumajo_WEB_NONE', u'indumajo_WEB_PHYSICS']
                     

feature_cols_less =[  u'yearsExperience', u'milesFromMetropolis', 
                     u'degree_DOCTORAL', u'degree_HIGH_SCHOOL', u'degree_MASTERS', u'degree_NONE', 
                     u'jobType_CFO', u'jobType_CTO', u'jobType_JANITOR', u'jobType_JUNIOR', u'jobType_MANAGER', u'jobType_SENIOR', u'jobType_VICE_PRESIDENT', 
                     u'indumajo_AUTO_BUSINESS', u'indumajo_AUTO_CHEMISTRY', u'indumajo_AUTO_COMPSCI', u'indumajo_AUTO_ENGINEERING', u'indumajo_AUTO_LITERATURE', u'indumajo_AUTO_MATH', u'indumajo_AUTO_NONE', u'indumajo_AUTO_PHYSICS', u'indumajo_EDUCATION_BIOLOGY', u'indumajo_EDUCATION_BUSINESS', u'indumajo_EDUCATION_CHEMISTRY', u'indumajo_EDUCATION_COMPSCI', u'indumajo_EDUCATION_ENGINEERING', u'indumajo_EDUCATION_LITERATURE', u'indumajo_EDUCATION_MATH', u'indumajo_EDUCATION_NONE', u'indumajo_EDUCATION_PHYSICS', u'indumajo_FINANCE_BIOLOGY', u'indumajo_FINANCE_BUSINESS', u'indumajo_FINANCE_CHEMISTRY', u'indumajo_FINANCE_COMPSCI', u'indumajo_FINANCE_ENGINEERING', u'indumajo_FINANCE_LITERATURE', u'indumajo_FINANCE_MATH', u'indumajo_FINANCE_NONE', u'indumajo_FINANCE_PHYSICS', u'indumajo_HEALTH_BIOLOGY', u'indumajo_HEALTH_BUSINESS', u'indumajo_HEALTH_CHEMISTRY', u'indumajo_HEALTH_COMPSCI', u'indumajo_HEALTH_ENGINEERING', u'indumajo_HEALTH_LITERATURE', u'indumajo_HEALTH_MATH', u'indumajo_HEALTH_NONE', u'indumajo_HEALTH_PHYSICS', u'indumajo_OIL_BIOLOGY', u'indumajo_OIL_BUSINESS', u'indumajo_OIL_CHEMISTRY', u'indumajo_OIL_COMPSCI', u'indumajo_OIL_ENGINEERING', u'indumajo_OIL_LITERATURE', u'indumajo_OIL_MATH', u'indumajo_OIL_NONE', u'indumajo_OIL_PHYSICS', u'indumajo_SERVICE_BIOLOGY', u'indumajo_SERVICE_BUSINESS', u'indumajo_SERVICE_CHEMISTRY', u'indumajo_SERVICE_COMPSCI', u'indumajo_SERVICE_ENGINEERING', u'indumajo_SERVICE_LITERATURE', u'indumajo_SERVICE_MATH', u'indumajo_SERVICE_NONE', u'indumajo_SERVICE_PHYSICS', u'indumajo_WEB_BIOLOGY', u'indumajo_WEB_BUSINESS', u'indumajo_WEB_CHEMISTRY', u'indumajo_WEB_COMPSCI', u'indumajo_WEB_ENGINEERING', u'indumajo_WEB_LITERATURE', u'indumajo_WEB_MATH', u'indumajo_WEB_NONE', u'indumajo_WEB_PHYSICS']   

df_new = pd.read_csv('..\\data\\df_new.csv')      
from functions import *                
from sklearn import linear_model

# instantiate, fit

model = linear_model.Lasso(alpha = 1)
result = split_evaluate(model, df_new, feature_cols_all)

model = linear_model.LinearRegression()
result = split_evaluate(model, df_new, feature_cols_less)  
result                     