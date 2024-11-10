from selenium.webdriver.common.by import By
from values import *
import allure

@allure.severity("blocker")
@allure.epic('форма')
class FillOutForm:

    @allure.title('form_skypro-1')
    @allure.description("Открываем страницу с формой")
    @allure.feature("")
    def __init__(self, driver):
        """
        Открываем страницу с формой
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    @allure.title('form_skypro-2')
    @allure.description("Заполняем форму значениями")
    @allure.feature("str")
    def add_value(self):
        """
        Заполняем форму значениями(str)
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=first-name]").send_keys(first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=last-name]").send_keys(last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=address]").send_keys(address)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=e-mail]").send_keys(email)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=phone]").send_keys(phone_number)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=city]").send_keys(city)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=country]").send_keys(country)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=job-position]").send_keys(
                job_position)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=company]").send_keys(company)

    @allure.title('form_skypro-3')
    @allure.description("Нажмаем кнопку Submit")
    @allure.feature("")
    def click_button(self):
        """
        Нажмаем кнопку Submit
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.title('form_skypro-4')
    @allure.description("Проверяем, что поле Zip code подсвечено красным")
    @allure.feature("")
    def zip_class(self):
        """
        Проверяем, что поле Zip code подсвечено красным
        """
        zip_class = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return zip_class

    @allure.title('form_skypro-5')
    @allure.description("Проверяем, что поле first_name подсвечено зеленым.")
    @allure.feature("")
    def first_name_class(self):
        """
        Проверяем, что поле first_name подсвечено зеленым.
        """
        first_name_class = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").get_attribute("class")
        return first_name_class

    @allure.title('form_skypro-6')
    @allure.description("Проверяем, что поле last_name подсвечено зеленым.")
    @allure.feature("")
    def last_name_class(self):
        """
        Проверяем, что поле last_name подсвечено зеленым.
        """
        last_name_class = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").get_attribute("class")
        return last_name_class

    @allure.title('form_skypro-7')
    @allure.description("Проверяем, что поле address подсвечено зеленым.")
    @allure.feature("")
    def address_class(self):
        """
        Проверяем, что поле address подсвечено зеленым.
        """
        address_class = self.driver.find_element(
            By.CSS_SELECTOR, "#address").get_attribute("class")
        return address_class

    @allure.title('form_skypro-8')
    @allure.description("Проверяем, что поле city подсвечено зеленым.")
    @allure.feature("")
    def city_class(self):
        """
        Проверяем, что поле city подсвечено зеленым.
        """
        city_class = self.driver.find_element(
            By.CSS_SELECTOR, "#city").get_attribute("class")
        return city_class

    @allure.title('form_skypro-9')
    @allure.description("Проверяем, что поле country подсвечено зеленым.")
    @allure.feature("")
    def country_class(self):
        """
        Проверяем, что поле country подсвечено зеленым.
        """
        country_class = self.driver.find_element(
            By.CSS_SELECTOR, "#country").get_attribute("class")
        return country_class

    @allure.title('form_skypro-10')
    @allure.description("Проверяем, что поле email подсвечено зеленым.")
    @allure.feature("")
    def email_class(self):
        """
        Проверяем, что поле email подсвечено зеленым.
        """
        email_class = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        return email_class

    @allure.title('form_skypro-11')
    @allure.description("Проверяем, что поле phone подсвечено зеленым.")
    @allure.feature("")
    def phone_class(self):
        """
        Проверяем, что поле phone подсвечено зеленым.
        """
        phone_class = self.driver.find_element(
            By.CSS_SELECTOR, "#phone").get_attribute("class")
        return phone_class

    @allure.title('form_skypro-12')
    @allure.description("Проверяем, что поле job_position подсвечено зеленым.")
    @allure.feature("")
    def job_position_class(self):
        """
        Проверяем, что поле job_position подсвечено зеленым.
        """
        job_position_class = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position").get_attribute("class")
        return job_position_class

    @allure.title('form_skypro-13')
    @allure.description("Проверяем, что поле company подсвечено зеленым.")
    @allure.feature("")
    def company_class(self):
        """
        Проверяем, что поле company подсвечено зеленым.
        """
        company_class = self.driver.find_element(
            By.CSS_SELECTOR, "#company").get_attribute("class")
        return company_class
