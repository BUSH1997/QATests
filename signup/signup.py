import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest
from random_username.generate import generate_username

url = "https://goodvibesazot.tk/signup"

LOGIN = generate_username(1)[0]
LOGIN_USER_EXISTS = '12345'
EMAIL = LOGIN + '@mail.ru'
EMAIL_WRONG = LOGIN + '@mailu'
PASSWORD = '12345'
PASSWORD_CONFIRM = '12345'
PASSWORD_CONFIRM_NOT_MATCH = '12346'


class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signup_positive(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN)
        element_email = driver.find_element(by=By.CLASS_NAME, value='user-box__email')
        element_email.send_keys(EMAIL)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD)
        element_password_repeat = driver.find_element(by=By.CLASS_NAME, value='user-box__confirm-password')
        element_password_repeat.send_keys(PASSWORD_CONFIRM)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        user_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.profile-image-block .b2n')))
        self.assertEqual(LOGIN, user_name.text)

    def test_signup_empty_field(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Заполните все поля')

    def test_signup_user_exists(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN_USER_EXISTS)
        element_email = driver.find_element(by=By.CLASS_NAME, value='user-box__email')
        element_email.send_keys(EMAIL)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD)
        element_password_repeat = driver.find_element(by=By.CLASS_NAME, value='user-box__confirm-password')
        element_password_repeat.send_keys(PASSWORD_CONFIRM)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Пользователь уже существует')

    def test_signup_passwords_not_match(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN_USER_EXISTS)
        element_email = driver.find_element(by=By.CLASS_NAME, value='user-box__email')
        element_email.send_keys(EMAIL)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD)
        element_password_repeat = driver.find_element(by=By.CLASS_NAME, value='user-box__confirm-password')
        element_password_repeat.send_keys(PASSWORD_CONFIRM_NOT_MATCH)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Пароли не одинаковые')

    def test_signup_wrong_email_wrong(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN_USER_EXISTS)
        element_email = driver.find_element(by=By.CLASS_NAME, value='user-box__email')
        element_email.send_keys(EMAIL_WRONG)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD)
        element_password_repeat = driver.find_element(by=By.CLASS_NAME, value='user-box__confirm-password')
        element_password_repeat.send_keys(PASSWORD_CONFIRM)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Неправильный формат данных')

    def test_signup_redirect_to_signin(self):
        driver = self.driver
        driver.get(url=url)
        element_signup_link = driver.find_element(by=By.CLASS_NAME, value='auth-content-form-signin__link')
        element_signup_link.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        signin_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.auth-box h2')))
        self.assertEqual(signin_title.text, 'Вход')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
