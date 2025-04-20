import pytest
import allure

from helpers_function.methods import Methods


@allure.step("Создание пользователя для теста")
@pytest.fixture(scope="session", params=[{"email" : 'lunina@yandex.ru',
                                           "password" : 'password',
                                           "name" : "anastasiya"}])
def create_user_and_return_data(request):
    data = request.param
    actions = Methods()
    response = actions.post_create_user(data)
    with allure.step('Cоздание уникального пользователя'):
        assert response.status_code == 200, 'Пользователь уже существует'

    login_data = {"email" : data['email'], "password" : data["password"]}
    auth_token, refresh_token = actions.post_login(login_data)
    yield {"data" : data, "auth_token" : auth_token, "refresh_token" : refresh_token}
    actions.delete_user(auth_token)

@allure.step('Полученние данных о пользователе')
@pytest.fixture
def get_test_data_and_return(create_user_and_return_data):
    data = create_user_and_return_data["data"]
    return data

@allure.step('Получение auth_token для теста')
@pytest.fixture
def get_auth_token_and_return(create_user_and_return_data):
    auth_token = create_user_and_return_data['auth_token']
    return auth_token

@allure.step('Создание дополнительного пользователя')
@pytest.fixture(params=[{"email" : 'somewho@yandex.ru',
                        "password" : 'password',
                        "name" : "somewho"}])
def create_additional_user_and_return_data(request):
    data = request.param
    actions = Methods()
    actions.post_create_user(data)
    login_data = {"email": data['email'], "password": data["password"]}
    auth_token, refresh_token = actions.post_login(login_data)
    yield {"data": data, "auth_token": auth_token, "refresh_token": refresh_token}
    actions.delete_user(auth_token)







