from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


driver.get("https://the-internet.herokuapp.com/login")


usearname = driver.find_element(
        By.NAME, "usearname")
usearname.send_keys("tomsmith")
sleep(1)

password = driver.find_element(
        By.NAME, "password")
password.send_keys("SuperSecretPassword!")

login = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
login.click
