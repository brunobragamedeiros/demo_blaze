from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page) 
        self.page = page
        self.home_link = page.get_by_role("link", name = "Home")
        self.product_name = page.get_by_role("link")

    def open_item_by_product_name(self, product_name):
        self.product_name.filter(has_text = product_name).click()

    def open_home_page(self):
        expect(self.home_link).to_be_visible()
        self.home_link.click()