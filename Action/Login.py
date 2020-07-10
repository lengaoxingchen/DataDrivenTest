from PageObject.LoginPage import *
from selenium import webdriver


def login(driver, username, password):
    lp = LoginPage(driver)
    driver.switch_to.frame(lp.getFrame())
    lp.getUserName().clear()
    lp.getUserName().send_keys(username)
    lp.getPassword().send_keys(password)
    lp.getLoginButton().click()


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
    time.sleep(2)
    driver.get('http://mail.126.com')
    login(driver, "w465898125", "Wen11281128#m")
