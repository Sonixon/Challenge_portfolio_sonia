import os
import unittest
import time
from PIL import Image

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        login_form_filled_file_path = os.path.abspath("screenshots/login_to_the_system/login_form_filled.png")
        user_login.title_of_page()
        user_login.check_header_of_box()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        self.driver.save_screenshot(login_form_filled_file_path)
        Image.open(login_form_filled_file_path).show()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    def test_log_in_with_invalid_data(self):
        user_login = LoginPage(self.driver)
        invalid_data_file_path = os.path.abspath("screenshots/login_to_the_system/invalid_data.png")
        user_login.title_of_page()
        user_login.check_header_of_box()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234567')
        user_login.click_sign_in_button()
        user_login.invalid_data()
        self.driver.save_screenshot(invalid_data_file_path)
        Image.open(invalid_data_file_path).show()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()