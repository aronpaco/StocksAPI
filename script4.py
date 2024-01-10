import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('MSFT_2014_2018.csv', parse_dates=['Date'])
data = data.set_index('Date')

# Calculate 50-day and 200-day Simple Moving Averages
data['SMA_50'] = data['Open'].rolling(window=50).mean()
data['SMA_200'] = data['Open'].rolling(window=200).mean()

# Generate buy/sell signals
data['Signal'] = 0  # 0 represents no signal
data['Signal'][data['SMA_50'] > data['SMA_200']] = 1  # Buy signal
data['Signal'][data['SMA_50'] < data['SMA_200']] = -1  # Sell signal

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
