import allure
import pytest
from helpers_function.methods import Methods

allure.story('Изменение данных пользователя')
class TestChangeUserData(Methods):

    @allure.title('Получение информации о пользователе с авторизацией ')
    def test_get_user_data_with_auth(self, get_test_data_and_return, get_auth_token_and_return):
        test_data = get_test_data_and_return.copy()
        del test_data['password']
        auth_token = get_auth_token_and_return
        response = self.get_info_about_user(auth_token)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'] == test_data

    @allure.title('Изменение имени пользователя с авторизацией ')
    @pytest.mark.parametrize('new_name', ['lunina1', 'somename', 'nobody'])
    def test_change_user_name_with_auth(self, get_test_data_and_return, get_auth_token_and_return, new_name):
        test_data_before_change = get_test_data_and_return.copy()
        del test_data_before_change['password']
        auth_token = get_auth_token_and_return
        response = self.patch_update_user_name(new_name, auth_token)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'] != test_data_before_change

    @allure.title('Изменение email пользователя на неиспользуемый email, с авторизацией ')
    @pytest.mark.parametrize('new_email', ['lunina1@yandex.ru', 'somename@yandex.ru', 'nobody@yandex.ru'])
    def test_change_user_email_to_unused_with_auth(self, get_test_data_and_return, get_auth_token_and_return, new_email):
        test_data_before_change = get_test_data_and_return.copy()
        del test_data_before_change['password']
        auth_token = get_auth_token_and_return
        response = self.patch_update_email(new_email, auth_token)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'] != test_data_before_change

    @allure.title('Изменение email пользователя на используемый, с авторизацией ')
    def test_change_user_email_to_a_used_with_auth(self, get_test_data_and_return,
                                         get_auth_token_and_return,
                                         create_additional_user_and_return_data):
        test_data_before_change = get_test_data_and_return.copy()
        del test_data_before_change['password']
        auth_token = get_auth_token_and_return
        second_user_data = create_additional_user_and_return_data['data'].copy()
        response = self.patch_update_email(second_user_data['email'], auth_token)

        assert response.status_code == 403
        assert response.json()['success'] == False
        assert response.json()['message'] == 'User with such email already exists'
        response_back = self.patch_update_email(test_data_before_change['email'], auth_token)
        assert response_back.status_code == 200
        assert response_back.json()['success'] == True

    @allure.title('Получение информации о пользователе без авторизации')
    def test_get_user_data_without_auth(self, get_test_data_and_return):
        test_data = get_test_data_and_return.copy()
        del test_data['password']
        response = self.get_info_about_user()

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == "You should be authorised"

    @allure.title('Изменение имени пользователя без авторизации')
    @pytest.mark.parametrize('new_name', ['lunina1', 'somename', 'nobody'])
    def test_change_user_name_without_auth(self, get_test_data_and_return, new_name):
        test_data_before_change = get_test_data_and_return.copy()
        del test_data_before_change['password']
        response = self.patch_update_user_name(new_name)

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == "You should be authorised"

    @allure.title('Изменение email на неиспользуемый, без авторизации')
    @pytest.mark.parametrize('new_email', ['lunina1@yandex.ru', 'somename@yandex.ru', 'nobody@yandex.ru'])
    def test_change_user_email_to_unused_without_auth(self, get_test_data_and_return, new_email):
        test_data_before_change = get_test_data_and_return.copy()
        del test_data_before_change['password']
        response = self.patch_update_email(new_email)

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == "You should be authorised"

