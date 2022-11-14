from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\Drivers.Chromedriver.exe")
    context.driver.maximize_window()


@when('I provide website url')
def step_impl(context):
    context.driver.get("https://en-ae.namshi.com/women-clothing/")
    # context.driver.find_element_by_xpath("").click()
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='welcomePopup']/div[2]/div"))
    ).click
    # context.driver.find_element("xpath", ).click()
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='wzrk-cancel']"))
    ).click


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    # ("//*[@id='wrapper']/div[7]/div[2]/div/div[3]/div/a[2]")
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='wrapper']/div[7]/div[2]/div/div[3]/div/a[2]"))).click
#handle login page iframe
    context.driver.switch_to.frame(context.driver.find_element("xpath", "//*[@id='userAuthIframe']"))
    # enter user id password
    context.driver.find_element("xpath", "//*[@id='app']/div/div[1]/div[1]").click
    #context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/div[1]/div/input")
    #context.driver.send_keys("user")
    context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/div[2]/div/input")
    context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/div[1]/div/input")
    #context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/div[1]/div/input").send_keys("user")
    #context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/div[2]/div/input").sendKeys("pwd")


@when('Click on login button')
def step_impl(context):
    context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/button")


@when('Check dashboard page')
def step_impl(context):
    text = context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/button").text
    assert text == dashboard




@then('logout to website')
def step_impl(context):
    #context.driver.find_element_by_id("AccoutSetting").click()
    context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/button")
    #context.driver.find_element_by_id("logoutbutton").click()
    context.driver.find_element("xpath", "//*[@id='login']/div[1]/div/section/form/button")
