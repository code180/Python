from selenium.webdriver.common.by import By
import allure

@allure.severity("blocker")
@allure.epic('Получение итоговой суммы')
class TotalPrice:
    def __init__(self, driver):
        self.driver = driver

    @allure.title('shop_TotalPrice_skypro-1')
    @allure.description("Получаем итоговую стоимость")
    @allure.feature("float")
    def total(self):
        """
        Получаем итоговую стоимость(float)
        """
        result = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        total_price = result.strip().replace("Total: $", "")
        print(f"Общая сумма = ${total_price}")
        return total_price
