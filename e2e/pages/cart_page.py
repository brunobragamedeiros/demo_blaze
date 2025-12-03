from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.cart_link = page.get_by_role("link", name="Cart", exact=True)
        self.product_information = page.get_by_role("cell")
        self.cart_total = page.locator('#totalp')

    def open_cart(self):
        self.cart_link.click()

    def validate_product_in_cart(self, product_name, product_price):
        product = self.product_information.filter(has_text = product_name)
        row = product.locator("..") 
        price = row.get_by_text(product_price)
        expect(product).to_be_visible()        
        expect(price).to_be_visible()   

    def delete_product(self, product_name):
        product = self.product_information.filter(has_text = product_name)
        row = product.locator("..") 
        delete_link = row.get_by_text("Delete")
        delete_link.click()

    def validate_product_not_in_cart(self, product_name, product_price):
        expect(self.product_information.filter(has_text = product_name)).not_to_be_visible()        
        expect(self.product_information.filter(has_text = product_price)).not_to_be_visible()

    def validate_total(self, total_count):
        expect(self.cart_total.filter(has_text = total_count)).to_be_visible()