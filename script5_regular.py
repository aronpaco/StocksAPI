import csv

# Initialize variables
total_price = 0
amount_of_stocks = 0

# Read the CSV file
csv_file_path = "MSFT.csv"  # Replace with the actual path to your CSV file

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Iterate through each row and "buy" the stock
    for row in reader:
        date, open_price, high, low, close, adj_close, volume = row
        # Assuming you buy at the opening price, you can use 'open_price' for the transaction
        stock_price = float(open_price)
        
        # Buy the stock
        total_price += stock_price
        amount_of_stocks += 1

# Print out the total price and amount of stocks
print(f'Total Price: {total_price:.2f}')
print(f'Amount of Stocks: {amount_of_stocks}')
averagePrice = total_price/amount_of_stocks
print(f'Average Price: {averagePrice:.2f}')