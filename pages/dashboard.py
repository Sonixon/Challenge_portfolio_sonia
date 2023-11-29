from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
import time


class Dashboard(BasePage):
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    scouts_panel_logo_xpath = "//*[@title='Logo Scouts Panel']"
    dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    shortcuts_header_xpath = "//div[2]/div/div/h2"
    activity_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
    players_button_xpath = "//ul[1]/div[2]"
    add_a_player_button_xpath = "//div[2]/div/div/a/button/span[1]"
    last_created_player_header_xpath = "//div/div/h6[1]"
    last_created_player_button_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_header_xpath = "//h6[2]"
    last_updated_player_button_xpath = "//a[2]/button/span[1]"
    last_created_match_header_xpath = "//h6[3]"
    last_created_match_button_xpath = "//a[3]/button/span[1]"
    last_updated_match_header_xpath = "//h6[4]"
    last_updated_match_button_xpath = "//a[4]/button/span[1]"
    last_updated_report_header_xpath = "//h6[5]"
    last_updated_report_button_xpath = "a[5]/button/span[1]"
    expected_title = "Scouts panel"
    expected_last_created_player = "Marian Kowalski"
    dashboard_url = 'https://scouts.futbolkolektyw.pl/en'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)

    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def check_last_created_player(self):
        self.assert_element_text(self.driver, self.last_created_player_button_xpath, self.expected_last_created_player)
