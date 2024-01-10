import pandas as pd
import datetime
import calendar

# Replace 'your_file.csv' with the actual file path
file_path = 'MSFT_2014_2018.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
# print(df)

def check_weekday_or_weekend(date):
    try:
        # Convert the input date string to a datetime object
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')
         
        # Use isoweekday() to get the weekday (Monday is 1 and Sunday is 7)
        day_of_week = (given_date.weekday() + 1) % 7  # Convert Sunday from 6 to 0
         
        
         
        # Print the result
        print(f"The day of the week for {given_date.strftime('%Y-%m-%d')} is {day_of_week}")
         
    except ValueError as e:
        print(f"Error: {e}")
 
# Example usage
date = '2024-01-11'
check_weekday_or_weekend(date)