import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import string

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Или другой браузер
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def generate_random_email():
    domain = "@example.com"
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    return f"{username}{domain}"