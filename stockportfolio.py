# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))
    portfolio[stock_name] = quantity

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock} x {quantity} = ${investment}")

print(f"\nTotal Investment Value = ${total_investment}")

# Save result to a text file
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("-----------------------\n")

        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            file.write(f"{stock} x {quantity} = ${investment}\n")

        file.write(f"\nTotal Investment Value = ${total_investment}")

    print("Report saved as portfolio_report.txt")

print("\nThank you for using Stock Portfolio Tracker!")