from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestCrossoverConstructor:

    def test_constructor_transition_to_main_page(self, driver_login):
        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_AC_BUTTON))

        driver_login.find_element(*Locators.PERSONAL_AC_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_PROFILE))

        driver_login.find_element(*Locators.DESIGNER_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))


    def test_logo_transition_to_main_page(self, driver_login):
        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_AC_BUTTON))

        driver_login.find_element(*Locators.PERSONAL_AC_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_PROFILE))

        driver_login.find_element(*Locators.LOGO_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))