from selenium.webdriver.common.by import By


class RegisterPage:

     def __init__(self,driver):
         self.driver = driver

     first_name_field_id = "input-firstname"
     last_name_field_id = "input-lastname"
     email_field_id = "input-email"
     telephone_field_id = "input-telephone"
     password_field_id = "input-password"
     password_conform_field_id = "input-confirm"
     privacy_policy_option_name = "agree"
     continue_button_xpath = "//input[@value='Continue']"
     yes_radio_option_xpath = "//input[@name='newsletter'][@value='1']"
     duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
     privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
     first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
     last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
     email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
     telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
     password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

     def enter_first_name(self,first_name_text):
         self.driver.find_element(By.ID,self.first_name_field_id).send_keys(first_name_text)


     def enter_last_name(self,last_name_text):
         self.driver.find_element(By.ID,self.last_name_field_id).send_keys(last_name_text)

     def enter_email(self,email_text):
         self.driver.find_element(By.ID,self.email_field_id).send_keys(email_text)

     def enter_telephone(self,telephone_text):
         self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_text)

     def enter_password(self,password_text):
         self.driver.find_element(By.ID,self.password_field_id).send_keys(password_text)

     def enter_password_conform(self,password_conform_text):
         self.driver.find_element(By.ID, self.password_conform_field_id).send_keys(password_conform_text)

     def select_privacy_policy(self):
         self.driver.find_element(By.NAME,self.privacy_policy_option_name).click()

     def click_on_continue_button(self):
         self.driver.find_element(By.XPATH,self.continue_button_xpath).click()

     def select_yes_newsletter_option(self):
         self.driver.find_element(By.XPATH,self.yes_radio_option_xpath).click()

     def display_status_of_duplicate_email_warning(self,expected_warning_text):
         return self.driver.find_element(By.XPATH,self.duplicate_email_warning_xpath).text.__contains__(expected_warning_text)

     def display_status_of_all_warnings(self,e_privacy_warning,e_first_name_warning,e_last_name_warning,e_email_warning,e_telephone_warning,e_password_warning):
         privacy_status = self.driver.find_element(By.XPATH,self.privacy_policy_warning_xpath).text.__contains__(e_privacy_warning)
         first_name_status = self.driver.find_element(By.XPATH,self.first_name_warning_xpath).text.__contains__(e_first_name_warning)
         last_name_status = self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text.__contains__(e_last_name_warning)
         email_status = self.driver.find_element(By.XPATH, self.email_warning_xpath).text.__contains__(e_email_warning)
         telephone_status = self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text.__contains__(e_telephone_warning)
         password_status = self.driver.find_element(By.XPATH, self.password_warning_xpath).text.__contains__(e_password_warning)
         if privacy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
             return True
         else:
             return False





