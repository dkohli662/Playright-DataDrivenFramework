from DataDrivenFramework.pages.Base import TestBasePage


def test_headerClicks(logged_in_context): # using logged_in_context fixture for login
    page = logged_in_context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    print("Current URL:", page.url)

#clicking on Orders
    base_obj=TestBasePage(page)
    base_obj.go_to_order()
    assert "https://rahulshettyacademy.com/client/#/dashboard/myorders" in page.url
    print("reached to orders tab:", page.url)

#clicking on cart
    base_obj.go_to_cart()
    assert "https://rahulshettyacademy.com/client/#/dashboard/cart" in page.url
    print("reached to cart page :", page.url)
#signing out
    base_obj.sigout()
    page.wait_for_url("https://rahulshettyacademy.com/client/#/auth/login")  # ✅ waits until login page is reached

    assert "https://rahulshettyacademy.com/client/#/auth/login" in page.url
    print("logged out succesfully:", page.url)









