import pandas as pd
import pandas_datareader as pdr
from pandas_datareader import data

import matplotlib

import numpy as np
import matplotlib.pyplot as plt



# read in the stock symbols. TODO: make path dynamic
df= pd.read_csv("/home/keenan/Stock-Experiment/companylist_nyse.csv")
df["Symbol"]

for Symbol in df["Symbol"]:
    stock = data.DataReader(Symbol, 'yahoo', '1980-01-01')
    #Create a new plot for each symbol
    plt.figure()
    plt.title(Symbol)
    stock["Adj Close"].plot(grid = True)

data = for Symbol in df["Symbol"]:
     DataReader(Symbol, 'yahoo', '1980-01-01')
