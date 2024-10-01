from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestCrossoverConstructor:

    def test_constructor_transition_to_filling(self, driver_login):
        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))

        driver_login.find_element(*Locators.FILLING_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING_CHOP))



    def test_constructor_transition_to_souce(self, driver_login):
        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))

        driver_login.find_element(*Locators.FILLING_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING_CHOP))

        driver_login.find_element(*Locators.SAUCE_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.SAUCE_SPACE))



    def test_constructor_loaf_transition_to_loaf(self, driver_login):
        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))

        driver_login.find_element(*Locators.FILLING_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING_CHOP))

        driver_login.find_element(*Locators.LOAF_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.LOAF_N))

