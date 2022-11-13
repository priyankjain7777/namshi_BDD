from behave import *
from selenium import webdriver


@given('launch chrome browser')
def openbrowser(context):
    # context.driver=webdriver.Chrome(executable_path="C:\Users\hp\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
    context.driver = webdriver.Chrome(executable_path="C:\Drivers.chromedriver.exe")
    context.driver.maximize_window()


@when('provide website urls')
def enterurl(context):
    context.driver.get("https://en-ae.namshi.com/men/")
    context.driver.sleep(15)



@then('click on register button')
def step_impl(context,status):
    status=context
    status = context.driver.find_element("xpath", "//a[@title='My Account']").click
    context.driver.sleep(5) # seconds


@then('fill registration form')
def step_impl(context):
    context.driver.close_browser()


@then('check user Dashbaord page')
def step_impl(context):
    context.driver.close_browser()



