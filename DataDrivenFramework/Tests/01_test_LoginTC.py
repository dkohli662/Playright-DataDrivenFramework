import pytest
from ..Utils.config import load_credentials

from DataDrivenFramework.pages.Login import LoginPage
from ..pages.Dahboard import Dashboard
from ..pages.OrderHistory import OrderHistory

# Load all credentials
creds_data = load_credentials() # calling method load_credentials which is in config file

@pytest.mark.parametrize("user_type", creds_data.keys()) # user_type name of variable can be any
def test_validateLogin(page, user_type):
    list = creds_data[user_type]
    email=list['username']
    psw=list['password']

    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    login_page = LoginPage(page)
    login_page.login(email, psw)


    if user_type == "valid_user":
        page.wait_for_url("https://rahulshettyacademy.com/client/#/dashboard/dash", timeout=10000)
        assert "https://rahulshettyacademy.com/client/#/dashboard/dash" in page.url

    else:
        error=page.locator("text=Enter Valid Email")
        page.wait_for_selector("text=Enter Valid Email")
        assert error.is_visible()









