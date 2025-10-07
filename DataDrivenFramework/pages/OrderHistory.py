from playwright.sync_api import Page


class TestOrderHistory:
    def __init__(self, page:Page):
        self.page=page
        self.orders=page.get_by_role("button", name="ORDERS")


    def orderTable(self):
        headers=self.page.locator("thead th") # getting all headers/columns
        headers_count=headers.count()
        print("total headers are :", headers_count)

        header_texts=[]

        for i in range(headers_count):
            text=headers.nth(i).inner_text().strip()
            header_texts.append(text)
        return header_texts # returning list of clumns names

    def getFirstRow(self):
        self.orders.click()
        self.page.wait_for_selector("tbody tr") # wait to table get loaded

        rows=self.page.locator("tbody tr")
        assert rows.count()>0

        first_row=rows.nth(0)
        cells=first_row.locator("th, td")
        row_texts = cells.all_text_contents() # retrun list of string
        return row_texts

    def viewClick(self):
        rows=self.page.locator("tbody tr")
        first_row=rows.nth(0)

        view=first_row.locator("text=View")
        view.click()
        thank_you_text = self.page.locator("p:has-text('Thank you for Shopping With Us')")
        text_value = thank_you_text.inner_text().strip()
        return text_value














