from pages.home_page import HomePage
from pages.product_page import ProductPage

class ShoppingFlow:
    def __init__(self, page):
        self.page = page
        self.home_page = HomePage(page)
        self.product_page = ProductPage(page)

    def send_product_to_cart(self, product_name):
        self.home_page.open_home_page()
        self.home_page.open_item_by_product_name(product_name)
        self.product_page.add_item()
