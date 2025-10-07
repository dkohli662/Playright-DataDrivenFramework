import pytest

from DataDrivenFramework.pages.Cart import Cart
from DataDrivenFramework.pages.Checkout import Checkout
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

# validating product count-card count

        dash_obj = Dashboard(page)
        product_count = dash_obj.get_product_count()
        assert product_count > 0
        print("card count is :", product_count)

        #clicking on card view
        dash_obj.viewItem()

 #add to cart
        cart_count=dash_obj.addCart()
        dash_obj.clickingOnCart()

#clicking on checkout

        obj_cart=Cart(page)
        obj_cart.clickingOnCheckout()


 #purchasing an item
        checkout_obj=Checkout(page)
        text=checkout_obj.itemPurchase()
        assert text =="Order Placed Successfully"
        print(text)

        # clicking on Orders tab and getting 1st row
        history_obj = OrderHistory(page)
        first_row=history_obj.getFirstRow()
        print("First row values:", first_row)



# clicking on view & getting thank you text
        message=history_obj.viewClick()
        assert "Thank you for Shopping With Us" in message
        print(message)

    else:
        error=page.locator("text=Enter Valid Email")
        page.wait_for_selector("text=Enter Valid Email")
        assert error.is_visible()