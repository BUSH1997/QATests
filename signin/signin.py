from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest

url = "https://goodvibesazot.tk/signin"

LOGIN = '12345'
PASSWORD = '12345'
LOGIN_NO_USER = 'adasdasdasd'
PASSWORD_INCORRECT = 'sdfsdfsdfsf'
PASSWORD_SHORT = '123'


class SignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signin_positive(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD)
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

    def test_signin_empty_field(self):
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

    def test_signin_no_user(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN_NO_USER)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Пользователя не существует')

    def test_signin_incorrect_password(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD_INCORRECT)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Неверный пароль')

    def test_signin_short_password(self):
        driver = self.driver
        driver.get(url=url)
        element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
        element_login.send_keys(LOGIN)
        element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
        element_password.send_keys(PASSWORD_SHORT)
        element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
        element_button.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        error = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))
        self.assertEqual(error.text, 'Неверный формат пароля')

    def test_signin_redirect_to_signup(self):
        driver = self.driver
        driver.get(url=url)
        element_signup_link = driver.find_element(by=By.CLASS_NAME, value='auth-content-form-registration__link')
        element_signup_link.click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        signup_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.auth-box h2')))
        self.assertEqual(signup_title.text, 'Создать аккаунт')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
