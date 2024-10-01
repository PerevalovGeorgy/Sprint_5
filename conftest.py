import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


@pytest.fixture
def exemple_ancorrect_user(word):
    user_dat = {'name': '', 'Email': 'ivanyaru', 'Пароль': '12345'}
    return user_dat[word]


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver_login():
    driver_login = webdriver.Chrome()
    driver_login.get("https://stellarburgers.nomoreparties.site/login")

    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTER))

    driver_login.find_element(*Locators.INPUT_EMAIL_ENTER).send_keys('ivan1234@ya.ru')
    driver_login.find_element(*Locators.INPUT_PASSWORD_ENTER).send_keys('123456')

    driver_login.find_element(*Locators.ENTER_BUTTON).click()

    yield driver_login
    driver_login.quit()

