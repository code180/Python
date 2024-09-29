from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/entry_ad")


close = driver.find_element(
        By.CLASS_NAME, 'modal-footer')
close.click
sleep(1)
