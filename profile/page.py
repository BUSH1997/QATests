from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *



class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def get_username_element(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.profile-image-block .b2n')))

    def get_profile_orders_title(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.orders-box .box-title')))