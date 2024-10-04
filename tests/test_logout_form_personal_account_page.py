from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestCrossoverProfilePage:

    def test_crossover_from_profile_page(self, driver_login):
        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_AC_BUTTON))

        driver_login.find_element(*Locators.PERSONAL_AC_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_PROFILE))

        driver_login.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

        assert driver_login.find_element(*Locators.ENTER_BUTTON).get_attribute(
            "class") == 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa'

