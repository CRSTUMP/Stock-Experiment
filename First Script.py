# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
pd
import requests
import os

cwd = cwd = os.getcwd()
cwd
os.chdir("C:\\Users\\Chris\\Documents\\Python\\Stock-Experiment")



url="http://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2025&g=d&a=7&b=19&c=2004 &ignore=.csv&s=cmcsa"
s= requests.get(url).content

dfr = pd.DataFrame(data = s, index = index)
c=pd.read_csv(s)

import csv

with open('test.csv', 'w') as csvfile:
    ##fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    
 import mangler  