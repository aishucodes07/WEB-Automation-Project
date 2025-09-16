from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given('I got navigated to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    #expected_title = "Your Store"
    assert context.home_page.check_home_page_title("Your Store")


@when('I enter valid product into the Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("HP")


@when('I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()

@then('Valid product should get displayed in Search results')
def step_impl(context):
   assert context.search_page.display_status_of_product()



@when('I enter invalid product into the Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("Honda")


@then('Proper message should be displayed in search results')
def step_impl(context):
    assert context.search_page.display_status_of_message("There is no product that matches the search criteria.")


@when('I dont enter anything into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")
