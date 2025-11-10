# NESTQUANT Market Test - BTC Price Prediction

This project automates the process of hourly data crawling, feature engineering, model training, and prediction submission for the NESTQUANT Market Test. It uses multiple data sources (stocks, forex, economic indicators) to predict Bitcoin (BTC) price movements using LightGBM machine learning models.

## Features

- **Automated Data Crawling**: Downloads market data from NESTQUANT API (stocks, forex, crypto, economic indicators)
- **Feature Engineering**: Extracts technical indicators (RSI, MACD, VWAP, volatility, returns) from multiple assets
- **Machine Learning**: Trains LightGBM regression models to predict BTC price movements
- **Automated Pipeline**: End-to-end workflow from data collection to prediction submission
- **Multi-Asset Features**: Uses correlated financial markets to improve prediction accuracy

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file in the project root:
```env
API_KEY=your_api_key_here
NESTQUANT_API_ENDPOINT=https://api-dev.nestquant.com
```

### 3. Download Data (First Time)
```bash
cd market_test
python crawlAsubmit/crawling.py
```

### 4. Run Main Script
```bash
cd market_test
python main/main.py
```

Or use the helper script from project root:
```bash
python run_main.py
```

## Detailed Setup

For comprehensive setup instructions, see:
- **QUICK_START.md** - Quick 5-step setup guide
- **SETUP_GUIDE.md** - Detailed setup and troubleshooting guide

## Project Structure

```
market_test/
├── main/
│   └── main.py              # Main execution script
├── preproces/
│   ├── preprocess.py        # Feature engineering
│   ├── get_feature.py       # Feature extraction and selection
│   └── feat_importance.py   # Feature importance analysis
├── training/
│   ├── train.py             # Model training (LightGBM)
│   └── predict.py           # Prediction generation
├── src/
│   ├── crawl.py             # Data crawling from API
│   └── submit.py            # Prediction submission to API
├── crawlAsubmit/            # Alternative crawling/submission scripts
├── model/                   # Saved trained models
└── realtimeData/            # Processed feature data
```

## How It Works

1. **Data Collection**: Downloads historical data for stocks, forex, crypto, and economic indicators
2. **Feature Engineering**: Calculates technical indicators (RSI, MACD, VWAP, volatility) for each asset
3. **Feature Selection**: Uses model-based feature importance to select relevant features
4. **Model Training**: Trains LightGBM regression models on 960 hours of historical data
5. **Prediction**: Generates predictions 25 hours ahead for BTC price movements
6. **Submission**: Submits predictions to NESTQUANT API for evaluation

## Key Parameters

- **Training Window**: 960 hours (~40 days) of historical data
- **Retraining Frequency**: Every 21 hours (delta=21)
- **Prediction Horizon**: 25 hours ahead
- **Model**: LightGBM with GOSS boosting, max_depth=4, learning_rate=0.08

## Requirements

- Python 3.8+
- pandas, numpy, lightgbm, scikit-learn
- python-dotenv, requests, pytz
- See `requirements.txt` for complete list

## Important Notes

⚠️ **Before running:**
1. Update hardcoded paths in `market_test/preproces/get_feature.py` to match your system
2. Ensure you have valid API credentials in `.env` file
3. Data files must be downloaded or available in the correct format

## Troubleshooting

Common issues and solutions are documented in **SETUP_GUIDE.md**.

## License

This project is for the NESTQUANT Market Test 2023 competition.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements.
