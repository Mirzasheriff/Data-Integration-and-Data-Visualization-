import requests
import pandas as pd
from datetime import datetime,UTC
import matplotlib.pyplot as plt

url = "https://open.er-api.com/v6/latest/inr"
response = requests.get(url)
data = response.json()

if data['result']!= 'success':
  raise Exception('API call failed')

time_stamp = data['time_last_update_unix']
base_currency = data['base_code']
rates = data['rates']

major_currencies = ['USD','EUR','GBP','JPY','AUD']
inr_per_currency = {}

for currency in major_currencies:
  if(currency in rates and rates[currency]!= 0):
    inr_per_currency[currency] =  round(1/rates[currency],2)
    
updated_at = datetime.fromtimestamp(time_stamp,UTC).strftime('%y-%m-%d %H:%M:%S')

df = pd.DataFrame(list(inr_per_currency.items()),columns = ['Currency','Inr_Equivalent'])

df['Base_currency']= base_currency

df['Updated_at'] = updated_at
