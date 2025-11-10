# Quick Start Guide

## Fast Setup (5 steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env` File
Create a `.env` file in the project root with:
```env
API_KEY=your_api_key_here
NESTQUANT_API_ENDPOINT=https://api-dev.nestquant.com
```

### 3. Download Data (First Time Only)
```bash
cd market_test
python crawlAsubmit/crawling.py
```

This will create a `data/` directory with all required data files.

### 4. Create Output Directories
```bash
# Windows PowerShell
mkdir market_test\realtimeData, market_test\model -Force

# Linux/Mac
mkdir -p market_test/realtimeData market_test/model
```

### 5. Run the Main Script
```bash
cd market_test
python main/main.py
```

## Important Notes

⚠️ **Before running, you must:**
1. Update hardcoded paths in `market_test/preproces/get_feature.py` (lines 179, 197, 199, 209, 246, 250, 260)
2. Have data files ready (either download via API or use existing data)
3. Ensure your API key is valid

## Troubleshooting

- **"File not found" errors**: Update paths in `get_feature.py` to match your system
- **"Module not found"**: Run `pip install -r requirements.txt`
- **"API_KEY not found"**: Create `.env` file with your API key
- **"realtime_feature.csv not found"**: The script needs preprocessing to run first. Check if `get_and_update_feature()` function is working correctly.

## What the Script Does

1. Loops through hourly timestamps (Aug 25-26, 2023)
2. Preprocesses data every 21 hours
3. Trains LightGBM model every 21 hours
4. Generates predictions for each hour
5. Collects all predictions

## Expected Runtime

- First run: ~30-60 minutes (includes data preprocessing and training)
- Subsequent runs: Faster if data is already processed

For detailed information, see `SETUP_GUIDE.md`.

