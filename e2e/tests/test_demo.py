from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from flows.shopping_flow import ShoppingFlow


def test_add_item_to_the_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    product = "Iphone 6 32gb"

    page.goto('/')
    home_page.open_item_by_product_name(product)
    product_page.validate_page_header(product)
    product_page.add_item()

def test_product_information_in_cart(page, login_random):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    product = "Iphone 6 32gb"
    price = "790"

    page.goto('/')
    home_page.open_item_by_product_name(product)
    product_page.valida_product_information(product, price)
    product_page.add_item()
    cart_page.open_cart()
    cart_page.validate_product_in_cart(product, price) 

def test_product_deletion_in_cart(page):
    cart_page = CartPage(page)
    shopping_flow = ShoppingFlow(page)
    product_1 = "Iphone 6 32gb"
    price_1 = "790"
    product_2 = "Sony xperia z5"
    price_2 = "320"

    page.goto('/')
    shopping_flow.send_product_to_cart(product_1)
    shopping_flow.send_product_to_cart(product_2)
    cart_page.open_cart()
    cart_page.validate_product_in_cart(product_1, price_1)
    cart_page.validate_product_in_cart(product_2, price_2)
    cart_page.delete_product(product_1)
    cart_page.validate_product_not_in_cart(product_1, price_1)
    cart_page.validate_product_in_cart(product_2, price_2)

def test_total_cart(page):
    cart_page = CartPage(page)
    shopping_flow = ShoppingFlow(page)
    product_1 = "Iphone 6 32gb"
    price_1 = 790
    product_2 = "Sony xperia z5"
    price_2 = 320
    total = price_1 + price_2

    page.goto('/')
    shopping_flow.send_product_to_cart(product_1)
    shopping_flow.send_product_to_cart(product_2)
    cart_page.open_cart()
    cart_page.validate_total(str(total))
    cart_page.delete_product(product_1)
    cart_page.validate_total(str(price_2))

def test_log_out(page, login_random):
    home_page = HomePage(page)
    home_page.logout()