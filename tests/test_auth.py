import random
import string
import pytest
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_random_email():
    domain = "@example.com"
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    return f"{username}{domain}"

def test_successful_registration(browser):
    browser.get("https://stellarburgers.nomoreparties.site/register")

    # Ждём поля формы регистрации
    name_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(REGISTER_FORM_NAME_FIELD)
    )
    email_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(REGISTER_FORM_EMAIL_FIELD)
    )
    password_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(REGISTER_FORM_PASSWORD_FIELD)
    )

    # Сначала кликаем по элементу, затем заполняем значение
    name_input.click()
    name_input.clear()
    name_input.send_keys("John Doe")

    email_input.click()
    email_input.clear()
    email_input.send_keys(generate_random_email())

    password_input.click()
    password_input.clear()
    password_input.send_keys("ValidPassword123!")

    # Ждём кнопку отправки формы
    register_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON)
    )
    register_button.click()

    # Ждём сообщение об успешной регистрации
    success_message = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(REGISTRATION_SUCCESS_MESSAGE)
    )
    assert "Вы успешно зарегистрированы" in success_message.text

def test_invalid_password_registration(browser):
    browser.get("https://stellarburgers.nomoreparties.site/register")

    # Ждём поля формы регистрации
    name_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(REGISTER_FORM_NAME_FIELD)
    )
    email_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(REGISTER_FORM_EMAIL_FIELD)
    )
    password_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(REGISTER_FORM_PASSWORD_FIELD)
    )

    # Сначала кликаем по элементу, затем заполняем значение
    name_input.click()
    name_input.clear()
    name_input.send_keys("Jane Smith")

    email_input.click()
    email_input.clear()
    email_input.send_keys(generate_random_email())

    password_input.click()
    password_input.clear()
    password_input.send_keys("pwd")  # Короткий пароль

    # Ждём кнопку отправки формы
    register_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON)
    )
    register_button.click()

    # Ждём сообщение об ошибке регистрации
    error_message = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(INVALID_CREDENTIALS_MESSAGE)
    )
    assert "Неверный логин или пароль" in error_message.text

def test_login(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Ждём кнопку входа
    login_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(ACCOUNT_LOGIN_BUTTON)
    )
    login_button.click()

    # Ждём поля формы входа
    email_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(LOGIN_FORM_EMAIL_FIELD)
    )
    password_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(LOGIN_FORM_PASSWORD_FIELD)
    )

    # Сначала кликаем по элементу, затем заполняем значение
    email_input.click()
    email_input.clear()
    email_input.send_keys("valid_user@example.com")

    password_input.click()
    password_input.clear()
    password_input.send_keys("ValidPassword123!")

    # Ждём кнопку входа
    login_submit_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)
    )
    login_submit_button.click()

    # Ждём появление панели личного кабинета
    profile_section = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(PERSONAL_ACCOUNT_BUTTON)
    )
    assert profile_section.is_displayed()