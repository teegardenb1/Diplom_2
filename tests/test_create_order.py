import pytest

from pythonProject.helpers_function.methods import Methods
from pythonProject.helpers_function.hashes import Hashes



class TestCreateOrder(Methods, Hashes):

    @pytest.mark.parametrize('order', [
        ([Hashes.bun_r2d3, Hashes.main_alpha]),
        ([Hashes.bun_n200i, Hashes.main_cheese, Hashes.sauce_spice_x]),
        ([Hashes.bun_r2d3, Hashes.main_alpha, Hashes.main_cheese, Hashes.sauce_space, Hashes.sauce_anaterian])
    ])
    def test_create_order_with_ingredients(self, order, get_auth_token_and_return):
        auth_token = get_auth_token_and_return
        response = self.post_create_order_with_auth(auth_token, order)
        assert response.status_code == 200
        assert response.json()['success'] == True

    def test_create_empty_order(self, get_auth_token_and_return):
        auth_token = get_auth_token_and_return
        response = self.post_create_order_with_auth(auth_token)
        assert response.status_code == 400
        assert response.json()['success'] == False
        assert response.json()['message'] == "Ingredient ids must be provided"

    def test_create_order_with_incorrect_hash(self, get_auth_token_and_return):
        auth_token = get_auth_token_and_return
        product = self.bad_hash_product
        response = self.post_create_order_with_auth(auth_token, product)
        assert response.status_code == 500

    @pytest.mark.parametrize('order', [
        ([Hashes.bun_r2d3, Hashes.main_alpha]),
        ([Hashes.bun_n200i, Hashes.main_cheese, Hashes.sauce_spice_x]),
        ([Hashes.bun_r2d3, Hashes.main_alpha, Hashes.main_cheese, Hashes.sauce_space, Hashes.sauce_anaterian])
    ])
    def test_create_order_without_auth(self, order):
        response = self.post_create_order_without_auth(order)
        assert response.status_code == 200





