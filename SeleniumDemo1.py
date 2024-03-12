import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
UserName="standard_user"
Password="secret_sauce"
HOME_URL = "https://www.saucedemo.com/"

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(HOME_URL)
time.sleep(2)

search_box1 = driver.find_element(By.XPATH,'//*[@id="user-name"]')
search_box1.send_keys(UserName) 
# pswd
search_box2 = driver.find_element(By.XPATH,'//*[@id="password"]')
search_box2.send_keys(Password) 
search_box2.send_keys(Keys.ENTER)
# search_box.send_keys("redtape") 

# search_box.send_keys(Keys.ENTER)
time.sleep(5)

prd = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
prd.click()

time.sleep(2)

crt = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
crt.click()
time.sleep(2)

chk = driver.find_element(By.XPATH,'//*[@id="checkout"]')
chk.click()
time.sleep(2)
name1="Rahul"
name2="R"
zip=678581
nm = driver.find_element(By.XPATH,'//*[@id="first-name"]')
nm.send_keys(name1)
time.sleep(2)
nm2 = driver.find_element(By.XPATH,'//*[@id="last-name"]')
nm2.send_keys(name2)
time.sleep(2)
zp = driver.find_element(By.XPATH,'//*[@id="postal-code"]')
zp.send_keys(zip)
time.sleep(2)

chk1 = driver.find_element(By.XPATH,'//*[@id="continue"]')
chk1.click()
time.sleep(2)
fnsh = driver.find_element(By.XPATH,'//*[@id="finish"]')
fnsh.click()

time.sleep(10)
