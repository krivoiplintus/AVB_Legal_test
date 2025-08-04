import allure
from page.company_api import CompanyApi
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider


base_url = ConfigProvider().get_api_base_url()
#token = CompanyApi(base_url).authorization()["access"]
token = ConfigProvider().get_api_token()



@allure.title("Изменение информации о пользователе")
@allure.epic("Пользователи")
def test_update_user_information():
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
@allure.description("Новый пароль 8 символов, латиница минимум один символ в верхнем регистре, один символ в нижнем регистре, одна цифра")
@allure.epic("Пользователи")
def test_update_user_password():
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


@allure.title("Изменение пароля 1")
@allure.description("Новый пароль 50 символов, латиница минимум один символ в верхнем регистре, один символ в нижнем регистре, одна цифра")
@allure.epic("Пользователи")
def test_update_user_password1():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("new_password1")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 200
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result1["status"] == "successful"
    password = DataProvider().get("new_password1")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result2["status"] == "successful"


@allure.title("Изменение пароля 2")
@allure.description("Пробел перед новым паролем")
@allure.epic("Пользователи")
def test_update_user_password1():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("new_password2")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 200
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result1["status"] == "successful"
    password = DataProvider().get("new_password2")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        result2["status"] == "successful"


@allure.title("Изменение пароля, негативный 1")
@allure.description("Новый пароль пустой")
@allure.epic("Пользователи")
def test_update_user_password_neg1():
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


@allure.title("Изменение пароля, негативный 2")
@allure.description("Тире перед, в середине и после нового пароля")
@allure.epic("Пользователи")
def test_update_user_password_neg2():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("password2")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        result1["new_password"][0] == "Это поле не может быть пустым."


@allure.title("Изменение пароля, негативный 3")
@allure.description("В новом пароле присутствуют спецсимволы")
@allure.epic("Пользователи")
def test_update_user_password_neg3():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("password3")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        result1["new_password"][0] == "Это поле не может быть пустым."


@allure.title("Изменение пароля, негативный 4")
@allure.description("Новый пароль на кирилице")
@allure.epic("Пользователи")
def test_update_user_password_neg4():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("password4")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        result1["new_password"][0] == "Это поле не может быть пустым."


@allure.title("Изменение пароля, негативный 5")
@allure.description("Новый пароль состоит из символов других языков")
@allure.epic("Пользователи")
def test_update_user_password_neg5():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("password5")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        result1["new_password"][0] == "Это поле не может быть пустым."


@allure.title("Изменение пароля, негативный 6")
@allure.description("Новый пароль с пробелом внутри текста")
@allure.epic("Пользователи")
def test_update_user_password_neg6():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    password = DataProvider().get_password()
    new_passsword = DataProvider().get("password6")
    resp1 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        result1["new_password"][0] == "Это поле не может быть пустым."


@allure.title("Восстановление пароля")
@allure.epic("Пользователи")
def test_recover_user_password(code_recover):
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
    


