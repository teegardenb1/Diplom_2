class Urls:

    base = "https://stellarburgers.nomoreparties.site/api/"
    ingredients = base + "ingredients"
    orders = base + "orders"
    reset_password = base + "password-reset"
    set_new_password_in_reset = reset_password + "/reset"
    create_user = base + "auth/register"
    login = base + "auth/login"
    logout = base + "auth/logout"
    new_token = base + "auth/token"
    user_info = base + "auth/user"
    update_user = user_info
    all_orders = orders + "all"
