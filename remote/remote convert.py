import pandas as pd
import json
import csv

with pd.read_csv('https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/CSV/kecamatanforecast-banten.csv') as f:
    reader = csv.reader(f)
    data = {"forecast": []}
    for row in reader:
        data["forecast"].append({"code": row[0], "time": row[1], "Tmin": row[2], "Tmax": row[3], "Hmin": row[4], "Hmax": row[5], "humidity": row[6], "temperature": row[7], "weather": row[8], "Wdir": row[9], "Wspeed": row[10]})
    print (data)

with open ("banten.json", "w") as f:
    json.dump(data, f, indent=4)