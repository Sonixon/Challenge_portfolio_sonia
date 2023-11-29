import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from PIL import Image


class TestLogOut(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_out_of_the_system(self):
        user_login = LoginPage(self.driver)
        dashboard_file_path = os.path.abspath("screenshots/log_out/dashboard.png")
        logged_out_file_path = os.path.abspath("screenshots/log_out/logged_out.png")
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        self.driver.save_screenshot(dashboard_file_path)
        Image.open(dashboard_file_path).show()
        dashboard_page.click_sign_out_button()
        user_login.title_of_page()
        self.driver.save_screenshot(logged_out_file_path)
        Image.open(logged_out_file_path).show()

    @classmethod
    def tearDown(self):
        self.driver.quit()