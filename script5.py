import pandas as pd
import matplotlib.pyplot as plt
import csv

# Load the CSV data
data = pd.read_csv('MSFT.csv', parse_dates=['Date'])
data = data.set_index('Date')

# Calculate 50-day and 200-day Simple Moving Averages
data['SMA_50'] = data['Open'].rolling(window=50).mean()
data['SMA_200'] = data['Open'].rolling(window=200).mean()

# Generate buy/sell signals
data['Signal'] = 0  # 0 represents no signal
data['Signal'][data['SMA_50'] > data['SMA_200']] = 1  # Buy signal
data['Signal'][data['SMA_50'] < data['SMA_200']] = -1  # Sell signal

# Create a new DataFrame for buy/sell signals
signals_df = data[data['Signal'].isin([1, -1])][['Open', 'Signal']].copy()
signals_df['Date'] = signals_df.index

# Write the signals to a new CSV file
signals_df.to_csv('buy_sell_signals.csv', index=False)

# Initialize variables for tracking transactions
total_price = 0
amount_of_stocks = 0

# Iterate through buy/sell signals and update transaction variables
for index, row in signals_df.iterrows():
    price = row['Open']
    signal = row['Signal']
    
    if signal == 1:  # Buy signal
        total_price += price
        amount_of_stocks += 1
    elif signal == -1:  # Sell signal
        total_price -= price
        amount_of_stocks -= 1

# Print out the total price and amount of stocks
print(f'Total Price: {total_price:.2f}')
print(f'Amount of Stocks: {amount_of_stocks}')
averagePrice = total_price/amount_of_stocks
print(f'Average Price: {averagePrice:.2f}')

# Plot the prices and the trading signals
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Open'], label='Open Price')
plt.scatter(data.index[data['Signal'] == 1], data['Open'][data['Signal'] == 1], marker='^', color='g', label='Buy Signal')
plt.scatter(data.index[data['Signal'] == -1], data['Open'][data['Signal'] == -1], marker='v', color='r', label='Sell Signal')
plt.plot(data.index, data['SMA_50'], label='50-day SMA')
plt.plot(data.index, data['SMA_200'], label='200-day SMA')

plt.title('Moving Average Crossover Strategy (Daily Data)')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.legend()
plt.show()

