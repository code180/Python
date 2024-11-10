from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.severity("blocker")
@allure.epic('Добавить товары в корзину')
class AddToCart:

    def __init__(self, driver):
        self.driver = driver

    @allure.title('shop_skypro-1')
    @allure.description("Добавляем в корзину Sauce Labs Backpack")
    @allure.feature("")
    def add_Sauce_Labs_Backpack(self):
        """
        Добавляем в корзину Sauce Labs Backpack
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    @allure.title('shop_skypro-2')
    @allure.description("Добавляем в корзину Sauce Labs Bolt T-Shirt")
    @allure.feature("")
    def add_Sauce_Labs_Bolt_TShirt(self):
        """
        Добавляем в корзину Sauce Labs Bolt T-Shirt
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.title('shop_skypro-3')
    @allure.description("Добавляем в корзину Sauce Labs Onesie")
    @allure.feature("")
    def add_Sauce_Labs_Onesie(self):
        """
        Добавляем в корзину Sauce Labs Onesie
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.title('shop_skypro-4')
    @allure.description("Переходим в корзину и Нажмаем Checkout")
    @allure.feature("")
    def go_to_cart(self):
        """
        Переходим в корзину и Нажмаем Checkout
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
