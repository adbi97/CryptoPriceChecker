from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from selenium.common.exceptions import NoSuchElementException
import os

today = date.today()
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def write_data(ticker, tickerstring):
    driver.get("https://www.coinspot.com.au/buy/" + ticker + "#")
    try:
        search = driver.find_element_by_class_name("price-title")
        price = search.text.replace("$", "")
        f = open(tickerstring, "a")
        f.write(str(today) + "," + price + "\n")
        driver.close()
    except NoSuchElementException:
        print("That is an invalid ticker, please try another ticker.")
        os.remove(tickerstring)
