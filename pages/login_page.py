from locators.login_locators import LoginLocators as ll
from core.core import Core
import time


class LoginPage(Core):
    def __init__(self, driver):
        Core.__init__(self, driver)
        self.driver = driver

    def login_title(self):
        return self.driver.title

    def action_login(self, username, password):
        Core.send_keys(
            self, [ll.input_username['by'], ll.input_username['v']], username
        )
        Core.send_keys(
            self, [ll.input_password['by'], ll.input_password['v']], password
        )
        Core.click(self, [ll.login_btn['by'], ll.login_btn['v']])

    def action_logout(self):
        self.driver.find_element(ll.hamburger_btn['by'], ll.hamburger_btn['v']).click()
        self.driver.find_element(ll.logout_btn['by'], ll.logout_btn['v']).click()
