import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV file
file_path = 'MSFT_2014_2018.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Calculate short-term (e.g., 50 days) and long-term (e.g., 200 days) moving averages
df['Short_MA'] = df['Close'].rolling(window=50).mean()
df['Long_MA'] = df['Close'].rolling(window=200).mean()

# Create a column for the trading signals
df['Signal'] = 0.0
df['Signal'][50:] = np.where(df['Short_MA'][50:] > df['Long_MA'][50:], 1.0, 0.0)

# Create a column for the positions
df['Position'] = df['Signal'].diff()

# Print out prices when buying or selling
buy_signals = df[df['Position'] == 1]
sell_signals = df[df['Position'] == -1]

for index, row in buy_signals.iterrows():
    print(f"Buy: {index.date()} - Price: {row['Close']}")

for index, row in sell_signals.iterrows():
    print(f"Sell: {index.date()} - Price: {row['Close']}")

# Plotting the Closing Prices with Buy/Sell signals
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price', linewidth=2)

# Plot Buy signals
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='g', label='Buy Signal')

# Plot Sell signals
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='r', label='Sell Signal')

plt.title('Stock Price with Buy/Sell Signals')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()
