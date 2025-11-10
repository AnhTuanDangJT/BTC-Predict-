# Why You Can't Run the File - Issues Fixed

## Summary

The main issues preventing the script from running have been **FIXED**:

### ✅ Issues Fixed:

1. **Missing Dependencies** - FIXED
   - Installed all required packages: pandas, numpy, lightgbm, etc.

2. **Unicode Encoding Error** - FIXED
   - Removed emoji characters that Windows console can't display
   - Added UTF-8 encoding support

3. **Path Calculation Error** - FIXED
   - Fixed duplicate `market_test` in path calculation
   - Now correctly calculates: `market_test/realtimeData/`

4. **Hardcoded Paths** - FIXED
   - Updated `get_feature.py` to use relative paths instead of hardcoded Kaggle paths
   - Changed from `/kaggle/input/nq2023/data` to relative `data/` directory
   - Fixed Windows path splitting issues (changed from `split('/')` to `os.path.basename()`)

### ⚠️ Remaining Requirements:

1. **Data Files Must Be Downloaded**
   - The script needs data files in the `data/` directory
   - Run: `python market_test/crawlAsubmit/crawling.py`
   - This requires a valid API key in `.env` file

2. **.env File Configuration**
   - Create `.env` file in project root with:
     ```
     API_KEY=your_api_key_here
     NESTQUANT_API_ENDPOINT=https://api-dev.nestquant.com
     ```

## What Was Wrong

### Original Errors:

1. **ModuleNotFoundError: No module named 'pandas'**
   - **Cause:** Dependencies not installed
   - **Fix:** Ran `pip install -r requirements.txt`

2. **UnicodeEncodeError: 'charmap' codec can't encode character**
   - **Cause:** Emoji characters in print statements
   - **Fix:** Removed emojis, added UTF-8 encoding support

3. **FileNotFoundError: [WinError 3] The system cannot find the path specified: '/kaggle/input/nq2023/data'**
   - **Cause:** Hardcoded Linux/Kaggle paths
   - **Fix:** Updated to use relative paths based on project structure

4. **Wrong path calculation: `market_test\market_test\realtimeData`**
   - **Cause:** Incorrect directory level calculation
   - **Fix:** Corrected path calculation to use `market_test_dir` directly

## How to Run Now

1. **Install dependencies** (if not already done):
   ```bash
   pip install -r requirements.txt
   ```

2. **Create .env file** with your API key:
   ```env
   API_KEY=your_api_key_here
   NESTQUANT_API_ENDPOINT=https://api-dev.nestquant.com
   ```

3. **Download data**:
   ```bash
   cd market_test
   python crawlAsubmit/crawling.py
   ```

4. **Run the main script**:
   ```bash
   cd market_test
   python main/main.py
   ```

## Current Status

✅ **All code issues fixed**
✅ **Dependencies installed**
⚠️ **Need data files** (download via crawling script)
⚠️ **Need .env file** (create with API key)

The script should now run successfully once you have:
- Data files in `data/` directory
- Valid API key in `.env` file

## Next Steps

1. Create `.env` file with your API key
2. Run the data crawling script to download required data
3. Run `main.py` - it should work now!

If you still encounter errors, check:
- Are data files in the correct location? (`data/Crypto/BTCUSDT`, etc.)
- Is the `.env` file in the project root?
- Are all dependencies installed?

