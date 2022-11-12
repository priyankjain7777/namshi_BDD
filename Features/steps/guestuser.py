from behave import *
from selenium import webdriver



@given('open chrome browser')
def OpenBrowser(context):
    # context.driver=webdriver.Chrome(executable_path="C:\Users\hp\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
    context.driver = webdriver.Chrome(executable_path="C:\Drivers.chromedriver.exe")
    context.driver.maximize_window()


@when('enter website url')
def EnterURL(context):
    context.driver.get("https://en-ae.namshi.com/women-clothing/")


@then('click on any available products')
def SelectProduct(context):
    status=context.driver.find_element("xpath","//a[@data-gender-cookie='women']").click


@then('click on any different product')
def ChangeProduct(context):
    status=context.driver.find_element("xpath","//a[@data-gender-cookie='men']").click



