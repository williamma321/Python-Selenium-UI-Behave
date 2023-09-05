import os
from behave import fixture, use_fixture
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
get_call_url = os.getenv("LIB_BASE_URL")
get_selenium_driver_path = os.getenv("SELENIUM_DRIVER_PATH")
myUserName = os.getenv("LIB_USER_NAME")
myPwd = os.getenv("LIB_PWD")
PATH = os.getenv("SELENIUM_DRIVER_PATH", "/Users/irenema/Documents/Python Projects/Selenium-Python-demo/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
demo_driver = webdriver.Chrome()


@fixture
def before_all(context):
    context.username = myUserName
    context.password = myPwd
    context.call_url = get_call_url
    context.selenium_driver = demo_driver
    context.page_object_dict = {"object": ""}
