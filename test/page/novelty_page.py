import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configyration.config_provider import ConfigProvider


class NoveltyPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get_ui_url_novelty_page()
        self.__driver = driver
        self.__driver.get(self.__url)
        self.__driver.fullscreen_window()

    @allure.step("Добавить первую книгу в корзину")
    def add_book_from_novelty_page(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'picture.product-picture').click()
        self.__driver.find_element(By.CSS_SELECTOR, 'div.product-offer-header__buttons').click()
