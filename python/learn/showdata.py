# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:54:21 2015

@author: dlmu__000
"""

df_comp4 = df_web_ceo[ df_web_ceo.companyId == 'COMP4' ]
df_comp4.head()
df_clean = df_comp4.drop(['jobType', 'jobId','companyId'],axis=1)
