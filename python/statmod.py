# -*- coding: utf-8 -*-
"""
Created on Thu May 07 23:24:29 2015

@author: dlmu__000
"""
import statsmodels.formula.api as smf
mod = smf.ols(formula='salary ~ C(jobType)+C(degree)+C(major)+C(industry)+yearsExperience+milesFromMetropolis', data=df3)
res = mod.fit()
print res.summary()

from statsmodels.stats.anova import anova_lm

one_lm = ols('salary ~ C(jobType)', data=df3).fit()
one_lm = ols('salary ~ C(companyId)', data=df3).fit()
table9 = anova_lm(one_lm)
print(table9)

two_lm = ols('salary ~ C(industry)*C(major)', data=df3).fit()

table10 = anova_lm(two_lm)
print(table10)


