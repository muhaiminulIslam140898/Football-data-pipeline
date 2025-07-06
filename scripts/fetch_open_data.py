# scripts/fetch_open_data.py

import pandas as pd
import requests
import os

# ✅ Create the 'data' folder if not exists
os.makedirs('data', exist_ok=True)

# ✅ Public dataset (Premier League 2022–23)
url = "https://raw.githubusercontent.com/openfootball/football.json/master/2022-23/en.1.json"

response = requests.get(url)
data = response.json()

# ✅ Extract matches
matches = data['matches']

# ✅ Parse useful fields
records = []
for m in matches:
    record = {
        'date': m['date'],
        'home_team': m['team1'],
        'away_team': m['team2'],
        'home_score': m['score']['ft'][0],
        'away_score': m['score']['ft'][1],
        'round': m['round']
    }
    records.append(record)

# ✅ Save to CSV
df = pd.DataFrame(records)
df.to_csv('./data/raw_data.csv', index=False)
print(f"✅ Saved {len(df)} records to data/raw_data.csv")
