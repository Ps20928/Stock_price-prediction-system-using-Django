# Stock Prediction System

This project is a stock prediction system built using Django, integrating machine learning algorithms and data from Yahoo Finance to predict stock prices. The system also includes functionalities for viewing top 50 stocks, Bear vs Bull analysis, and a user-friendly UI for interacting with the data.

## Features

- **Home Page**: Displays charts for the top 50 stocks, including high, low, and average prices using Chart.js.
- **Company Data**: Allows users to input a stock symbol to view Bear vs Bull trends, including price changes, highs, lows, and average prices.
- **Prediction Window**: A form for predicting stock prices using machine learning models.
- **About Page**: Provides information about the system and its functionalities.

## Installation

### Steps to Install

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/stock_prediction_system.git
    cd stock_prediction_system
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional)**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

- **stock_prediction**: Main project directory containing settings and configurations.
- **predictor**: Django app handling the core functionalities like views, models, and templates.
- **templates**: Directory containing HTML templates for the UI.
- **static**: Directory for static files like CSS and JavaScript.

## Usage

- **Home Page**: View the top 50 stocks by market cap with their high, low, and average prices.
- **Company Data**: Analyze a stock's trend (Bullish or Bearish) over the past month by entering its symbol.
- **Prediction Window**: Predict the future price of a stock using machine learning models (to be implemented).
- **About Page**: Learn more about the system and its capabilities.


*This project is for educational purposes and should not be used for actual stock trading without proper financial advice.*
