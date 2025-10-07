from playwright.sync_api import Page, expect


class Checkout:
    def __init__(self, page:Page):
        self.page=page
        self.country_input = page.locator("input[placeholder='Select Country']")
        self.place_order = page.locator("a.btnn.action__submit")

    def itemPurchase(self):
        expect(self.country_input).to_be_visible(timeout=10000)

        self.country_input.type("India", delay=200)
        self.page.wait_for_selector("section.ta-results button.ta-item", timeout=10000)
        items=self.page.locator("section.ta-results button.ta-item")
        print("Totoal items are :", items.count())

        items.nth(1).click()

        self.page.wait_for_timeout(500)
        self.place_order.click()
        toast=self.page.locator("#toast-container")
        toast.wait_for(state="visible", timeout=10000)
        return toast.inner_text().strip()

