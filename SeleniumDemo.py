import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

HOME_URL = "https://www.flipkart.com/"

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(HOME_URL)
time.sleep(5)

search_box = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
search_box.send_keys("redtape") 

search_box.send_keys(Keys.ENTER)

time.sleep(2)

shoe = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[1]')
shoe.click()

time.sleep(5)


# Select and Click Add to Cart
AddTocart = driver.find_element(By.ID,'//*[@id="swatch-3-size"]/a')
AddTocart.click()
time.sleep(5)

BuyNow = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button')
BuyNow.click()
time.sleep(5)

# Visit the Cart Page and Verify the Order

# viewCart = driver.find_element(By.XPATH,'//*[@id="nav-cart-count"]')
# viewCart.click()

# time.sleep(10)