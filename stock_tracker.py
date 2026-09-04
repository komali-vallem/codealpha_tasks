# Stock Portfolio Tracker

# Manually defined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print("Stock price:", stock_prices[stock])
    print("Investment:", investment)

print("\n===== Portfolio Summary =====")
print("Total Investment:", total_investment)
print("Thank you for using Stock Portfolio Tracker!")