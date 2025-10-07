from playwright.sync_api import Page


class BasePage:
    def __init__(self, page:Page):
        self.page=page
        self.home=page.get_by_role("button", name=" HOME")
        self.orders=page.get_by_role("button", name="ORDERS")
        self.cart=page.locator("button[routerlink='/dashboard/cart']")
        self.sign_out=page.get_by_role("button", name="Sign Out")

# common methods
    def go_to_home(self):
        self.home.click()

    def go_to_order(self):
        self.orders.click()

    def go_to_cart(self):
        self.cart.click()

    def sigout(self):
        self.sign_out.click()


