import multiprocessing as mp
mp.set_start_method('spawn', force=True)


import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
print('Importing tensorflow...' + tf.__version__)

from tensorflow import keras



#authentication variable setup
api_key = 'insert_key'
api_secret = 'insert_secret_key'
base_url = 'https://paper-api.alpaca.markets'

#open REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version = 'v2')


#tests its open
account = api.get_account()
if(account == None):
    print("Error connecting to Alpaca\n")
else:
    print("Alpaca opened\n")

#define the variables for training here - not sure about batch size
learning_rate = 0.01
epochs = 30
batch_size = 2


#features and labels - at the moment we are only using one column
feature = 'Relative Strength Index'
label = "buy_or_sell"

#canslim_model = None
'''

#buyShare function - takes ticker as input
def buyShare(ticker):
    api.submit_order(
        symbol=ticker,
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
        )
    print(ticker + " share purchased\n")

#sellShare function - takes ticker as input
def sellShare(ticker):
    api.submit_order(
        symbol = ticker,
        qty = 1,
        side = 'sell',
        type = 'market',
        time_in_force = 'gtc'
        )
    print(ticker + " share sold\n")
'''

canslim = pd.read_csv(filepath_or_buffer = "canslimAnalysis.csv")

if (canslim.empty):
    print("Error opening canslimAnalysis.csv\n")
else:
    print("canslimAnalysis.csv has been opened successfully\n")


model = keras.Sequential(
    [
        layers.Dense(2, activation = "relu", name="layer1"),
    ]
)

print("Model built")

#mean square error and stochastic gradient descent
model.compile(optimizer='sgd', loss='mean_squared_error')

'''
MODIFY CODE HERE - needs to read data in from canslim
pandas?
'''
xs = np.array([76.62, 36.62, 53.07, 55.65, 67.5, 40.94, 49.69, 52.75, 58.39], dtype=float) #feature column
ys = np.array([1, 0, 1, 1, 1, 0, 1, 1, 1], dtype=float) #label columm
print("data loaded")

#train
model.fit(xs, ys, epochs=50)

#testing
print("This should be zero: ")
print(model.predict([44.44]))
print("This should be zero: ")
print(model.predict([51.71]))

