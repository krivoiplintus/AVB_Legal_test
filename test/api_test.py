import allure
import json
from page.company_api import CompanyApi
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider


base_url = ConfigProvider().get_api_base_url()
token = CompanyApi(base_url).authorization()["access"]




@allure.title("Изменение информации о пользователе")
@allure.epic("Пользователи")
def test_update_user_information():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    with open('avatar.json', 'r', encoding='utf-8') as f:
        avatar = json.load(f)
        return avatar
    first_name = "Владимир"
    middle_name = "Андреевич"
    last_name = "Андреев"
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
        assert result1["status"] == "successful"
    password = DataProvider().get("new_password")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        assert result2["status"] == "successful"


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
        assert result1["status"] == "successful"
    password = DataProvider().get("new_password1")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        assert result2["status"] == "successful"


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
        assert result1["status"] == "successful"
    password = DataProvider().get("new_password2")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        assert result2["status"] == "successful"


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
        assert result1["new_password"][0] == "Это поле не может быть пустым."


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
        assert result1["new_password"][0] == "Пароль должен содержать только латинские буквы и цифры."


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
        assert result1["new_password"][0] == "Пароль должен содержать только латинские буквы и цифры."


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
        assert result1["new_password"][0] == "Пароль должен содержать только латинские буквы и цифры."


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
        assert result1["new_password"][0] == "Пароль должен содержать только латинские буквы и цифры."


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
        assert result1["new_password"][0] == "Пароль должен содержать только латинские буквы и цифры."


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
        assert result1["status"] == "successful"
    password = DataProvider().get("new_password")
    new_passsword = DataProvider().get_password()
    resp2 = api.update_password(token, password, new_passsword)
    with allure.step("Проверить код ответа"):
        assert resp2.status_code == 200
    result2 = resp2.json()
    with allure.step("Проверить, что от сервера пришло сообщение об успешной смене пароля"):
        assert result2["status"] == "successful"
    

@allure.title("Восстановление пароля негативный")
@allure.description("Новый пароль пустой")
@allure.epic("Пользователи")
def test_recover_user_password_neg(code_recover):
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    new_password = DataProvider().get("password1")
    resp1 = api.recover_password(code_recover, new_password)
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 400
    result1 = resp1.json()
    with allure.step("Проверить, что от сервера пришло сообщение об ошибке"):
        assert result1["new_password"][0] == "Это поле не может быть пустым."


@allure.title("Обновление токена авторизации")
@allure.epic("Пользователи")
def test_update_token():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp1 = api.authorization()
    old_token = resp1["access"]
    refresh_token = resp1["refresh"]
    resp2 = api.refresh_token(refresh_token)
    new_token = resp2["access"]
    with allure.step("Проверить, что новый токен отличается от старого"):
        assert old_token != new_token


@allure.title("Получение списка тарифов")
@allure.epic("Тарифы")
def test_get_list_of_tariffs():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.get_list_of_tariffs(token)
    list = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить, что список не пустой"):
        assert list != None


@allure.title("Получение текста 'О нас'")
@allure.epic("Информация")
def test_get_info_about_us():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.get_info_about_us(token)
    result = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить тип информации"):
        assert result["type"] == "about us"
    with allure.step("Проверить заголовок"):
        assert result["title"] == "О нас"
    with allure.step("Проверить, что текст не пустой"):
        assert result["text"] != None


@allure.title("Получение контактов")
@allure.epic("Информация")
def test_get_info_contacts():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.get_info_contacts(token)
    result = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить тип информации email"):
        assert result[0]["type"] == "email"
    with allure.step("Проверить адрес электронной почты"):
        assert result[0]["contact"] == DataProvider().get("our_email")
    with allure.step("Проверить тип информации phone"):
        assert result[1]["type"] == "phone"
    with allure.step("Проверить номер телефона"):
        assert result[1]["contact"] == DataProvider().get("our_phone")


@allure.title("Получение ссылок на социальные сети")
@allure.epic("Информация")
def test_get_info_social_networks():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.get_info_social_networks(token)
    result = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить название соцсети 'Telegram'"):
        assert result[0]["title"] == "Telegram"
    with allure.step("Проверить ссылку на соцсеть"):
        assert result[0]["link"] == DataProvider().get("our_telegram")
    with allure.step("Проверить название соцсети 'VK'"):
        assert result[1]["title"] == "VK"
    with allure.step("Проверить ссылку на соцсеть"):
        assert result[1]["link"] == DataProvider().get("our_vk")


@allure.title("Получение документов")
@allure.epic("Информация")
def test_get_info_documents():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.get_info_documents(token)
    result = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить, что список документов не пустой"):
        assert len(result) != 0
    with allure.step("Проверить название документа 1"):
        assert result[0]["title"] == "Политика в отношении обработки файлов cookies"
    with allure.step("Проверить, что ссылка на документ не пустая"):
        assert result[0]["file"] != None
    with allure.step("Проверить название документа 2"):
        assert result[1]["title"] == "Политика обработки персональных данных"
    with allure.step("Проверить, что ссылка на документ не пустая"):
        assert result[1]["file"] != None
    with allure.step("Проверить название документа 3"):
        assert result[2]["title"] == "Договор оферты"
    with allure.step("Проверить, что ссылка на документ не пустая"):
        assert result[2]["file"] != None
    with allure.step("Проверить название документа 4"):
        assert result[3]["title"] == "Политика конфиденциальности"
    with allure.step("Проверить, что ссылка на документ не пустая"):
        assert result[3]["file"] != None
    with allure.step("Проверить название документа 5"):
        assert result[4]["title"] == "Пользовательское соглашение"
    with allure.step("Проверить, что ссылка на документ не пустая"):
        assert result[4]["file"] != None
    with allure.step("Проверить название документа 6"):
        assert result[5]["title"] == "Согласие на рекламную рассылку"
    with allure.step("Проверить, что ссылка на документ не пустая"):
        assert result[5]["file"] != None


@allure.title("Получение списка категорий")
@allure.epic("Правовые документы")
def test_get_legal_reference_book_list_of_categories():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.get_legal_reference_book_list_of_categories(token)
    list = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить, что список не пустой"):
        assert list != None


@allure.title("Получение категории по идентификатору")
@allure.epic("Правовые документы")
def test_get_legal_reference_book_category_by_id():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    category_id = DataProvider().getint("category_id")
    resp = api.get_legal_reference_book_category_by_id(token, category_id)
    result = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить, что id категории соответствует запрашиваемому"):
        assert result["id"] == category_id


@allure.title("Поиск документов по категории и ключевой фразе")
@allure.epic("Правовые документы")
def test_get_legal_reference_book_search_documents_by_category():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    category_id = DataProvider().getint("category_id1")
    search_data = "Об особенностях предоставления государственных услуг по регистрации транспортных средств"
    resp = api.get_legal_reference_book_search_documents_by_category(token, category_id, search_data)
    result = resp.json()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить, что id категории соответствует запрашиваемому"):
        assert result["results"][0]["category"]["id"] == category_id
    with allure.step("Проверить, что в названии присутствует запрашиваемая ключевая фраза"):
        name = result["results"][0]["name"]
        assert search_data in name
