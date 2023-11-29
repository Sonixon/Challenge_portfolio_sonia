import os
import unittest
import time

from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestGoToAddNewPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_go_to_add_a_new_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        time.sleep(5)
        add_player = AddAPlayer(self.driver)
        add_player.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()