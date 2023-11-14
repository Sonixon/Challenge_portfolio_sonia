from pages.base_page import BasePage


class add_a_match_form(BasePage):
    My_team_input_xpath = "//*[@name='myTeam']"
    Enemy_team_input_xpath = "//*[@name='enemyTeam']"
    My_team_score_input_xpath = "//*[@name='myTeamScore']"
    Enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"
    Date_input_xpath = "//*[@name='date']"
    Match_at_home_input_xpath = "//*[@name='matchAtHome']"
    Match_out_home_input_xpath = "//*[@name='matchOutHome']"
    T-schirt_color_input_xpath = "//*[@name='tshirt']"
    Submit_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]"
    Clear_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]"
pass