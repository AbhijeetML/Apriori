# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:12:19 2020

@author: Abhijeet
"""

import pandas as pd
import numpy as np
from apyori import apriori

df=pd.read_csv('C:/Users/Abhijeet/Downloads/store_data.csv',header=None)


data=[]
for i in range(0,7501):
    data.append([str(df.values[i,j]) for j in range(0,20)])
    
association=apriori(data,min_support=.0045,min_confidence=.2,min_lift=3,min_length=2)
new_association=list(association)


for item in new_association:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[1] + " -> " + items[0])

   
    print("Support: " + str(item[1]))

    

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

