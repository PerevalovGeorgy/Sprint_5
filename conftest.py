import pytest
from data_url import TestUrl, UserData
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver_login(driver):

    driver.get(TestUrl.url_login_page)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

    driver.find_element(*Locators.INPUT_EMAIL_ENTER).send_keys(UserData.email)
    driver.find_element(*Locators.INPUT_PASSWORD_ENTER).send_keys(UserData.password)

    driver.find_element(*Locators.ENTER_BUTTON).click()

    yield driver


