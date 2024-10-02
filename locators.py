from typing import Tuple

from selenium.webdriver.common.by import By


class Locators:
    TITLE_REG = (By.XPATH, ".//h2[text()='Регистрация']")
    INPUT_NAME_REG = By.XPATH, ".//label[text()='Имя']/parent::div/input"
    INPUT_EMAIL_REG = By.XPATH, ".//label[text()='Email']/parent::div/input"
    INPUT_PASSWORD_REG = By.XPATH, ".//label[text()='Пароль']/parent::div/input"
    REG_BUTTON = By.XPATH, "//button[contains(text(),'Зарегистрироваться')]"
    TITLE_ENTER = By.XPATH, ".//h2[contains(text(),'Вход')]"
    TITLE_ANCORRECT_PASS = By.XPATH, "//p[@class='input__error text_type_main-default']"
    INPUT_ACC_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"
    INPUT_ACC_BUTTON_REG = By.XPATH, "//a[contains(text(),'Войти')]"
    TITLE_RECOVERY = By.XPATH,"//h2[contains(text(), 'Восстановление пароля')]"
    TITLE_REMEMBERED = By.XPATH,"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]"
    RECOVERY_BUTTON = By.XPATH,"//button[contains(text(), 'Восстановить')]"
    INPUT_EMAIL_ENTER = By.XPATH, "//input[@name='name']"
    INPUT_PASSWORD_ENTER = By.XPATH, "//input[@name='Пароль']"
    INPUT_NAME_REPAIR = By.NAME, "name"
    ENTER_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"
    PLACE_ON_ORDER_BUTTON = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    DESIGNER_BUTTON = By.XPATH, ".//p[text()='Конструктор']"
    STRIP_BUTTON = By.XPATH, ".//p[text()='Лента Заказов']"
    LOGO_BUTTON = By.XPATH, "(//*[name()='svg'])[3]"
    LOGIN_BUTTON = By.XPATH, ".//batton[text()='Войти в аккаунт']"
    PERSONAL_AC_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    LOGOUT_BUTTON = By.XPATH,"// button[contains(text(), 'Выход')]"
    TITLE_PROFILE = By.XPATH, "//a[contains(text(),'Профиль')]"
    TITLE_COLLECT_BURGER = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]"
    LOAF_BUTTON = By.XPATH, ".//span[text()='Булки']"
    SAUCE_BUTTON = By.XPATH, ".//span[text()='Соусы']"
    FILLING_BUTTON = By.XPATH, ".//span[text()='Начинки']"
    FILLING_VISIBLE = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[3]"
    LOAF_VISIBLE = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[1]"
    SAUCE_VISIBLE = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]"
    TITLE_CHANGE_PROFILE = By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']"

