import pandas as pd
data = {
    "AOI": [50, 60, 55],
    "PM2.5": [35, 40, 45],
    "PM10": [80, 90, 85],
    "city": ["Delhi", "Jhharkhand", "Ranchi"]
}

df = pd.DataFrame(data)

df.rename(columns={
    "AOI": "AIR QUALITY INDEX",
    "PM2.5": "Particulate Matter 2.5",
    "PM10": "Particulate Matter 10",
    "city": "Location Code"
}, inplace=True)

print(df)

