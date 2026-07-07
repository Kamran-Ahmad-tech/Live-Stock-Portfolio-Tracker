import yfinance as yf
import pandas as pd
class PortfolioTracker:
    def __init__(self):
        # Jab bhi hum naya tracker banayenge, yeh khali dictionary pehle ready hogi
        # Is mein data aise save hoga -> {'AAPL': 5, 'MSFT': 10}
        self.portfolio = {}

    def export_to_excel(self,df):
        filename = "Stock_Portfolio_Report.xlsx"
        df.to_excel(filename,index=False)
        print(f" ✅ Report saved successfully as {filename}")

    def get_live_prices(self):
        price={}
        for ticker in self.portfolio:
            clean_ticker=ticker.strip().upper()
            stock_data=yf.Ticker(clean_ticker)
            try:
                hist = stock_data.history(period="1d")
                live_price = hist['Close'].iloc[-1]
                price[clean_ticker] = live_price
            except Exception:
                # Agar phir bhi koi masla ho tu None bhej do
                price[clean_ticker] = None
           
        return price
    
    def calculate_portfolio_analytics(self):
        prices=self.get_live_prices()
        data_list=[]
        for ticker, qty in self.portfolio.items():
            live_p=prices[ticker]
            if live_p is None:
                print(f"⚠️ Warning: Could not fetch price for {ticker}. Skipping...")
                continue
            current_value=qty*live_p
            data_dict={
                "Ticker": ticker,
                "Quantity": qty,
                "Live Price": live_p,
                "Current value":current_value
                }
            data_list.append(data_dict)
        df=pd.DataFrame(data_list)
        df["Total_value"]=df["Current value"].sum()
        df["Allocation %"]=(df["Current value"]/df["Total_value"])*100
        return df
    
    def add_asset(self):
        """User se dynamic tareeqe se stocks aur unki quantity input lene ka function"""
        print("--- 📈 Welcome to Live Stock Portfolio Input System ---")
        print("(Type 'exit' when you are done adding stocks)\n")
        
        while True:
            # 1. User se stock ka ticker/symbol lena (jaise AAPL, GOOGL)
            ticker = input("Enter Stock Ticker (e.g., AAPL, MSFT, TSLA, NVDA , GOOG): ").strip().upper()
            
            # Agar user 'EXIT' likhe tu loop khatam ho jaye
            if ticker == 'EXIT':
                break
            
            # Ticker khali nahi hona chahiye
            if not ticker:
                print("❌ Invalid input! Ticker cannot be empty.")
                continue

            # 2. User se shares ki quantity lena
            try:
                quantity = int(input(f"Enter quantity for {ticker}: "))
                if quantity <= 0:
                    print("❌ Quantity must be greater than 0!")
                    continue
            except ValueError:
                # Agar user number ki jagah abc likh de tu crash na ho (Exception Handling)
                print("❌ Invalid quantity! Please enter a valid whole number.")
                continue

            # 3. Agar stock pehle se majood hai tu quantity plus kar do, warna naya add karo
            if ticker in self.portfolio:
                self.portfolio[ticker] += quantity
            else:
                self.portfolio[ticker] = quantity
                
            print(f"✅ Added {quantity} shares of {ticker} to your portfolio.\n")

    def display_portfolio(self):
        """Jo data input hua hai usay screen par show karne ke liye"""
        print("\n--- 📋 Current Portfolio Summary ---")
        if not self.portfolio:
            print("Your portfolio is currently empty.")
        for ticker, qty in self.portfolio.items():
            print(f"Stock: {ticker} | Quantity: {qty}")

# --- Testing Our First Layer ---
if __name__ == "__main__":
    # 1. Object banaya
    my_tracker = PortfolioTracker()
    
    # 2. User se stocks input liye (jaise AAPL, MSFT, TSLA)
    my_tracker.add_asset()
    
    # 3. Analytics wala function chalaya aur table ko ek variable mein liya
    portfolio_table = my_tracker.calculate_portfolio_analytics()
    
    # 4. Table ko screen par display karwaya
    print("\n--- 📊 Final Live Portfolio Analytics Table ---")
    print(portfolio_table)
    my_tracker.export_to_excel(portfolio_table)