import csv

total_price = 0
amount_of_stocks = 0

csv_file = "csv/" + input("Stock ticker: ") + ".csv"

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        date, open_price, high, low, close, adj_close, volume = row
        stock_price = float(open_price)
        
        total_price += stock_price
        amount_of_stocks += 1

print("If bought daily:")
print(f'Total Price: {total_price:.2f}')
print(f'Amount of Stocks: {amount_of_stocks}')
averagePrice = total_price/amount_of_stocks
print(f'Average Price: {averagePrice:.2f}')