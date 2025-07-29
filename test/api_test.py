import allure
import json
from page.company_api import CompanyApi
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider


base_url = ConfigProvider().get_api_base_url()
#token = CompanyApi(base_url).authorization()["access"]


@allure.title("Регистрация нового пользователя")
@allure.epic("Пользователи")
def test_reg(code_reg):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    email = DataProvider().get_email()
    password = DataProvider().get_password()
    first_name = DataProvider().get("first_name")
    middle_name = DataProvider().get("middle_name")
    last_name = DataProvider().get("last_name")
    resp = api.registration(code_reg, email, password, first_name, middle_name, last_name)
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 201
    with allure.step("Проверить, что emale в теле ответа соответстует указанному при регистрации"):
        assert resp.json()["email"] == DataProvider().get_email()
    avatar_url = resp.json()["avatar"]
    data_to_save = {"avatar": avatar_url}
    with open("test_data.test_data.json", "w") as f:
        json.dump(data_to_save, f, indent=4)


@allure.title("Изменение информации о пользователе")
@allure.epic("Пользователи")
def test_update_user_information(token):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    avatar = DataProvider().get("avatar")
    first_name = DataProvider().get("new_first_name")
    middle_name = DataProvider().get("new_middle_name")
    last_name = DataProvider().get("new_last_name")
    resp = api.update_user_information(token, avatar, first_name, middle_name, last_name)
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    result = api.get_user_information(token)
    with allure.step("Проверить, что имя пользователя изменилось"):
        assert result["first_name"] == DataProvider().get("new_first_name")
    with allure.step("Проверить, что отчество пользователя изменилось"):
        assert result["middle_name"] == DataProvider().get("new_middle_name")
    with allure.step("Проверить, что фамилия пользователя изменилась"):
        assert result["last_name"] == DataProvider().get("new_last_name")




@allure.title("Изменение пароля")
@allure.epic("Пользователи")
def test_update_user_password(token):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("new_password")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 200
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result1["status"] == "successful"
    password = DataProvider().get("new_password")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result2["status"] == "successful"


@allure.title("Изменение пароля, негативный новый пароль пустой")
@allure.epic("Пользователи")
def test_update_user_password_neg(token):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("password1")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        result1["new_password"][0] == "Это поле не может быть пустым."
    
 

@allure.title("Восстановление пароля")
@allure.epic("Пользователи")
def test_recover_user_password(code_recover, token):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    new_password = DataProvider().get("new_password")
    resp1 = api.recover_password(code_recover, new_password)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 200
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result1["status"] == "successful"
    password = DataProvider().get("new_password")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result2["status"] == "successful"
    


