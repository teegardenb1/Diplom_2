from pythonProject.helpers_function.methods import Methods


class TestGetOrder(Methods):

    def test_get_order_auth_user(self, get_auth_token_and_return):
        auth_token = get_auth_token_and_return
        response = self.get_orders_auth_user(auth_token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    def test_get_order_not_auth_user(self):
        response = self.get_orders_not_auth_user()
        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == "You should be authorised"
