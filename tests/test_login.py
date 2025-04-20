from pythonProject.helpers_function.methods import Methods


class TestLogin(Methods):

    def test_login_with_incorrect_password(self, get_test_data_and_return):
        test_data = get_test_data_and_return.copy()
        test_data['password'] = 'password2'
        response = self.post_login(test_data)
        assert response == 401

    def test_login_with_incorrect_login(self, get_test_data_and_return):
        test_data = get_test_data_and_return.copy()
        test_data["email"] = 'lunina1@yandex.ru'
        response = self.post_login(test_data)
        assert response == 401


