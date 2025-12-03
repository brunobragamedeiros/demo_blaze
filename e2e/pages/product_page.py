from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.add_to_cart_link = page.get_by_role("link", name="Add to cart")
        self.product_info = page.get_by_role("heading")

    def add_item(self):
        self.wait_dialog()
        self.add_to_cart_link.click()
        self.page.wait_for_timeout(1000)

    def valida_product_information(self, product_name, price):
        expect(self.product_info.filter(has_text = product_name)).to_be_visible()
        expect(self.product_info.filter(has_text = f"${price} *includes tax")).to_be_visible()

    def wait_dialog(self):
        def handle_dialog(dialog):
            assert "Product added" in dialog.message
            dialog.accept() 
  
        self.page.on("dialog", handle_dialog)