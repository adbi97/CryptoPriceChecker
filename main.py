######################################################################################################################
# Program Written by Aadib Ahsan 04-2021

# Import Modules
import os.path
from pathlib import Path
import getdata
######################################################################################################################
# Checks to see if a data file for the ticker already exists, and creates one if it doesn't
ticker = input("Please enter the Ticker of the Cryptocurrency you would like to track: ")
tickerstring = (ticker + "_data.txt")
file_path_string = ("C:/Users/aadib/PycharmProjects/cryptochecker/" + tickerstring)
my_file = Path(file_path_string)

if my_file.exists():
    pass
else:
    f = open(tickerstring, "a")
    f.write(str("date,price") + "\n")
    f.close()

#####################################################################################################################

getdata.write_data(ticker, tickerstring)

