import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import unittest
from utils.utils import login

OLD_NAME = 'OldName'
NEW_NAME = 'NewName'
OLD_SURNAME = 'OldSurname'
NEW_SURNAME = 'NewSurname'
OLD_EMAIL = 'OldEmail@mail.ru'
NEW_EMAIL = 'NewEmail@mail.ru'
OLD_DATE = '01.01.2000'
NEW_DATE = '31.12.2000'
NEW_DATE_COMPARE = '2000-12-31'
MALE_SEX = 2
NO_SEX = 0


class Profile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_profile_update_button(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()
        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        self.assertEqual(update_button.text, 'ОБНОВИТЬ')

    def test_profile_update_notification(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()
        update_notification = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile-update-alert-label')))
        self.assertEqual(update_notification.text, 'Данные обновлены!')

    def test_update_name(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        name_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__firstname')))
        name_input.click()
        name_input.clear()
        name_input.send_keys(NEW_NAME)

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

        driver.refresh()

        updated_name = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__firstname')))
        self.assertEqual(updated_name.get_attribute('value'), NEW_NAME)

        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        updated_name.click()
        updated_name.clear()
        updated_name.send_keys(OLD_NAME)
        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

    def test_update_surname(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        name_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__secondname')))
        name_input.click()
        name_input.clear()
        name_input.send_keys(NEW_SURNAME)

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

        driver.refresh()

        updated_name = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__secondname')))
        self.assertEqual(updated_name.get_attribute('value'), NEW_SURNAME)

        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        updated_name.click()
        updated_name.clear()
        updated_name.send_keys(OLD_SURNAME)
        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

    def test_update_email(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        name_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__email')))
        name_input.click()
        name_input.clear()
        name_input.send_keys(NEW_EMAIL)

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

        driver.refresh()

        updated_name = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__email')))
        self.assertEqual(updated_name.get_attribute('value'), NEW_EMAIL)

        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        updated_name.click()
        updated_name.clear()
        updated_name.send_keys(OLD_EMAIL)
        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

    def test_update_sex(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        sex = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__sex')))
        selector = Select(sex)
        selector.select_by_index(MALE_SEX)

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

        driver.refresh()

        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        sex = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__sex')))
        selector = Select(sex)
        option = selector.first_selected_option
        self.assertEqual(option.text, "Мужской")

        selector.select_by_index(NO_SEX)
        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

    def test_update_birthday(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))
        profile_icon.click()
        profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))
        profile_link.click()
        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        birthday = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__birthday')))
        birthday.send_keys(NEW_DATE)

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

        driver.refresh()

        updated_birthday = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__birthday')))
        self.assertEqual(updated_birthday.get_attribute('value'), NEW_DATE_COMPARE)

        change_profile_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))
        change_profile_link.click()

        updated_birthday.click()
        updated_birthday.send_keys(OLD_DATE)

        update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))
        update_button.click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
