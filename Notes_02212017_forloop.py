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

import csv
df = pd.read_csv('test.csv')


import numpy as np

array_s = np.array(s)

from io import StringIO

import pandas as pd
import requests

url="https://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s=CMCSA"
url_ref ="https://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s="
headers = {'Date': 'Open': 'High': 'Low': 'Close': 'Volume': 'Adj Close'}
headers = {'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'}



#######Parse String
companylist_nasdaq = pd.read_csv('companylist_nasdaq.csv')
 url.split('CMCSA')
companylist_nasdaq['Symbol']

symbol_list = companylist_nasdaq['Symbol']
total_rows = len(symbol_list)
symbol =  "".join(symbol_list[[2]].astype('str').tail(1).tolist())
df.loc[[2]]

url_source = url_ref + symbol
s= requests.get(url_source)
from io import StringIO
c=pd.read_csv(StringIO(s.text))

Adj_Close = c['Adj Close']
max_close = round(max(Adj_Close),2)
last_entry_len = len(Adj_Close)-1
last_entry = round(Adj_Close[[last_entry_len]],2)
delta = round((max_close - last_entry)/max_close,3)

result_array = np.array([symbol, max_close, last_entry,delta])

 newrow = [1,2,3]
  result = numpy.vstack([result, result_array])
  
  pd.DataFrame(my_array, columns = ["symbol", "max_close", "last_entry", "delta"])
last_entry.tolist()

test2 = last_entry.astype(float)

pd.DataFrame([result_array, result_array], columns=list('ABCD'))
