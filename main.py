import requests
import pprint
import os
from dotenv import load_dotenv
import smtplib

STOCK_NAME = "AAPL"

load_dotenv()
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API")


def get_stock_data(api_key, stock_name):
    url = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_name,
        "apikey": api_key
    }

    response = requests.get(url, parameters)
    # print(response.status_code)
    return response.json()['Time Series (Daily)']


def get_news_data(news_api, stock_name, date):
    url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": stock_name,
        "from": date,
        "sortBy": "popularity",
        "apiKey": news_api,
    }
    response = requests.get(url, params=news_params)
    # print(response.status_code)

    return response.json()


# Call stock data function.
stock_data = get_stock_data(stock_api_key, STOCK_NAME)
# pprint.pprint(data)

all_dates = [key for (key, content) in stock_data.items()]
yesterday = all_dates[0]
before_yesterday = all_dates[1]

yesterday_close_stock = float(stock_data[yesterday]['4. close'])
before_yesterday_close_stock = float(stock_data[before_yesterday]['4. close'])

# Calculate difference in percentage
difference = yesterday_close_stock - before_yesterday_close_stock
percentage = difference / before_yesterday_close_stock * 100

# Symbol to shortly show percentage status (raise or fall).
if percentage > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

# If stock percentage rises by 5%, then the mail will be sent with top 3 articles.
if abs(percentage) >= 5:
    # Call news function.
    all_news = get_news_data(news_api_key, STOCK_NAME, yesterday)['articles']
    top_three_news = all_news[:3]

    # Send each article as a separate message via mail.
    # for i in range(3):
    #     with smtplib.SMTP("smtp.gmail.com") as connection:
    #         connection.starttls()
    #         connection.login(user="me@gmail.com", password=f"{os.getenv("MAIL_PASS")}")
    #         connection.sendmail(from_addr="me@gmail.com", to_addrs="me@gmail.com",
    #                             msg=f"Subject:{STOCK_NAME}: {symbol}{round(percentage)}%\n\n"
    #                                 f'Headline {i + 1}: {top_three_news[i]["title"]}\n'
    #                                 f'Brief: {top_three_news[i]["description"]}\n'
    #                                 f'URL: {top_three_news[i]["url"]}')

    # Simulate mail message in python console.
    for i in range(3):
        print(f'{STOCK_NAME}: {symbol}{round(percentage)}%\n'
              f'Headline {i + 1}: {top_three_news[i]["title"]}\n'
              f'Brief: {top_three_news[i]["description"]}\n'
              f'URL: {top_three_news[i]["url"]}')
