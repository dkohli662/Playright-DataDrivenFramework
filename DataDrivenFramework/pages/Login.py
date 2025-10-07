from playwright.sync_api import Page


class LoginPage:
    # defining locators - variables
    def __init__(self, page:Page):
        self.page=page
        self.username="#userEmail" # locator for email using id
        self.password="#userPassword" # locator for password using id
        self.submit="#login"  # locator for submit using id

# performing action - methods
    def login(self, username, password):
        self.page.fill(self.username, username) # pass (selector, value)
        self.page.fill(self.password, password)
        self.page.click(self.submit)



