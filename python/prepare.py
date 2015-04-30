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
