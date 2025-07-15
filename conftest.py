import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="session")
def browser():
    chrome_options = ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()