import allure
import pytest
import json
from page.company_api import CompanyApi
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider


base_url = ConfigProvider().get_api_base_url()



@allure.title("Регистрация нового пользователя, негативный 1")
@allure.description("Не указаны личные данные и пароль")
@allure.epic("Пользователи")
def test_reg_neg1(code_reg):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    email = DataProvider().get_email()
    password = DataProvider().get("password1")
    first_name = DataProvider().get("first_name1")
    middle_name = DataProvider().get("middle_name1")
    last_name = DataProvider().get("last_name1")
    resp2 = api.registration(code_reg, email, password, first_name, middle_name, last_name)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 400
    with allure.step("Проверить, что emale в теле ответа присутствуют сообщения об ошибке"):
        assert resp2.json()["first_name"][0] == "Это поле не может быть пустым."
        assert resp2.json()["last_name"][0] == "Это поле не может быть пустым."
        assert resp2.json()["password"][0] == "Это поле не может быть пустым."


@allure.title("Регистрация нового пользователя, негативный 2")
@allure.description("Личные данные указаны на латинице, пароль на кирилице")
@allure.epic("Пользователи")
def test_reg_neg2(code_reg):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    email = DataProvider().get_email()
    password = DataProvider().get("password2")
    first_name = DataProvider().get("first_name2")
    middle_name = DataProvider().get("middle_name2")
    last_name = DataProvider().get("last_name2")
    resp2 = api.registration(code_reg, email, password, first_name, middle_name, last_name)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 400
    with allure.step("Проверить, что emale в теле ответа присутствуют сообщения об ошибке"):
        assert resp2.json()["first_name"][0] == "Должно содержать только кириллические буквы, символ дефиса, символ пробела."
        assert resp2.json()["middle_name"][0] == "Должно содержать только кириллические буквы и символ дефиса."
        assert resp2.json()["last_name"][0] == "Должно содержать только кириллические буквы, символ дефиса, символ пробела."


@allure.title("Регистрация нового пользователя, негативный 3")
@allure.description("Личные данные указаны на кирилице, количество символов меньше минимального значения")
@allure.epic("Пользователи")
def test_reg_neg3(code_reg):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    email = DataProvider().get("email1")
    password = DataProvider().get("password3")
    first_name = DataProvider().get("first_name3")
    middle_name = DataProvider().get("middle_name3")
    last_name = DataProvider().get("last_name3")
    resp2 = api.registration(code_reg, email, password, first_name, middle_name, last_name)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 400
    with allure.step("Проверить, что emale в теле ответа присутствуют сообщения об ошибке"):
        assert resp2.json()["first_name"][0] == "Должно содержать только кириллические буквы, символ дефиса, символ пробела."
        assert resp2.json()["middle_name"][0] == "Должно содержать только кириллические буквы и символ дефиса."
        assert resp2.json()["last_name"][0] == "Должно содержать только кириллические буквы, символ дефиса, символ пробела."


@allure.title("Регистрация нового пользователя")
@allure.epic("Пользователи")
def test_reg(code_reg):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    email = DataProvider().get_email()
    password = DataProvider().get_password()
    first_name = "Андрей"
    middle_name = "Владимирович"
    last_name = "Владимиров"
    resp = api.registration(code_reg, email, password, first_name, middle_name, last_name)
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 201
    with allure.step("Проверить, что emale в теле ответа соответстует указанному при регистрации"):
        assert resp.json()["email"] == DataProvider().get_email()
    avatar_url = resp.json()["avatar"]
    data_to_save = {"avatar": avatar_url}
    with open("test_data.test_data.json", "w") as f:
        json.dump(data_to_save, f, indent=4)
