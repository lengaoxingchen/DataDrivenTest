import traceback

from selenium import webdriver
import time

from Util.ParsePageObjectRepository import *

from Util.ObjectMap import *


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.login_page_items = self.parse_config_file.getItemSection("126mail_login")
        print(self.login_page_items)
        self.wait = WebDriverWait(self.driver, 10, 0.2)

    def login(self):
        self.driver.switch_to.frame(self.getFrame())
        self.getUserName().clear()
        self.getUserName().send_keys("w465898125")
        self.getPassword().send_keys("Wen11281128#m")
        self.getLoginButton().click()

    def getFrame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split('>')
        frame = getElement(self.driver, locateType, locateExpression)
        return frame

    def getUserName(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split('>')
        userName = getElement(self.driver, locateType, locateExpression)
        return userName

    def getPassword(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split('>')
        password = getElement(self.driver, locateType, locateExpression)
        return password

    def getLoginButton(self):
        locateType, locateExpression = self.login_page_items['login_page.login_button'].split('>')
        loginButton = getElement(self.driver, locateType, locateExpression)
        return loginButton

    def logout(self):
        wait = WebDriverWait(self.driver, 10, 0.2)
        logout_link = wait.until(lambda x: x.find_element_by_xpath("//a[text()='退出']"))
        logout_link.click()


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
    driver.get('http://mail.126.com')
    login = LoginPage(driver)
    login.login()
    driver.switch_to.default_content()
    time.sleep(5)
    assert u"退出" in driver.page_source, "no exist in page_source"
