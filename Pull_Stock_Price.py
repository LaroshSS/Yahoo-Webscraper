import requests
from bs4 import BeautifulSoup

def get_stock_data(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'

    # Send a request to the webpage
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the stock price in the HTML (class name may change)
        price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
        price = price_tag.text if price_tag else "Could not find stock price"

        # Find the stock name
        name_tag = soup.find('h1', {'class': 'yf-vfa1ac'})
        stock_name = name_tag.text if name_tag else "Could not find stock name"

        # Find the previous close price
        prev_close_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'})
        prev_close = prev_close_tag.text if prev_close_tag else "Could not find previous close price"

        # Find the open price
        open_tag = soup.find('fin-streamer', {'active-data-field': 'regularMarketOpen'})
        open_price = open_tag.text if open_tag else "Could not find open price"

        # Find the day's range
        days_range_tag = soup.find('fin-streamer', {'data-field': 'regularMarketDayRange'})
        days_range = days_range_tag.text if days_range_tag else "Could not find day's range"

        # Find the 52 week range
        week_range_tag = soup.find('fin-streamer', {'data-field': 'fiftyTwoWeekRange'})
        week_range = week_range_tag.text if week_range_tag else "Could not find 52 week range"

        # Find the volume
        volume_tag = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'})
        volume = volume_tag.text if volume_tag else "Could not find volume"

        # Find the market cap
        market_cap_tag = soup.find('fin-streamer', {'data-field': 'marketCap'})
        market_cap = market_cap_tag.text if market_cap_tag else "Could not find market cap"

        stock_data = {
            'stock_name': stock_name,
            'price': price,
            'previous_close': prev_close,
            'open_price': open_price,
            'days_range': days_range,
            '52_week_range': week_range,
            'volume': volume,
            'market_cap': market_cap
        }

        return stock_data
    else:
        return f"Failed to retrieve data. HTTP Status code: {response.status_code}"

while True:
    ticker = input("Enter the stock ticker symbol: ")
    stock_data = get_stock_data(ticker)

    if isinstance(stock_data, dict):
        while True:
            print("Available data fields:")
            for key in stock_data.keys():
                print(key)

            field = input("Enter the field you want to retrieve: ")
            if field in stock_data:
                print(f"{field}: {stock_data[field]}")
            else:
                print("Invalid field.")

            next_action = input("Would you like to check another value for the same stock, input a new ticker, or exit? (check/new/exit): ").strip().lower()
            if next_action == 'check':
                continue
            if next_action == 'new':
                break
            if next_action == "exit":
                exit()

        else:
            print(stock_data)
            retry = input("Would you like to re-input the ticker or exit? (yes/exit): ").strip().lower()
            if retry == 'exit':
                break
            if retry != 'yes':
                break
        
    else:
        restart = input("Would you like to restart or exit? (yes/exit): ").strip().lower()
        if restart == 'exit':
            exit()
        if restart != 'restart':
            break

    
