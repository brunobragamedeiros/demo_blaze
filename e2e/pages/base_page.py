from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page
        self.sign_up_link = page.get_by_role("link", name="Sign up")
        self.log_in_link = page.get_by_role("link", name="Log in")
        self.log_out_link = page.get_by_role("link", name="Log out")
        self.sign_up_username =  page.get_by_role("textbox", name="Username:")
        self.sign_up_password = page.get_by_role("textbox", name="Password:")
        self.sign_up_button = page.get_by_role("button", name="Sign up")
        self.log_in_button = page.get_by_role("button", name="Log in")
        self.log_in_username = page.locator("#loginusername")
        self.log_in_password = page.locator("#loginpassword")     

    def validate_page_header(self, pageTitle):
        expect(self.page.get_by_role("heading", name=pageTitle)).to_be_visible()

    def login_as_new_user(self, generated_username, generated_password):
        self.sign_up_link.click()
        self.sign_up_username.fill(generated_username)
        self.sign_up_password.fill(generated_password)
        self.sign_up_button.click()
        self.log_in_link.click()        
        self.log_in_username.fill(generated_username)
        self.log_in_password.fill(generated_password)
        self.log_in_button.click()
        expect(self.page.get_by_role("link", name=f'Welcome {generated_username}')).to_be_visible()

    def logout(self):
        self.log_out_link.click()
        expect(self.log_in_link).to_be_visible()