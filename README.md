# BTC-Predict-
# 🪙 BTC-Predict — Bitcoin Price Prediction using Machine Learning

A machine learning–powered system that predicts Bitcoin (BTC) price trends based on historical market data and technical indicators.  
Built with **Python** for data analysis and model training, and **JavaScript (optional)** for visualization/dashboard integration.  
This project aims to explore how quantitative modeling and AI can enhance crypto trading insights.

---

## 🚀 Features

- 📈 **Data Pipeline:** Automatically collects and preprocesses Bitcoin market data (via NestQuant API or CSV source).  
- 🧠 **Machine Learning Models:** Implements regression and neural-network–based predictors for BTC/USD closing prices.  
- ⚙️ **Feature Engineering:** Includes technical indicators such as moving averages, RSI, MACD, volatility, and volume metrics.  
- 📊 **Evaluation Metrics:** Uses MAE, RMSE, and directional accuracy to evaluate performance.  
- 🌐 **Optional Dashboard:** Simple front-end (JavaScript) visualization for daily predictions and historical comparison.  

---

## 🧩 Project Structure
```
BTC-Predict-/
│
├── data/                   # Historical Bitcoin market data (CSV or fetched via API)
├── models/                 # Trained ML models saved as .pkl or .h5 files
├── src/                    # Core source code for data processing and prediction
│   ├── data_loader.py      # Fetches and preprocesses raw BTC data
│   ├── feature_engineer.py # Builds technical indicators and transforms features
│   ├── train_model.py      # Trains machine learning models (e.g., LR, LSTM, etc.)
│   ├── predict.py          # Generates and exports BTC price predictions
│   └── evaluate.py         # Tests model accuracy and visualizes performance
│
├── web/                    # Optional JavaScript dashboard or REST API interface
├── requirements.txt        # Python dependencies and library requirements
└── main.ipynb              # Jupyter notebook for exploration and experimentation


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AnhTuanDangJT/BTC-Predict-.git
cd BTC-Predict-

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

Install dependencies
pip install -r requirements.txt
🧠 Usage
▶️ Train a model
python src/train_model.py

🔮 Make predictions
python src/predict.py

📊 Evaluate results
python src/evaluate.py


Predicted BTC prices and plots will be saved in the /output directory.
🧩 Technologies Used
Category	Tools
Programming Languages	Python, JavaScript
Data Libraries	Pandas, NumPy, Scikit-learn, TensorFlow/Keras
Visualization	Matplotlib, Seaborn, Plotly
Data Source	NestQuant API / Binance historical data
Model Types	Linear Regression, LSTM Neural Network
Version Control	Git & GitHub
