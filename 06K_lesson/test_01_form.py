from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(
    By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
driver.find_element(
    By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
driver.find_element(
    By.CSS_SELECTOR, "input[name=address").send_keys("Ленина, 55-3")
driver.find_element(
    By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
driver.find_element(
    By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
driver.find_element(
    By.CSS_SELECTOR, "input[name=zip-code]").send_keys("")
driver.find_element(
    By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
driver.find_element(
    By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
driver.find_element(
    By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
driver.find_element(
    By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

submit_button = driver.find_element(
        By.XPATH, '//button[text()="Submit"]').click()


zip_code_red = driver.find_element(By.CSS_SELECTOR, "#zip-code")
assert "alert-danger" in zip_code_red.get_attribute("class")

first_name_green = driver.find_element(By.CSS_SELECTOR, "#first-name")
assert "alert-success" in first_name_green.get_attribute("class")

last_name_green = driver.find_element(By.CSS_SELECTOR, "#last-name")
assert "alert-success" in last_name_green.get_attribute("class")

address_green = driver.find_element(By.CSS_SELECTOR, "#address")
assert "alert-success" in address_green.get_attribute("class")

city_green = driver.find_element(By.CSS_SELECTOR, "#city")
assert "alert-success" in city_green.get_attribute("class")

country_green = driver.find_element(By.CSS_SELECTOR, "#country")
assert "alert-success" in country_green.get_attribute("class")

email_green = driver.find_element(By.CSS_SELECTOR, "#e-mail")
assert "alert-success" in email_green.get_attribute("class")

phone_green = driver.find_element(By.CSS_SELECTOR, "#phone")
assert "alert-success" in phone_green.get_attribute("class")

job_green = driver.find_element(By.CSS_SELECTOR, "#job-position")
assert "alert-success" in job_green.get_attribute("class")

company_green = driver.find_element(By.CSS_SELECTOR, "#company")
assert "alert-success" in company_green.get_attribute("class")
