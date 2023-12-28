import pandas as pd

# Replace 'your_file.csv' with the actual file path
file_path = 'MSFT_2014_2018.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df)
