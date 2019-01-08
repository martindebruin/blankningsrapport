import requests
import datetime
import pandas as pd
import xlrd

todayString = datetime.date.today().strftime('%Y-%m-%d')
timeString = datetime.datetime.now().time().strftime('%H:%M')

fname = "aktuella_positioner_"+todayString+".xlsx" # Automatic reference to today's file
#fname = "aktuella_positioner_2019-01-07_old.xlsx" # when working with old file

url = 'https://www.fi.se/contentassets/71a61417bb4c49c0a4a3a2582ea8af6c/'+fname
r = requests.get(url)
open(fname , 'wb').write(r.content)

print fname+" downloaded: "+todayString+" "+timeString

watchlist = ['SE0006887063','SE0008374250'] # Which stocks do we want

stocks = pd.read_excel(fname)
stocks = stocks.iloc[5:,] # strip top 5 rows to get just interesting stuffs
stocks.columns = ['holder','issuer','isin','size','date'] # rename the columns to get them more workable
myReport = stocks.loc[stocks['isin'].isin(watchlist)] # Generate report of just the stocks on the watchlist
print myReport

