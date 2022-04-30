# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:58:31 2022

@author: mason
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:22:12 2022

@author: mason
"""




import cvxpy as cp
from math import log



def lp_depol(d,q,channel):

    r1 = cp.Variable(nonneg=True)
    r2 = cp.Variable(nonneg=True)
    r3 = cp.Variable(nonneg=True)
    r4 = cp.Variable(nonneg=True)

    mu = cp.Variable()

    constraints = [r1 >= r2, r3 >= r4]
    constraints += [(d*(r1+r3) + r2 + r4) <= mu]
    constraints += [(r1 - r3 - q/d + d*(r2-r4) - d*(1-q)) >= 0]
    constraints += [(r1 - r3 - q/d) >= 0]

    prob = cp.Problem(cp.Minimize(mu), constraints)

    prob.solve()
    return log(prob.value,2)


print(lp_depol(50,.0272,depol))

