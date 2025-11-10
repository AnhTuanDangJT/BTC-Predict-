import os
import sys
import pickle
import pandas as pd
import itertools
import pytz
from datetime import datetime

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..'))

from src.crawl import Crawler
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from preproces.preprocess import *
from preproces.feat_importance import *
from preproces.get_feature import *
from training.train import *
from training.predict import *
from IPython.utils import io




if __name__ == "__main__":
    # from datetime import datetime

    # # Set the time zone to Vietnamese time (Indochina Time)
    # vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')

    # # Get the current time in the Vietnamese time zone
    # # current_time_in_vietnam = datetime.now(vietnam_timezone)

    # # # Get the hour from the current time
    # # current_hour_in_vietnam = current_time_in_vietnam.hour
    # # # print("current hours: "+ str(current_hour_in_vietnam)) 

    # print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    # print("Start to crawlling ...")
    # print("Please wait ... 🙄 🙄")
    # print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    
    # #crawlinng
    # stocks_lst = ["AAPL","AMZN","AVGO","BRK.B","GOOG","JNJ","JPM","LLY","META","MSFT","NVDA","QQQ","TSLA","UNH","V","WMT","XOM","SPY"]
    # fx_lst = ["AUDUSD","EURUSD","GBPUSD","USDJPY","XAUUSD"]
    # fred_lst = ["T1YFF","SOFR","DCOILBRENTEU","CPFF","BAA10Y"]
    # crawler = Crawler(api_key=os.getenv('API_KEY')) # Put your API key in .env file
    # for i in stocks_lst:
    #     crawler.download_historical_data(category="stocks", symbol=f"{i}", location='./data/Stocks')
    # for i in fx_lst:
    #     crawler.download_historical_data(category="fx", symbol=f"{i}", location='./data/FX')
    # for i in fred_lst:
    #     crawler.download_historical_data(category="fred", symbol=f"{i}", location='./data/FRED')
    # #print("Lastest data: ", crawler.get_lastest_data(category="crypto", symbol="BTCUSDT"))
    
    # crawler.download_historical_data(category="crypto", symbol="BTC", location='./data/Crypto')
    # crawler.download_historical_data(category="label", symbol="BTC", location='./data/Label')
    # print("sucessful crawling data")
    # print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    # #preprocessing and getting data
    submitt = []

    for i in range(1690207200000+ 3600000, 1690297200000, 3600000):
        current_hour_in_vietnam = ((i%(3600000*24))/3600000) +7
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("Start to preprocessing data")
        print("Keep going...")

        rangee = 960
        delta= 21
        num_boost_round = 90
        with io.capture_output() as captured:


            if current_hour_in_vietnam%delta ==2:
                get_and_update_feature(False, rangee,i, delta)
                
            # elif current_hour_in_vietnam%4 !=2:
            #     get_and_update_feature(True)
        # Get base directory (market_test folder - parent of main folder)
        market_test_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        realtime_data_dir = os.path.join(market_test_dir, 'realtimeData')
        model_dir = os.path.join(market_test_dir, 'model')
        
        # Create directories if they don't exist
        os.makedirs(realtime_data_dir, exist_ok=True)
        os.makedirs(model_dir, exist_ok=True)
        
        feature_csv_path = os.path.join(realtime_data_dir, 'realtime_feature.csv')
        model_pkl_path = os.path.join(model_dir, 'trained_model.pkl')
        
        # Check if feature file exists
        if not os.path.exists(feature_csv_path):
            print(f"Warning: Feature file not found at {feature_csv_path}")
            print("Please run data crawling and preprocessing first.")
            continue
            
        testting = pd.read_csv(feature_csv_path)
        
        
        print("....")
        if current_hour_in_vietnam%delta==2:
            print("Sucessful get preprocessed data with shape of: "+ str(testting.shape))
        
        elif current_hour_in_vietnam%delta!=2:
            print("successful updating data with shape of: "+ str(testting.shape))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        #training

        print("Start to train ...")
        

        df_final = pd.read_csv(feature_csv_path)
        df_final = df_final.dropna()
        dff = df_final.copy()
        # Remove Unnamed: 0 column if it exists
        if "Unnamed: 0" in dff.columns:
            dff = dff.drop("Unnamed: 0", axis = 1)

        if current_hour_in_vietnam%delta ==2:

            model = train(dff,rangee,num_boost_round, i)
            pickle.dump(model, open(model_pkl_path, 'wb'))
            print("....")

            print("Sucessful trained data with the shape of: "+ str(testting.shape))
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        

    
        print("Time to predict and submit my result...")
        
        # Check if model exists
        if not os.path.exists(model_pkl_path):
            print(f"Warning: Model file not found at {model_pkl_path}")
            print("Please train the model first.")
            continue
            
        data = pd.read_csv(feature_csv_path)
        model = pickle.load(open(model_pkl_path, 'rb')) 
        #print(data)
        submit = get_predict(model, data, i)
        data_set = submit.to_dict('records')
        submitt.append(data_set)
        print(data_set)
        # s = Submission(api_key='svx8ZNYrgMNyuithrHdnLEAkn7OzlBKp8h5rzy2e')
        # timestamp = s.submit(False, data=data_set, symbol='BTC')
        # print("Sucessful submit to the system: 🥳 🥳 ")
        # print("Submission time: " + str(timestamp))

        print("-----------------------------------------------------------------------------------------------------------------------------------------------")


    flat_list = list(itertools.chain(*submitt))
    print(flat_list)
    print(f"Total predictions: {len(flat_list)}")
    
    # Note: get_score function is not defined in this file
    # If you need scoring, implement it or import from another module
    # score = get_score(flat_list)
    # print("Final score: "+ str(score))