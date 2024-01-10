import pandas as pd
import matplotlib.pyplot as plt
import csv

total_price = 0
amount_of_stocks = 0
stocks_bought = 0
stocks_sold = 0

csv_input = input("Stock ticker: ")
csv_file = "csv/" + csv_input + ".csv"

data = pd.read_csv(csv_file, parse_dates=['Date'])
data = data.set_index('Date')

# Simple Moving Averages
data['SMA_50'] = data['Open'].rolling(window=100).mean()
data['SMA_200'] = data['Open'].rolling(window=25).mean()

# buy/sell signals
data['Signal'] = 0  # no signal
data['Signal'][data['SMA_50'] > data['SMA_200']] = 1  # Buy signal
data['Signal'][data['SMA_50'] < data['SMA_200']] = -1  # Sell signal

# DataFrame
signals_df = data[data['Signal'].isin([1, -1])][['Open', 'Signal']].copy()
signals_df['Date'] = signals_df.index

signals_df.to_csv('buy_sell_signals.csv', index=False)

for index, row in signals_df.iterrows():
    price = row['Open']
    signal = row['Signal']
    
    if signal == 1:  # Buy
        total_price += price
        amount_of_stocks += 1
        stocks_bought += 1
    elif signal == -1 and amount_of_stocks >=1:  # Sell
        total_price -= price
        amount_of_stocks -= 1
        stocks_sold += 1
    elif signal == -1: # Don't do anything
        i = 0

print("If bought by AI:")
print(f'Total Price: {total_price:.2f}')
print(f'Amount of Stocks: {amount_of_stocks}')
if amount_of_stocks > 0:
    averagePrice = total_price/amount_of_stocks
    print(f'Average Price: {averagePrice:.2f}')
# print("sold", stocks_sold)
# print("bought",  stocks_bought)

# plot
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

