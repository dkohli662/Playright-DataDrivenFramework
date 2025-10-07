import pytest

from DataDrivenFramework.pages.Cart import Cart
from DataDrivenFramework.pages.Checkout import Checkout
from DataDrivenFramework.pages.Dahboard import Dashboard

@pytest.mark.usefixtures("cart_ready_page")

def test_itemPurchase(cart_ready_page): # using fixture from conftest that return cart page
    page = cart_ready_page
    assert "cart" in page.url

    obj_cart=Cart(page)
    obj_cart.clickingOnCheckout()

    obj_checkout=Checkout(page)
    toast_message=obj_checkout.itemPurchase()
    assert toast_message=="Order Placed Successfully"
    print("Item purchase flow completed successfully!")




