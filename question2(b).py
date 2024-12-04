import pandas as pd
data = {
    "AOI": [50, 60, 55],
    "PM2.5": [35, 40, 45],
    "PM10": [80, 90, 85],
    "city": ["Delhi", "unknown", "Jhharkhand"]
}

df = pd.DataFrame(data)

df["city"] = df["city"].replace("unknown", "Not Available")

print("Updated Dataset:")
print(df)

output_file = "result.csv"
df.to_csv(output_file, index=False)

print(f"\nThe updated dataset has been saved to '{output_file}'.")
