# Stock News Alert System

This project is a simple Python-based script that monitors the daily stock price changes for a specific stock (by default, Apple Inc. - AAPL).
If the stock price changes by more than 5% compared to the previous day, the script fetches relevant news articles about the stock and sends an email with the top 3 articles. 

It uses the Alpha Vantage API for stock data and the News API for news articles. The email alerts are sent via the Gmail SMTP server.

## Overview
Stock Price Monitoring: The script automatically fetches the stock data for AAPL (Apple) by default. It compares the closing price of the most recent two days.
Stock Change Calculation: If the stock price changes by 5% or more (up or down), the script fetches the top 3 news articles from the News API related to the stock symbol.
Email Alerts: If the change is significant, an email with the news headlines is sent to the specified email (both sender and receiver can be the same email).

## Features
- **Fetch Stock Data**: The script retrieves daily stock price data using the Alpha Vantage API.
- **Fetch News Articles**: If a significant stock price change occurs (5% or more), the script fetches the top 3 news articles related to the stock from the News API.
- **Send Email Alerts**: Sends an email alert with the stock price change and news headlines when the price change threshold is met.

## Requirements

- **Python 3.12
- **Alpha Vantage API Key**: To fetch stock data.
- **News API Key**: To fetch relevant news articles.
- **Gmail Account**: To send email alerts.
- **Python Libraries**:
  - `requests`
  - `python-dotenv`
  - `smtplib`

## Set up environment variables:
**Create a .env file in the project root directory to store your API keys and email credentials:
- STOCK_API_KEY=your_alpha_vantage_api_key
- NEWS_API=your_news_api_key
- MAIL_PASS=your_gmail_password

## Important Notes
- API Rate Limits: The Alpha Vantage API has a limit of 25 API requests per day
- 




