
import pandas as pd
import pandas_datareader as pdr
from pandas_datareader import data
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import requests
import os
%matplotlib inline
from matplotlib.backends.backend_pdf import PdfPages
import csv
import numpy as np

os.chdir("C:\\Users\\Chris\\Documents\\Python\\Stock-Experiment")
cwd = cwd = os.getcwd()



url="https://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s=CMCSA"
url_ref ="https://ichart.finance.yahoo.com/table.csv?d=6&e=1&f=2009&g=d&a=7&b=19&c=2004&ignore=.csv&s="

companylist_nasdaq = pd.read_csv("companylist_nasdaq.csv")

#companylist_nasdaq = pd.read_csv("companylist_nasdaq_1.csv")
####Build a loop

f = plt.figure()

from io import StringIO
for Symbol in companylist_nasdaq["Symbol"]:
	try:
		stock_url = url_ref + Symbol
		s= requests.get(stock_url)
		from io import StringIO
		stock=pd.read_csv(StringIO(s.text))
		print( Symbol, max(stock['Adj Close']))
		
		f = plt.figure()
		plt.title(Symbol)
		stock["Adj Close"].plot(grid = True)
		plt.show()
		#pdf_pages.savefig(fig)
	
		f.savefig(Symbol + ".pdf", bbox_inches='tight')
	
		
	except:
		pass

print("Done Processing")




