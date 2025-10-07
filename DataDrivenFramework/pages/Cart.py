from playwright.sync_api import Page


class TestCart:
    def __init__(self, page:Page):
        self.page=page
        self.continue_shopping=page.get_by_role("button", name="Continue Shopping")
        self.buy_now=page.get_by_role("button", name="Buy Now")
        self.delete=page.locator("button.btn.btn-danger")
        self.checkout=page.get_by_role("button", name="Checkout")

    def clickingOnContinueSHopping(self):
        self.continue_shopping.click()

    def clickingOnBuyNow(self):
        self.buy_now.click()

    def clickingOnDelete(self):
        self.delete.click()

    def clickingOnCheckout(self):
        self.checkout.click()


