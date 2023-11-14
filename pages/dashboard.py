from pages.base_page import BasePage


class Dashboard(BasePage):
    dodaj_gracza_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button"
    strona_glowna_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]"
    gracze_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[2]"
    english = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]"
    wyloguj = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]"
    dev_team_contact_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a"
    ostatni_gracz_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    pass
