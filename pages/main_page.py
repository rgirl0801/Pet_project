from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    B_CAROUSEL_NEXT = (
        By.XPATH, "//*[@id='carouselExampleIndicators']/a[2]/span[1]")
    B_CAROUSEL_PREV = (
        By.XPATH, '//*[@id="carouselExampleIndicators"]/a[1]/span[1]')
    IMG_SAMSUNG = (By.CSS_SELECTOR, 'img[src*="Samsung1.jpg"]')
    IMG_NEXUS = (By.CSS_SELECTOR, 'img[src*="nexus1.jpg"]')
    IMG_LAPTOP = (By.CSS_SELECTOR, 'img[src*="iphone1.jpg"]')
    B_CATEGORY_PHONES = (By.XPATH, "//a[contains(text(),'Phones')]")
    B_CATEGORY_LAPTOPS = (By.XPATH, "//a[contains(text(),'Laptops')]")
    B_CATEGORY_MONITORS = (By.XPATH, "//a[contains(text(),'Monitors')]")
    B_SAMSUNG_S6 = (By.XPATH, "//button[contains(text(),'Samsung galaxy s6')]")
    B_LOGIN_CONFIRM = (By.XPATH, "//button[contains(text(),'Log in')]")
    B_LOGIN_CANCEL = (By.XPATH, "//button[contains(text(),'Close')]")
    B_SIGNUP_CONFIRM = (By.XPATH, "//button[contains(text(),'Sign up')]")

    def carousel_click_next(self):
        self.wait_until_clickable(self.B_CAROUSEL_NEXT).click()

    def carousel_click_prev(self):
        self.wait_until_clickable(self.B_CAROUSEL_PREV).click()

    def samsung_is_present(self):
        assert self.element_is_present(self.IMG_SAMSUNG)

    def nexus_is_present(self):
        assert self.element_is_present(self.IMG_NEXUS)

    def laptop_is_present(self):
        assert self.element_is_present(self.IMG_LAPTOP)

    def select_phone_category(self):
        self.wait_until_clickable(self.B_CATEGORY_PHONES)

    def select_phone_laptops(self):
        self.wait_until_clickable(self.B_CATEGORY_LAPTOPS)

    def select_phone_monitors(self):
        self.wait_until_clickable(self.B_CATEGORY_MONITORS)

    def open_samsung_galaxy_s6(self):
        self.wait_until_clickable(self.B_SAMSUNG_S6).click()

    def login_ui(self, name, password):
        self.wait_until_clickable(self.F_LOGIN_USERNAME).send_keys(name)
        self.wait_until_clickable(self.F_LOGIN_PASSWORD).send_keys(password)
        self.wait_until_clickable(self.B_LOGIN_CONFIRM).click()

    def check_login_successfully_complete(self):
        assert self.element_is_present(self.B_LOGOUT)

    def signup_ui(self, name, password):
        self.wait_until_clickable(self.F_SIGNUP_USERNAME).send_keys(name)
        self.wait_until_clickable(self.F_SIGNUP_PASSWORD).send_keys(password)
        self.wait_until_clickable(self.B_SIGNUP_CONFIRM).click()

    def check_signup_successfully_complete(self):
        assert self.wait_until_alert().text == 'Sign up successful.'
