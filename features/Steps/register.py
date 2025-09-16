from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.Accountsuccesspage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to register page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_my_account()
    home_page.select_register_option()



@when(u'I enter details into mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("Aishwarya")
    context.register_page.enter_last_name("Ganiger")

    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "aishu" + time_stamp + "@gmail.com"

    context.register_page.enter_email(new_email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("@Aishu#2000")
    context.register_page.enter_password_conform("@Aishu#2000")


@when(u'I select privacy policy option')
def step_impl(context):
    context.register_page.select_privacy_policy()


@when(u'I click on continue button')
def step_impl(context):
    context.register_page. click_on_continue_button()

@then('account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    account_success_page = AccountSuccessPage(context.driver)
    assert account_success_page.display_status_of_account_created_heading(expected_text)


@when('I enter details into all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("Aishwarya")
    context.register_page.enter_last_name("Ganiger")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "aishu" + time_stamp + "@gmail.com"
    context.register_page.enter_email(new_email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("@Aishu#2000")
    context.register_page.enter_password_conform("@Aishu#2000")
    context.register_page.select_yes_newsletter_option()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("Aishwarya")
    context.register_page.enter_last_name("Ganiger")
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("@Aishu#2000")
    context.register_page.enter_password_conform("@Aishu#2000")
    context.register_page.select_yes_newsletter_option()


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email("aishuganiger09@gmail.com")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.register_page.display_status_of_duplicate_email_warning(expected_warning)


@then('I dont enter anything into the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_password_conform("")
    context.register_page.select_yes_newsletter_option()



@then('Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):

    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    assert context.register_page.display_status_of_all_warnings(expected_privacy_policy_warning,
                                                                expected_first_name_warning,
                                                                expected_last_name_warning,
                                                                expected_email_warning,
                                                                expected_telephone_warning,
                                                                expected_password_warning)






