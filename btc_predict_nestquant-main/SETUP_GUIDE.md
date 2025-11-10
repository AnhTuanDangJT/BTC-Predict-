# Setup and Running Guide for BTC Prediction Project

## Prerequisites

1. **Python 3.8 or higher** (Python 3.10+ recommended)
2. **pip** (Python package installer)

## Step 1: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas numpy lightgbm scikit-learn python-dotenv requests pytz optuna ipython
```

## Step 2: Environment Configuration

Create a `.env` file in the project root directory with the following variables:

```env
API_KEY=your_api_key_here
NESTQUANT_API_ENDPOINT=https://api-dev.nestquant.com
```

**Note:** Replace `your_api_key_here` with your actual NESTQUANT API key.

## Step 3: Data Setup

The project requires data files to be present. You have two options:

### Option A: Download Data via API (Recommended)

1. First, download the data by running the crawling script:
   ```bash
   cd market_test
   python crawlAsubmit/crawling.py
   ```

   This will download:
   - Stock data (AAPL, AMZN, GOOG, etc.)
   - Forex data (AUDUSD, EURUSD, etc.)
   - Economic indicators (FRED data)
   - Crypto data (BTC)
   - Label data (BTC labels)

2. The data will be saved in `./data/` directory with subdirectories:
   - `./data/Stocks/`
   - `./data/FX/`
   - `./data/FRED/`
   - `./data/Crypto/`
   - `./data/Label/`

### Option B: Use Existing Data

If you already have data files, ensure they are in the correct format (Parquet files) and placed in the appropriate directories.

## Step 4: Create Required Directories

Create the necessary directories for output files:

```bash
# Windows (PowerShell)
mkdir -p market_test\realtimeData
mkdir -p market_test\model

# Linux/Mac
mkdir -p market_test/realtimeData
mkdir -p market_test/model
```

## Step 5: Configure File Paths (Important!)

The `get_feature.py` file contains hardcoded paths that need to be updated for your system:

1. **Update data paths in `market_test/preproces/get_feature.py`:**
   - Line 179: Change `/kaggle/input/nq2023/data` to your data directory path
   - Line 197: Change `/kaggle/input/nq2023/data/Crypto/BTCUSDT` to your BTC data path
   - Line 199: Change `/kaggle/input/nq2023/data/Label/LABEL_BTCUSDT` to your label data path
   - Line 209: Change `/kaggle/input/nq2023/data/Stocks/SPY` to your SPY data path
   - Line 246: Change `/kaggle/working/realtime_feature.csv` to your output path
   - Line 250: Update the realtime_feature.csv path
   - Line 260: Update the Label data path

**Recommended:** Use relative paths based on the project structure:
```python
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'data')
```

## Step 6: Run the Main Script

### Basic Run

Navigate to the project directory and run:

```bash
cd market_test
python main/main.py
```

### Understanding the Main Script

The `main.py` script:
1. Loops through hourly timestamps (from 1690207200000 to 1690297200000)
2. Preprocesses data every 21 hours (delta=21)
3. Trains the model every 21 hours
4. Generates predictions for each hour
5. Collects all predictions

### Parameters

You can modify these parameters in `main.py`:
- `rangee = 960`: Training window size (hours)
- `delta = 21`: Retraining frequency (hours)
- `num_boost_round = 90`: Number of boosting iterations

## Step 7: Troubleshooting

### Common Issues

1. **Missing data files:**
   - Error: `FileNotFoundError` for data files
   - Solution: Run the crawling script first or update file paths

2. **Missing API key:**
   - Error: `API_KEY not found`
   - Solution: Create `.env` file with your API key

3. **Module not found:**
   - Error: `ModuleNotFoundError`
   - Solution: Install missing packages with `pip install <package_name>`

4. **Path issues on Windows:**
   - The script uses relative paths, but some functions may have hardcoded Linux paths
   - Solution: Update paths in `get_feature.py` to use `os.path.join()` for cross-platform compatibility

5. **Missing feature file:**
   - Error: `realtime_feature.csv not found`
   - Solution: The script will skip iterations if the feature file doesn't exist. Make sure preprocessing runs first.

### Expected Output

The script will output:
- Preprocessing status messages
- Training status messages
- Prediction results for each hour
- Final list of all predictions

## Step 8: Submit Predictions (Optional)

To submit predictions to the NESTQUANT API, uncomment the submission code in `main.py`:

```python
from src.submit import Submission
s = Submission(api_key=os.getenv('API_KEY'))
timestamp = s.submit(False, data=data_set, symbol='BTC')
print("Sucessful submit to the system: 🥳 🥳 ")
print("Submission time: " + str(timestamp))
```

## Project Structure

```
btc_predict_nestquant-main/
├── market_test/
│   ├── main/
│   │   └── main.py          # Main execution script
│   ├── preproces/
│   │   ├── preprocess.py    # Feature engineering
│   │   ├── get_feature.py   # Feature extraction
│   │   └── ...
│   ├── training/
│   │   ├── train.py         # Model training
│   │   └── predict.py       # Prediction generation
│   ├── src/
│   │   ├── crawl.py         # Data crawling
│   │   └── submit.py        # API submission
│   ├── model/               # Saved models
│   └── realtimeData/        # Processed features
├── data/                    # Raw data (created after crawling)
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables (create this)
```

## Additional Notes

1. **Time Zone:** The script uses Vietnamese timezone (Asia/Ho_Chi_Minh) for calculations
2. **Data Format:** The project expects Parquet files for input data
3. **Model:** Uses LightGBM for regression (predicting BTC price movements)
4. **Features:** Extracts technical indicators (RSI, MACD, VWAP, etc.) from multiple assets

## Getting Help

If you encounter issues:
1. Check the log file: `market_test/main/log.txt`
2. Verify all dependencies are installed
3. Ensure data files are in the correct format and location
4. Check that API keys are correctly configured in `.env`

