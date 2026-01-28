import pandas as pd
import os
import dvc

data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }

df = pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir, exist_ok=True)

csv_path = os.path.join(data_dir, 'people.csv')

df.to_csv(csv_path, index=False)

print(f"DataFrame saved to {csv_path}")