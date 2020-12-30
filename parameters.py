# #https://www.thepythoncode.com/article/stock-price-prediction-in-python-using-tensorflow-2-and-keras
# add credits to this dev for coming up with the model

import os
import time
from tensorflow.keras.layers import LSTM,GRU,SimpleRNN


# Window size or the sequence length
N_STEPS = 150
# Lookup step, 1 is the next day
LOOKUP_STEP = 1

# test ratio size, 0.2 is 20%
TEST_SIZE = 0.2
# features to use
FEATURE_COLUMNS = ["close", "volume", "open", "high", "low"]
# date now
date_now = time.strftime("%Y-%m-%d")

# Data history
START_DATE = '1999-02-04'
END_DATE = '2020-07-30'

### model parameters

N_LAYERS = 3
# LSTM cell
CELL = LSTM
# 256 LSTM neurons
UNITS = 256
# 40% dropout
DROPOUT = 0.2
# whether to use bidirectional RNNs
BIDIRECTIONAL = False

### training parameters

# mean absolute error loss
# LOSS = "mae"
# huber loss
LOSS = "huber_loss"
OPTIMIZER = "adam"
BATCH_SIZE = 64
EPOCHS = 100

# 'Ticker' stock market
ticker = "JFC"
ticker_data_filename = os.path.join("data", f"{ticker}_{date_now}.csv")
# model name to save, making it as unique as possible based on parameters
model_name = f"{date_now}_{ticker}-{LOSS}-{OPTIMIZER}-{CELL.__name__}-seq-{N_STEPS}-step-{LOOKUP_STEP}-layers-{N_LAYERS}-units-{UNITS}"
if BIDIRECTIONAL:
    model_name += "-b"