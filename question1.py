impoprt pandas as pd
import numpy as np
p=import(https.csvAQI_Data.csv)

print("enter 8 rows of the dataset");
printf(api_dataset head(A));
printf(api_data.index);
printf()


min_pm10_per_city = data.groupby('City')['PM10'].min()
print(min_pm10_per_city)


first_8_columns = data.iloc[:, :8]
print(first_8_columns)


last_5_rows = data.tail(5)
print(last_5_rows)


data_info = data.info()
mean_aqi_per_city = data.groupby('City')['AQI'].mean()
print(mean_aqi_per_city)


min_pm10_per_city = data.groupby('City')['PM10'].min()
print(min_pm10_per_city)