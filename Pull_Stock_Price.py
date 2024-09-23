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
        name_tag = soup.find('h1', {'class': 'D(ib) Fz(18px)'})
        stock_name = name_tag.text if name_tag else "Could not find stock name"

        # Find the previous close price
        prev_close_tag = soup.find('td', {'data-test': 'PREV_CLOSE-value'})
        prev_close = prev_close_tag.text if prev_close_tag else "Could not find previous close price"

        # Find the open price
        open_tag = soup.find('fin-streamer', {'data-field': 'regularMarketOpen'})
        open_price = open_tag.text if open_tag else "Could not find open price"

        # Find the day's range
        days_range_tag = soup.find('td', {'data-test': 'DAYS_RANGE-value'})
        days_range = days_range_tag.text if days_range_tag else "Could not find day's range"

        # Find the 52 week range
        week_range_tag = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})
        week_range = week_range_tag.text if week_range_tag else "Could not find 52 week range"

        # Find the volume
        volume_tag = soup.find('td', {'data-test': 'TD_VOLUME-value'})
        volume = volume_tag.text if volume_tag else "Could not find volume"

        # Find the market cap
        market_cap_tag = soup.find('td', {'data-test': 'MARKET_CAP-value'})
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

# Example usage
ticker = input("Enter the stock ticker symbol: ")
stock_data = get_stock_data(ticker)

if isinstance(stock_data, dict):
    print("Available data fields:")
    for key in stock_data.keys():
        print(key)

    field = input("Enter the field you want to retrieve: ")
    if field in stock_data:
        print(f"{field}: {stock_data[field]}")
    else:
        print("Invalid field.")
else:
    print(stock_data)
