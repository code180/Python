from selenium.webdriver.common.by import By
from shop_values import *
import allure

@allure.severity("blocker")
@allure.epic('Авторизация')
class Authorization():

    @allure.title('shop_auto_skypro-1')
    @allure.description("Открываем страницу магазина")
    @allure.feature("")
    def __init__(self, driver):
        """
        Открываем страницу магазина
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    @allure.title('shop_auto_skypro-2')
    @allure.description("Авторизируемся")
    @allure.feature("str")
    def add_values(self):
        """
        Авторизируемся(str)
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
