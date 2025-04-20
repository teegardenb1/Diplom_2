from pythonProject.helpers_function.methods import Methods


class TestCreateUser(Methods):

    def test_create_created_user(self, get_test_data_and_return):
        test_data = get_test_data_and_return.copy()
        response = self.post_create_user(test_data)
        assert response == 403

    def test_create_user_without_field(self, get_test_data_and_return):
        test_data = get_test_data_and_return.copy()
        del test_data['password']
        response = self.post_create_user(test_data)
        assert response == 403

