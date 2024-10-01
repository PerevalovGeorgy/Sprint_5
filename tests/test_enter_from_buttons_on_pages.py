from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestLogin:

    def test_login_from_button_on_password_recovery_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_RECOVERY))

        driver.find_element(*Locators.INPUT_EMAIL_ENTER).send_keys('ivan1234@ya.ru')

        driver.find_element(*Locators.RECOVERY_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_RECOVERY))


    def test_login_from_button_on_registration_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_REG))

        driver.find_element(*Locators.INPUT_ACC_BUTTON_REG).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

        driver.find_element(*Locators.INPUT_EMAIL_ENTER).send_keys('ivan1234@ya.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_ENTER).send_keys('123456')

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))


    def test_login_from__main_page_button_entry_personal_account_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.INPUT_ACC_BUTTON))

        driver.find_element(*Locators.PERSONAL_AC_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

        driver.find_element(*Locators.INPUT_EMAIL_ENTER).send_keys('ivan1234@ya.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_ENTER).send_keys('123456')

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))


    def test_login_from_button_on_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.INPUT_ACC_BUTTON))

        driver.find_element(*Locators.INPUT_ACC_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

        driver.find_element(*Locators.INPUT_EMAIL_ENTER).send_keys('ivan1234@ya.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_ENTER).send_keys('123456')

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ON_ORDER_BUTTON))


