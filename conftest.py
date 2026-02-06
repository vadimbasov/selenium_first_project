import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.ember-view navbar__auth.navbar__auth_login.st-link st-link_style_button'))
    )
    button.click()
    # browser.find_element(By.CSS_SELECTOR, '#ember499').click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('vadim.bassoff@gmail.com')
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('VBasov21-Stepik6493')

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.sign-form__btn.button_with-loader '))
    )
    button.click()
    yield browser
    browser.quit()

# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")