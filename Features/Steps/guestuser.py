from lib2to3.pgen2 import driver

from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@given('open chrome browser')
def OpenBrowser(context):
    # context.driver=webdriver.Chrome(executable_path="C:\Users\hp\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
    context.driver = webdriver.Chrome(executable_path="C:\Drivers.chromedriver.exe")
    context.driver.maximize_window()


@when('enter website url')
def EnterURL(context):
    context.driver.get("https://en-ae.namshi.com/women-clothing/")


@when('click on any available products')
def SelectProduct(context):
    context.driver.find_element("xpath", "//a[@data-gender-cookie='women']").click


@When('click on any different product2')
def ChangeProduct2(context):
    # context.driver.wait = WebDriverWait(driver, 120)
    context.driver.find_element("xpath", "//a[@data-gender-cookie='kids']").click


@then('close browser')
def ChangeProduct3(context):
    # context.driver.wait = WebDriverWait(driver, 120)
    context.driver.close()
