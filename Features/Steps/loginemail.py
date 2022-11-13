from behave import *
from selenium import webdriver


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\Drivers.chromedriver.exe")
    context.driver.maximize_window()


@when('I provide website url')
def step_impl(context):
    context.driver.get("https://en-ae.namshi.com/women-clothing/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").sendkeys(user)
    context.driver.find_element_by_id("txtpassword").sendkeys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnlogin").click()


@then('Check dashboard page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("").text
    assert text == dashboard
    context.driver.close()


@then('logout to website')
def step_impl(context):
    context.driver.find_element_by_id("AccoutSetting").click()
    context.driver.find_element_by_id("logoutbutton").click()
