import allure
import requests 
from test_data.data_provider import DataProvider


class CompanyApi:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        
    @allure.step("Получить код подтверждения для регистрации нового пользователя")
    def get_code_reg(self) -> dict:
        email = DataProvider().get_email()
        body = {
            "email": email,
            "target": "registration"
        }
        response = requests.post(self.base_url + "api/users/confirmation-code/", json=body)
        return response.json()

    @allure.step("Получить код подтверждения для восстановления пароля")
    def get_code_recover_password(self) -> dict:
        email = DataProvider().get_email()
        body = {
            "email": email,
            "target": "password_recovery"
        }
        response = requests.post(self.base_url + "api/users/confirmation-code/", json=body)
        return response.json()

    @allure.step("Регисрация")
    def registration(self, code_reg: int, email: str, password: str, first_name: str, middle_name: str, last_name: str) -> requests.Response:
        self.code_reg = code_reg
        self.email = email
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        body = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "email": self.email,
            "password": self.password,
            "theme": "light",
            "is_subscribed_to_newsletter": False,
            "code": self.code_reg           
        }
        responses = requests.post(self.base_url + "api/users/registration/", json=body)
        return responses

    @allure.step("Авторизация")
    def authorization(self) -> dict:
        self.email = DataProvider().get_email()
        self.password = DataProvider().get_password()
        body = {
            "email": self.email,
            "password": self.password
        }
        responses = requests.post(self.base_url + "api/users/login/", json=body)
        return responses.json()

    @allure.step("Обновление токена")
    def refresh_token(self, refresh: str) -> dict:
        self.refresh = refresh
        body = {
            "refresh": self.refresh
        }
        responses = requests.post(self.base_url + "api/users/refresh-token/", json=body)
        return responses.json()

    @allure.step("Получить информацию о пользователе")
    def get_user_information(self, token: str) -> dict:
        self.token = token
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        responses = requests.get(self.base_url + "api/users/me/", headers=headers)
        return responses.json()

    @allure.step("Обновить информацию о пользователе")
    def update_user_information(self, token: str, avatar: str, first_name: str, middle_name: str, last_name: str) -> requests.Response:
        self.token = token
        self.avatar = avatar
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
            "theme": "light",
            "is_subscribed_to_newsletter": False,
            "phone": ""
        }
        responses = requests.patch(self.base_url + "/api/users/me/", headers=headers, json=body)
        return responses


    @allure.step("Обновить пароль")
    def update_password(self, token: str, password: str, new_password: str) -> requests.Response:
        self.token = token
        self.password = password
        self.new_password = new_password
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "old_password": self.password,
            "new_password": self.new_password
        }
        responses = requests.post(self.base_url + "api/users/me/password/", json=body, headers=headers)
        return responses
    


    @allure.step("Восстановление пароля")
    def recover_password(self, code_recover: int, new_password: str) -> requests.Response:
        self.code_recover = code_recover
        self.new_password = new_password
        body = {
            "new_password": self.new_password,
            "code": self.code_recover
        }
        responses = requests.post(self.base_url + "api/users/password-recovery/", json=body)
        return responses
    