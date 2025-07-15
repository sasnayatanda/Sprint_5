import pytest
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Ждём кнопку входа
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(ACCOUNT_LOGIN_BUTTON)
    )
    login_button.click()

    # Ждём появление полей формы входа
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LOGIN_FORM_EMAIL_FIELD)
    )
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LOGIN_FORM_PASSWORD_FIELD)
    )

    # Заполняем поля формы входа
    email_input.send_keys("valid_user@example.com")
    password_input.send_keys("ValidPassword123!")

    # Ждём кнопку входа
    login_submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)
    )
    login_submit_button.click()

    # Ждём появление панели личного кабинета
    profile_section = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(PERSONAL_ACCOUNT_BUTTON)
    )

    # Ждём кнопку выхода
    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON)
    )
    logout_button.click()

    # Ждём появление формы входа
    login_form = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(LOGIN_FORM_EMAIL_FIELD)
    )
    assert login_form.is_displayed()