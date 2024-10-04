from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data_generator
from locators import Locators
from data_url import TestUrl


class TestRegistration:

    def test_correct_registration_true(self, driver):
        driver.get(TestUrl.url_register_page)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_REG))

        driver.find_element(*Locators.INPUT_NAME_REG).send_keys('Имя')
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys(data_generator.user_login('Имя'))
        driver.find_element(*Locators.INPUT_PASSWORD_REG).send_keys(data_generator.user_password())

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

        assert driver.find_element(*Locators.ENTER_BUTTON).get_attribute(
            "class") == 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa'

    def test_ancorrect_registration_folse(self, driver):
        driver.get(TestUrl.url_register_page)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_REG))

        driver.find_element(*Locators.INPUT_NAME_REG).send_keys('Ваня')
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys('ivan12@ya.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_REG).send_keys('12345')

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.TITLE_ANCORRECT_PASS))

        assert driver.find_element(*Locators.TITLE_ANCORRECT_PASS).text == 'Некорректный пароль'

