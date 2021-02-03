#https://pypi.org/project/yfinance/

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date as dt
import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

today = dt.today().strftime("%Y-%m-%d")

createFolder('C:/Users/Seeni/OneDrive/Desktop/Option_History/TQQQ/Calls/' + today)
createFolder('C:/Users/Seeni/OneDrive/Desktop/Option_History/TQQQ/Puts/' + today)

tqqq = yf.Ticker("TQQQ")

for day in tqqq.options:
    tqqq_options = tqqq.option_chain(day)
    tqqq_calls = tqqq_options.calls

    tqqq_calls.to_csv('C:/Users/Seeni/OneDrive/Desktop/Option_History/TQQQ/Calls/' + today + "/" + day + ".csv")

    tqqq_puts = tqqq_options.puts
    tqqq_puts.to_csv('C:/Users/Seeni/OneDrive/Desktop/Option_History/TQQQ/Puts/' + today + "/" + day + ".csv")

# storing options data for TMF
createFolder('C:/Users/Seeni/OneDrive/Desktop/Option_History/TMF/Calls/' + today)
createFolder('C:/Users/Seeni/OneDrive/Desktop/Option_History/TMF/Puts/' + today)

tmf = yf.Ticker("TMF")

for day in tmf.options:
    tmf_options = tmf.option_chain(day)
    tmf_calls = tmf_options.calls

    tmf_calls.to_csv('C:/Users/Seeni/OneDrive/Desktop/Option_History/TMF/Calls/' + today + "/" + day + ".csv")

    tmf_puts = tmf_options.puts
    tmf_puts.to_csv('C:/Users/Seeni/OneDrive/Desktop/Option_History/TMF/Puts/' + today + "/" + day + ".csv")


#storing options data for UVXY
createFolder('C:/Users/Seeni/OneDrive/Desktop/Option_History/UVXY/Calls/' + today)
createFolder('C:/Users/Seeni/OneDrive/Desktop/Option_History/UVXY/Puts/' + today)

uvxy = yf.Ticker("UVXY")

for day in uvxy.options:
    uvxy_options = uvxy.option_chain(day)
    uvxy_calls = uvxy_options.calls

    uvxy_calls.to_csv('C:/Users/Seeni/OneDrive/Desktop/Option_History/UVXY/Calls/' + today + "/" + day + ".csv")

    uvxy_puts = uvxy_options.puts
    uvxy_puts.to_csv('C:/Users/Seeni/OneDrive/Desktop/Option_History/UVXY/Puts/' + today + "/" + day + ".csv")