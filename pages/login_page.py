 from pages.base_page import BasePage


 class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id = ‘password’]"
     sign_in_button_xpath = "//child::html/body/div/form/div/div[2]/button"

     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
