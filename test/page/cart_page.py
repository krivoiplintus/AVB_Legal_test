import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configyration.config_provider import ConfigProvider


class CartPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get_ui_url_cart_page()
        self.__driver = driver
        self.__driver.get(self.__url)
        self.__driver.fullscreen_window()

    @allure.step("Узнать количество товаров в корзине")
    def total_book_in_cart(self) -> str:
        return self.__driver.find_element(By.CSS_SELECTOR, 'div.info-item__title').text

    @allure.step("Очистить корзину")
    def clear_cart(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'div.delete-many').click()

    @allure.step("Удалить книгу")
    def delete_book(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'button.button.cart-item__actions-button.cart-item__actions-button--delete.light-blue').click()
        self.__driver.implicitly_wait(60)

    @allure.step("Проверить, что корзина пуста")
    def empty_cart(self) -> str:
        return self.__driver.find_element(By.CSS_SELECTOR, 'div.empty-title').text
