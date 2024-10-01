from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data_generator
from locators import Locators


class TestRegistration:

    def test_correct_registration_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_REG))

        #эти три строчки можно вывести в фикстуру регистрации с рандомом
        driver.find_element(*Locators.INPUT_NAME_REG).send_keys('Имя')
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys(data_generator.user_login('Имя'))
        driver.find_element(*Locators.INPUT_PASSWORD_REG).send_keys(data_generator.user_password())

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))


    def test_ancorrect_registration_folse(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_REG))

        driver.find_element(*Locators.INPUT_NAME_REG).send_keys('Иван')
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys('ivan1234@ya.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_REG).send_keys('12345')

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ANCORRECT_PASS))

