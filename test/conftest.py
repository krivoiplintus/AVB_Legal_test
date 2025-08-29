import allure
import pytest
from selenium import webdriver
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider
from page.company_api import CompanyApi


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(ConfigProvider().get_ui_timeout())
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def token():
    with allure.step("Получить токен авторизации"):
        base_url = ConfigProvider().get_api_base_url()
        token = CompanyApi(base_url).authorization()["access"]
        yield token

@pytest.fixture
def code_reg():
    with allure.step("Получить код подтверждения регистрации"):
        base_url = ConfigProvider().get_api_base_url()
        code_reg = CompanyApi(base_url).get_code_reg()["code"]
        yield code_reg

@pytest.fixture
def code_recover():
    with allure.step("Получить код подтверждения восстановления пароля"):
        base_url = ConfigProvider().get_api_base_url()
        code_recover = CompanyApi(base_url).get_code_recover_password()["code"]
        yield code_recover
