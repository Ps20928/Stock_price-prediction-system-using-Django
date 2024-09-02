from django.shortcuts import render
import yfinance as yf
import pandas as pd

from .forms import StockPredictionForm
from .prediction import predict_stock_price

def home(request):
    top_50_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'BRK-B', 'META', 'V', 'JNJ', ...]  # Add more tickers
    stock_data = []

    for ticker in top_50_tickers:
        data = yf.download(ticker, period='1mo', interval='1d')
        if not data.empty:
            stock_data.append({
                'symbol': ticker,
                'high': data['High'].max(),
                'low': data['Low'].min(),
                'average': data['Close'].mean(),
            })

    return render(request, 'predictor/home.html', {'stock_data': stock_data})

def company_data(request):
    trend = None

    if request.method == 'POST':
        symbol = request.POST.get('symbol').upper()
        stock_data = yf.download(symbol, period='1mo', interval='1d')

        if not stock_data.empty:
            initial_price = stock_data['Close'].iloc[0]
            current_price = stock_data['Close'].iloc[-1]
            change = ((current_price - initial_price) / initial_price) * 100

            high_price = stock_data['High'].max()
            low_price = stock_data['Low'].min()
            avg_price = stock_data['Close'].mean()

            trend = {
                'symbol': symbol,
                'change': round(change, 2),
                'status': 'Bullish' if change > 0 else 'Bearish',
                'alert_class': 'success' if change > 0 else 'danger',
                'high': round(high_price, 2),
                'low': round(low_price, 2),
                'average': round(avg_price, 2),
            }

    return render(request, 'predictor/company_data.html', {'trend': trend})

def predict_stock(request):
    if request.method == 'POST':
        form = StockPredictionForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol'].upper()
            prediction = predict_stock_price(symbol)
    else:
        form = StockPredictionForm()

    return render(request, 'predictor/predict.html', {'form': form})

def about(request):
    return render(request, 'predictor/about.html')
