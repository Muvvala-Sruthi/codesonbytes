#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas


# In[6]:


import pandas as pd
import requests
from datetime import datetime
LATITUDE = 18.990713
LONGITUDE = 73.116844
api_url ="https://api.openweathermap.org/data/2.5/forecast?lat=15.90&lon=80.46&cnt=200&appid=98e027721603ca32cead5457312b406a"
response = requests.get(api_url)
data = response.json()
forecast_data = []
for entry in data['list']:
    timestamp = entry['dt']
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    temperature = entry['main']['temp']
    description = entry['weather'][0]['description']
    forecast_data.append({'Date': date, 'Temperature': temperature, 'Description': description})
df = pd.DataFrame(forecast_data)
df.to_csv('weather_forecast.csv', index=False)
print("Dataset has been created and saved as 'weather_forecast.csv'")


# In[ ]:




