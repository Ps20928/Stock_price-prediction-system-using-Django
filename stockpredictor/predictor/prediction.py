import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

def preprocess_data(symbol, look_back=60):
    # Fetch stock data
    data = yf.download(symbol, period='1y', interval='1d')

    # Select the 'Close' prices and convert to numpy array
    close_prices = data['Close'].values

    # Reshape the data to 2D array
    close_prices = close_prices.reshape(-1, 1)

    # Scale the data between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_prices)

    # Create data structure with `look_back` time-steps
    X, y = [], []
    for i in range(look_back, len(scaled_data)):
        X.append(scaled_data[i-look_back:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)

    # Reshape X to be accepted by LSTM layer (samples, time-steps, features)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    return X, y, scaler


def create_rnn_model(input_shape):
    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


def predict_stock_price(symbol):
    look_back = 60  # Use 60 days of data to predict the next day's price

    # Preprocess the data
    X, y, scaler = preprocess_data(symbol, look_back)

    # Create the RNN model
    model = create_rnn_model((X.shape[1], 1))

    # Train the model
    model.fit(X, y, batch_size=32, epochs=10)

    # Predict the next day's price
    last_60_days = X[-1].reshape(1, look_back, 1)
    predicted_price = model.predict(last_60_days)
    predicted_price = scaler.inverse_transform(predicted_price)

    return predicted_price[0][0]
