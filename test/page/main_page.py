import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from configyration.config_provider import ConfigProvider


class MainPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get_ui_url_main_page()
        self.__driver = driver
        self.__driver.get(self.__url)
        self.__driver.fullscreen_window()

    @allure.step("Добавить cookie авторизации")
    def auth(self, cookie: dict) -> None:
        """
            Добавление cookie авторизации
        """
        self.__cookie = cookie
        self.__driver.add_cookie(self.__cookie)
        self.__driver.refresh()

    @allure.step("Кликнуть по кнопке войти")
    def authorization_click(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'button.header-profile__button').click()

    @allure.step("Ввести номер телефона")
    def say_number(self, number: str) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'input.phone-input__input').send_keys(number)

    @allure.step("Найти атрибут 'class' кнопки")
    def find_atribyte_button(self) -> None:
        return self.__driver.find_element(By.CSS_SELECTOR, 'button.app-button.auth-modal__sms-button.blue').get_attribute('class')

    @allure.step("Поиск по заданным тестовым данным")
    def search(self, query: str) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'input.header-search__input').send_keys(query)
        self.__driver.find_element(By.CSS_SELECTOR, 'input.header-search__input').send_keys(Keys.RETURN)

    @allure.step("Найти количество найденных книг")
    def total_book_search(self) -> int:
        return int(self.__driver.find_element(By.CSS_SELECTOR, 'span.search-categories-tree-item__count').text)

    @allure.step("Найти сообщение о том, что книг не найдено")
    def not_founded_search(self) -> str:
        return self.__driver.find_element(By.CSS_SELECTOR, 'h4.catalog-empty-result__header').text
