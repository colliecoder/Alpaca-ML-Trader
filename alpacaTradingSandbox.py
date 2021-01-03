import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import tensorflow as tf



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


canslim = pd.read_csv(filepath_or_buffer = "canslimAnalysis.csv")

if (canslim.empty):
    print("Error opening canslimAnalysis.csv\n")
else:
    print("canslimAnalysis.csv has been opened successfully\n")

def build_canslim(learning_rate):
    #linear regression model
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))
    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=learning_rate),
                  loss="mean_squared_error",
                  metrics=[tf.keras.metrics.RootMeanSquaredError()])
    print("Canslim model is built")
    print('\n')
    
    return model


def train_canslim(model, df, feature, label, epochs, batch_size):
    history = model.fit(x=df[feature],
                        y=df[label],
                        batch_size=batch_size,
                        epochs=epochs)
    trained_weight = model.get_weights()[0]
    trained_bias = model.getweights()[1]

    epochs = history.epoch

    hist = pd.DataFrame(history.history)

    rmse = hist["root_mean_squared_error"]

    print("Canslim model is trained")
    print('\n')

    return trained_weight, trained_bias, epochs, rmse


#define the variables for training here - not sure about batch size
learning_rate = 0.01
epochs = 30
batch_size = 30


#features and labels - at the moment we are only using one column
feature = "Relative Strength Index"
label = "buy_or_sell"

canslim_model = None


#build and train it here
canslim_model = build_canslim(learning_rate)

weight, bias, epochs, rmse = train_canslim(canslim_model, canslim,
                                           feature, label, epochs,
                                           batch_size)

"""
print("\nThe learned weight of Relative Strength Index model is %.4f" % weight)
print("The learned bias of Relative Strength Index model is %.4f\n" % bias )

"""



#use canslim analysis.csv file and a correlation matrix with
#a machine learning algorithm to analyze and trade on the stock market
