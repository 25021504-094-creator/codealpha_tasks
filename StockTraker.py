import csv
import os
from datetime import datetime
STOCK_PRICES={
    "AAPL":280,
    "MSFT":420,
    "NVDA":900,
    "GOOGL":385,
    "AMZN":180,
    "TSLA":200,
    "JPM":190,
    "BRK.B":420,
    "XOM":120,
    "NFLX":480
}
#print(stock_prices)
def display_stock():
    print("\n📊 Available Stocks:")
    print("-" * 40)
    for symbol,price in STOCK_PRICES.items():
        print(f"{symbol:>8}-${price:.2f}")
    print("-" * 40)
def get_user_input():
    stocks = []
    
    while True:
        print("\n" + "="*50)
        stock_name = input("Enter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock_name == 'DONE':
            break
        
        if stock_name not in STOCK_PRICES:
            print(f"❌ '{stock_name}' not found in our database!")
            print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
            continue
        
        try:
            quantity = float(input(f"Enter quantity of {stock_name}: "))
            if quantity <= 0:
                print("❌ Quantity must be positive!")
                continue
            
            stocks.append({
                'Symbol': stock_name,
                'Quantity': quantity,
                'price': STOCK_PRICES[stock_name]
            })
            print(f"✅ Added {quantity} shares of {stock_name}")
            
        except ValueError:
            print("❌ Please enter a valid number for quantity!")
    
    return stocks

def calculate_totalvalue(stocks):
    total=0
    for stock in stocks:
        stock_value=stock["Quantity"]*stock["price"]
        total+=stock_value
    return total
def display_stockssummary(stocks,total_value):
    print("\n" + "__"*60)
    print("📈 STOCKS SUMMARY")
    print("__"*60)
    print(f"{'Symbol':<10} {'Quantity':<12} {'Price':<12} {'Total Value':<15}")
    print("__"*60)
    for stock in stocks:
        stock_value=stock["Quantity"]*stock["price"]
        print(f"{stock["Symbol"]:<10}{stock["Quantity"]:<12.2f}{stock["price"]:<11.2f}{stock_value:14.2f}")
    print("__"*60)
    print(f"\n💰 TOTAL INVESTMENT: ${total_value:,.2f}")
    print("__"*60)
def save_to_txt(stock,total_value):
    try:
        filename=f"Stocks{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(filename,"w") as file:
            file.write("\n" + "__"*60)
            file.write(" STOCKS RECORD\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("__"*60)
            file.write(f"{'Symbol':<10} {'Quantity':<12} {'Price':<12} {'Total Value':<15}")
            file.write("__"*60)
            for stock in stock:
                stock_value=stock["Quantity"]*stock["price"]
                file.write(f"{stock["Symbol"]:<10}{stock["Quantity"]:<12.2f}{stock["price"]:<11.2f}{stock_value:14.2f}")
            file.write("__"*60)
            file.write(f"\n TOTAL INVESTMENT: ${total_value:,.2f}")
            file.write("__"*60)
        print(f"\n✅ Stocks saved to: {filename}")
        return True
        
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        return False
def save_to_csv(stock,total_value):
    try:
        filename = f"Stocks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"   
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['Symbol', 'Quantity', 'Price per Share', 'Total Value'])
            
            # Write stock data
            for stock in stock:
                stock_value = stock['Quantity'] * stock['price']
                writer.writerow([
                    stock['Symbol'],
                    stock['Quantity'],
                    f"${stock['price']:.2f}",
                    f"${stock_value:.2f}"
                ])
            writer.writerow([])
            writer.writerow(['Total Investment', f"${total_value:,.2f}"])
            writer.writerow(['Number of Holdings', len(stock)])
            writer.writerow(['Generated', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        
        print(f"\n✅ Stocks saved to: {filename}")
        return True
        
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        return False
def main():
    """Main program function"""
    print("\n" + "__"*50)
    print("📊 STOCK  TRACKER")
    print("__"*50)
    display_stock()
    stocks = get_user_input()
    
    if not stocks:
        print("\n❌ No stocks added. Exiting program.")
        return
    total_investment = calculate_totalvalue(stocks)
    display_stockssummary(stocks,total_investment)
    print("\n💾 Would you like to save this portfolio?")
    print("1. Save as TXT file")
    print("2. Save as CSV file")
    print("3. Skip saving")
    choice = input("Enter your choice (1/2/3): ").strip()   
    if choice == '1':
        #name=input("Enter file name: ").strip()
        save_to_txt(stocks, total_investment)
    elif choice == '2':
        #name=input("Enter file name: ").strip()
        save_to_csv(stocks, total_investment)
    elif choice == '3':
        print("\n✅ Stocks data not saved.")
    else:
        print("\n❌ Invalid choice. Data not saved.")    
    print("\n✨ Thank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
    

        
