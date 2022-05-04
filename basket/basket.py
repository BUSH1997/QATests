import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import unittest
from utils.utils import login
from selenium.webdriver.support.ui import Select

PRODUCT_COUNT = 2
POST_OPTION = 2


class Basket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.product_id = 0

    def test_basket(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()
        css_product = 'table-product-' + self.product_id.__str__()
        product_in_basket = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_product)))
        remove_product_from_basket(self.product_id, wait)

    def test_basket_count(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        product_count_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-page-spinner__count')))
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(PRODUCT_COUNT.__str__())
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()
        css_sum = 'raw-item-price-' + self.product_id.__str__()
        css_price = 'item-price-' + self.product_id.__str__()
        product_sum = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_sum)))
        product_price = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_price)))
        count = int(int(product_sum.text) / int(product_price.text))
        self.assertEqual(count, PRODUCT_COUNT)

        remove_product_from_basket(self.product_id, wait)

    def test_basket_refresh(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        driver.refresh()

        css_product = 'table-product-' + self.product_id.__str__()
        product_in_basket = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_product)))
        remove_product_from_basket(self.product_id, wait)

    def test_basket_delete_product(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        remove_product_from_basket(self.product_id, wait)

        css_product = 'table-product-' + self.product_id.__str__()
        try:
            product_in_basket = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_product)))
            not_found = False
        except:
            not_found = True
        self.assertEqual(not_found, True)

    def test_basket_empty(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        remove_product_from_basket(self.product_id, wait)

        empty_basket_text = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'basket-empty-text')))

        self.assertEqual(empty_basket_text.text, "Ваша корзина пуста. Вернуться к покупкам")

    def test_basket_increase_in_basket(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        product_count_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'spinner__count')))
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(PRODUCT_COUNT.__str__())

        anywhere = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'coupon-row')))
        anywhere.click()

        css_sum = 'raw-item-price-' + self.product_id.__str__()
        css_price = 'item-price-' + self.product_id.__str__()

        product_sum = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_sum)))
        product_price = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_price)))

        count = int(int(product_sum.text) / int(product_price.text))
        self.assertEqual(count, PRODUCT_COUNT)

        remove_product_from_basket(self.product_id, wait)

    def test_basket_change_sum_of_one_product(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()
        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        product_count_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'spinner__count')))
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(PRODUCT_COUNT.__str__())

        anywhere = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'coupon-row')))
        anywhere.click()

        css_price = 'item-price-' + self.product_id.__str__()

        product_sum = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'basket-order-total__number')))
        product_price = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_price)))

        expected_sum = int(product_price.text) * PRODUCT_COUNT

        self.assertEqual(int(product_sum.text[:len(product_sum.text)-1]), expected_sum)

        remove_product_from_basket(self.product_id, wait)

    def test_basket_change_sum_many_products(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()

        back_in_catalog = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'back-to-result__link')))
        back_in_catalog.click()

        product_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div[href="/product?id={self.product_id+1}"]')))
        product_card.click()
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()

        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        css_sum_product_first = 'raw-item-price-' + self.product_id.__str__()
        css_sum_product_second = 'raw-item-price-' + (self.product_id+1).__str__()

        product_sum_first = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_sum_product_first)))
        product_sum_second = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_sum_product_second)))
        order_sum = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'basket-order-total__number')))

        self.assertEqual(int(order_sum.text[:len(order_sum.text)-1]), int(product_sum_first.text) + int(product_sum_second.text))

        remove_product_from_basket(self.product_id, wait)
        remove_product_from_basket(self.product_id+1, wait)

    def test_basket_selector(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()

        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        select_elem = wait.until(EC.element_to_be_clickable((By.ID, 'orderform-delivery_method')))
        selector = Select(select_elem)
        selector.select_by_index(POST_OPTION)
        option = selector.first_selected_option
        self.assertEqual(option.text, "Почта россии")

        remove_product_from_basket(self.product_id, wait)

    def test_success_order(self):
        driver = self.driver
        login(driver)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])
        product_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))
        product_card.click()
        one_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))
        current_url = driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))
        add_to_basket_button.click()

        go_to_basket_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))
        go_to_basket_button.click()

        confirm_order_button = driver.find_element(by=By.CLASS_NAME, value='confirm-btn')
        confirm_order_button.click()

        profile_orders_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.orders-box .box-title')))
        self.assertEqual(profile_orders_title.text, 'Мои заказы')

    def tearDown(self):

        self.driver.close()
        self.driver.quit()


def remove_product_from_basket(product_id, wait):
    css_remove = f'a[href="/cart/remove/{product_id}"]'
    remover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_remove)))
    remover.click()
