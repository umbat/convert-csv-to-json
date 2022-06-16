import json
import csv

with open ("Location.csv", "r") as f:
    reader = csv.reader(f)
    data = {"location": []}
    for row in reader:
        data["location"].append({"code": row[0], "kecamatan": row[1], "kabupaten": row[2], "province": row[3], "lon": row[4], "lat": row[5]})
    print (data)

with open ("location.json", "w") as f:
    json.dump(data, f, indent=4)