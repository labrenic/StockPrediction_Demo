import requests.api
import numpy as np
import pandas as pd


ticker = 'TSLA'
start_date = '2010-07-10'
end_date = '2020-12-30'

r = requests.get('https://pselookup.vrymel.com/api/stocks/JFC/history/1999-02-04/2020-07-30')

data = r.json()

print(data['history'])
