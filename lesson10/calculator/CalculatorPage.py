from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.severity("blocker")
@allure.epic('Калькулятор')
class Calculator:

    @allure.title('Calculator_skypro-1')
    @allure.description("Открывает страницу с калькулятором")
    @allure.feature("")
    def __init__(self, driver):
        """
        Открывает страницу с калькулятором
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    @allure.title('Calculator_skypro-2')
    @allure.description("Вводим время задержки выполнения функции")
    @allure.feature("")
    def change_time(self):
        """
        Вводим время задержки выполнения функции(45)
        """
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(45)

    @allure.title('Calculator_skypro-3')
    @allure.description("Нажмаем на кнопку 7")
    @allure.feature("")
    def click_7(self):
        """
        Нажмаем на кнопку 7
        """
        self.driver.find_element(
            By.XPATH, '//*[@title="calculator"]/div[2]/span[1]').click()

    @allure.title('Calculator_skypro-4')
    @allure.description("Нажмаем на кнопку +")
    @allure.feature("")
    def click_plus(self):
        """
        Нажмаем на кнопку +
        """
        self.driver.find_element(
            By.XPATH, '//*[@title="calculator"]/div[2]/span[4]').click()

    @allure.title('Calculator_skypro-5')
    @allure.description("Нажмаем на кнопку 8")
    @allure.feature("")
    def click_8(self):
        """
        Нажмаем на кнопку 8
        """
        self.driver.find_element(
            By.XPATH, '//*[@title="calculator"]/div[2]/span[2]').click()

    @allure.title('Calculator_skypro-6')
    @allure.description("Нажмаем на кнопку =")
    @allure.feature("")
    def click_equals(self):
        """
        Нажмаем на кнопку =
        """
        self.driver.find_element(
            By.XPATH, '//*[@title="calculator"]/div[2]/span[15]').click()

    @allure.title('Calculator_skypro-7')
    @allure.description("функция ожидающая результат")
    @allure.feature("")
    def wait(self):
        """
        функция ожидающая результат
        """
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, "div.screen"), "15"))

    @allure.title('Calculator_skypro-8')
    @allure.description("Получение результата")
    @allure.feature("Возвращается целое число")
    def result(self):
        """
        Получение результата
        (Возвращается целое число)
        """
        result = self.driver.find_element(
            By.CSS_SELECTOR, "div.screen").text
        return int(result)
