from selenium.webdriver.common.by import By


LOGIN = '12345'
PASSWORD = '12345'
LOGIN_NO_USER = 'adasdasdasd'
PASSWORD_INCORRECT = 'sdfsdfsdfsf'
PASSWORD_SHORT = '123'


url = "https://goodvibesazot.tk/signin"


def login(driver):
    driver.get(url=url)
    element_login = driver.find_element(by=By.CLASS_NAME, value='user-box__login')
    element_login.send_keys(LOGIN)
    element_password = driver.find_element(by=By.CLASS_NAME, value='user-box__password')
    element_password.send_keys(PASSWORD)
    element_button = driver.find_element(by=By.CLASS_NAME, value='auth-btn')
    element_button.click()
