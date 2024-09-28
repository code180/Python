from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


for _ in range(5):
    Add_Elements = driver.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    sleep(1)

    Remove_Elements = driver.find_elements(
        By.XPATH, '//button[text()="Delete"]')

print(len(Remove_Elements))
