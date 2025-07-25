import pytest
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigation:
    def test_navigate_to_constructor(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")

    # Ждём кнопку меню
        menu_icon = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(BURGER_MENU_ICON)
        )
        menu_icon.click()

    # Ждём секцию булок
        buns_section = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(MENU_BUNS_SECTION)
        )
        assert buns_section.is_displayed()

    def test_browse_menu_sections(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")

    # Ждём кнопку меню
        menu_icon = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(BURGER_MENU_ICON)
        )
        menu_icon.click()

    # Ждём появление каждой секции меню
        sections = [MENU_BUNS_SECTION, MENU_SAUCES_SECTION, MENU_FILLINGS_SECTION]
        for section in sections:
            element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(section)
            )
            assert element.is_displayed()