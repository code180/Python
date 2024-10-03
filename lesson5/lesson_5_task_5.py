from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/inputs")


string = driver.find_element(
        By.CSS_SELECTOR, "#content")

string.send_keys(1000)
sleep(5)

string.clear
