import requests.api
import numpy as np
import pandas as pd
from pandas import json_normalize


ticker = 'JFC'
start_date = '2010-07-10'
end_date = '2020-12-30'

r = requests.get(f'https://pselookup.vrymel.com/api/stocks/{ticker}/history/{start_date}/{end_date}')

data = r.json()

df = json_normalize(data, 'history')

print(df.head())
