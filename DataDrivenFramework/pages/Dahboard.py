import re

from playwright.sync_api import Page

from DataDrivenFramework.pages.Base import BasePage
from practice.exception import add_to_cart


class Dashboard(BasePage):

    def __init__(self, page):

        super().__init__(page) #calling constructor of BasePage class
        self.cards=page.locator("div.card-body") # locate all 3 cards in dashboard
        self.search_box=page.get_by_placeholder("search")
        self.view=page.get_by_role("button", name="View") # locate all view buttons
        self.add_to_cart=page.get_by_role("button", name="Add To Cart") # all add to card buttons

    def get_product_count(self):
        self.page.wait_for_selector(".card-body")
        count=self.cards.count()
        return count

    def viewItem(self):
        self.cards.filter(has_text="ZARA COAT 3").locator("button:has-text('View')").click()
        heading = self.page.locator("h2", has_text="ZARA COAT 3")
        heading.wait_for(state="visible", timeout=5000)
        heading_text=heading.text_content().strip()
        assert heading_text.upper() == "ZARA COAT 3"
        print("view page loaded succesfully")
        self.home.click()

    def addCart(self):
        self.cards.filter(has_text="ADIDAS ORIGINAL").locator("button:has-text('Add To Cart')").click()
        self.page.wait_for_timeout(1000)
        cart_text = self.page.locator("button[routerlink='/dashboard/cart']").text_content().strip()
        cart_number = re.search(r"\d+", cart_text).group()  # finds "1"

        cart_count = int(cart_number)
        return cart_count

    def clickingOnCart(self):
        self.cart.click()

    def sigout(self):
        self.sign_out.click()
        toast=self.page.locator("#toast-container")
        toast.wait_for(state="visible")
        toast_text=toast.text_content().strip()
        assert toast_text=="Logged out successfully"
        print("user logged out")

    def orderClick(self):
        self.orders.click()
        header=self.page.locator("h1").text_content().strip()
        assert header=="Your Orders"
