from behave import given, when, then
import json
from features.steps.utils import get_load_json_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'the logon page {username}')
def step_impl(context, username):
    context.page_object_dict = get_load_json_data("../page_objects/", "logon_page.json")
    the_pageobj = context.page_object_dict
    the_driver = context.selenium_driver
    the_driver.get(context.call_url)
    context.login_button = WebDriverWait(the_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, the_pageobj['logonPage']['logonButton'])))
    username_field = the_driver.find_element(By.XPATH, the_pageobj['logonPage']['userNameEditorBox'])
    context.password_field = the_driver.find_element(By.XPATH, the_pageobj['logonPage']['userPasswordEditorBox'])
    if username == 'correct':
        username_field.send_keys(context.username)
        time.sleep(1)
    else:
        username_field.send_keys(username)
        time.sleep(1)


@given(u'the logon {password}')
def step_impl(context, password):
    if password == 'correct':
        context.password_field.send_keys(context.password)
        time.sleep(1)
    else:
        context.password_field.send_keys(password)
        time.sleep(1)


@when(u'click on logon')
def step_impl(context):
    context.login_button.click()
    time.sleep(5)


@then(u'the logon is {status}')
def step_impl(context, status):
    context.page_object_dict = get_load_json_data("../page_objects/", "book_management.json")
    book_manage_page_dict = context.page_object_dict
    the_driver = context.selenium_driver
    try:
        is_button_visible = the_driver.find_element(By.XPATH, book_manage_page_dict['BookMgePage'][
            'pagetable']).is_displayed()
    except Exception:
        is_button_visible = False
    if status == 'OK':
        assert is_button_visible == True
    else:
        assert is_button_visible == False
        failed_text = WebDriverWait(the_driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "failureNotification")))
        assert failed_text.text == "Your login attempt was not successful. Please try again."
    logout_url_link = the_driver.find_element(By.XPATH, book_manage_page_dict['BookMgePage']['logout_url'])
    logout_url_link.click()
