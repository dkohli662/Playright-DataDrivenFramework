import pytest

from DataDrivenFramework.pages.Cart import TestCart
from DataDrivenFramework.pages.Checkout import TestCheckout
from DataDrivenFramework.pages.Dahboard import TestDashboard

@pytest.mark.usefixtures("cart_ready_page")

def test_itemPurchase(cart_ready_page): # using fixture from conftest that return cart page
    page = cart_ready_page
    assert "cart" in page.url

    obj_cart=TestCart(page)
    obj_cart.clickingOnCheckout()

    obj_checkout=TestCheckout(page)
    toast_message=obj_checkout.itemPurchase()
    assert toast_message=="Order Placed Successfully"
    print("Item purchase flow completed successfully!")




