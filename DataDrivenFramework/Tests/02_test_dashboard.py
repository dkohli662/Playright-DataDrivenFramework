from DataDrivenFramework.pages.Login import LoginPage
from DataDrivenFramework.pages.Dahboard import Dashboard



def test_dashboard(logged_in_context): # using fixture from conftest for login in
    page = logged_in_context.new_page()

    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    print("Current URL:", page.url)
    assert "https://rahulshettyacademy.com/client/#/dashboard/dash" in page.url


    obj_dash=Dashboard(page)
    product_count=obj_dash.get_product_count() # get product count method is called from dashboard page class
    assert product_count > 0
    print("card count is :", product_count)

    obj_dash.viewItem()

    cart_count=obj_dash.addCart()

    print("cart count is :", cart_count)




