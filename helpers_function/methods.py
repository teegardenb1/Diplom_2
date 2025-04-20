import requests
import allure
from urls.urls import Urls


class Methods(Urls):

    @allure.step('Получение информации о пользователе')
    def get_info_about_user(self, auth_token=None):
        headers = {"Authorization": auth_token}
        response = requests.get(self.user_info, headers=headers)
        return response

    @allure.step('Получение заказов авторизованного пользователя')
    def get_orders_auth_user(self, auth_token):
        headers = {"Authorization": auth_token}
        response = requests.get(self.orders, headers=headers)
        return response

    @allure.step('Получение заказов неавторизованного пользователя')
    def get_orders_not_auth_user(self):
        response = requests.get(self.orders)
        return response

    @allure.step('Создание пользователя')
    def post_create_user(self, data):
        response = requests.post(self.create_user, data=data)
        return response.status_code

    @allure.step('Вход под пользователем')
    def post_login(self, data):
        response = requests.post(self.login, data=data)
        if response.status_code == 200:
            json_response = response.json()
            auth_token = json_response['accessToken']
            refresh_token = json_response['refreshToken']
            return auth_token, refresh_token

        else:
            return response.status_code

    @allure.step('Выход из под пользователя')
    def post_logout(self, login_user_and_get_tokens):
        data = {"token" : login_user_and_get_tokens.refresh_token}
        print(data)
        response = requests.post(self.logout, data)
        return response

    @allure.step('Смена name у пользователя')
    def patch_update_user_name(self, new_name, auth_token=None):
        headers = {"Authorization": auth_token}
        data = {"name" : new_name}
        response = requests.patch(self.user_info, headers=headers, data=data)
        return response

    @allure.step('Смена email у пользователя')
    def patch_update_email(self, new_email, auth_token=None):
        headers = {"Authorization": auth_token}
        data = {"email" : new_email}
        response = requests.patch(self.user_info, headers=headers, data=data)
        return response

    @allure.step('Создание заказа под авторизованным пользователем')
    def post_create_order_with_auth(self, auth_token, order=None):
        headers = {"Authorization": auth_token}
        data = {'ingredients' : [order]}
        response = requests.post(self.orders, headers=headers, data=data)
        return response

    @allure.step('Создание заказа под неавторизованным пользователем')
    def post_create_order_without_auth(self, order=None):
        data = {'ingredients' : [order]}
        response = requests.post(self.orders, data=data)
        return response

    @allure.step('Удаление пользователя')
    def delete_user(self, auth_token):
        headers = {"Authorization" : auth_token}
        response = requests.delete(self.user_info, headers=headers)
        return response

