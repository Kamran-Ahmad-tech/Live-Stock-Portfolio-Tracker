# 📈 Live Stock Portfolio Tracker

A professional, bulletproof Python command-line application that tracks your stock portfolio with live data fetching, financial analytics, and automatic Excel report exporting.

## 🚀 Features
- **Dynamic Portfolio Input:** Add any number of stock tickers and quantities via an interactive terminal loop.
- **Live Price Integration:** Fetches real-time market prices utilizing the `yfinance` library.
- **Fail-Safe Mechanism:** Robust exception handling to manage API rate limits or network issues without crashing.
- **Portfolio Analytics:** Automatically calculates current asset value, total portfolio worth, and weight allocation percentage using `pandas`.
- **Automated Reporting:** Generates and exports clean financial reports directly into an Excel (`.xlsx`) sheet.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kamran-Ahmad-tech/Live-Stock-Portfolio-Tracker.git](https://github.com/Kamran-Ahmad-tech/Live-Stock-Portfolio-Tracker.git)
   cd Live-Stock-Portfolio-Tracker

2.Install dependencies:
    pip install -r requirements.txt

3.Run the application:
    python tracker.py

4.📊 Technologies Used:
    ** Python 3

    ** Pandas (Data Manipulation & Analytics)

    ** yfinance (Yahoo Finance Data API)

    ** OpenPyXL (Excel File Generation)