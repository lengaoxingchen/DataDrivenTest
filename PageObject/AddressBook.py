import time
import traceback

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.LoginPage import LoginPage
from Action.Login import *


class AddressBook(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.address_book_page = self.parse_config_file.getItemSection("126mail_homepage")
        print(self.address_book_page)
        self.address_book_page_items = self.parse_config_file.getItemSection("126mail_add_contact_page")
        print(self.address_book_page_items)

    def add_contact(self):
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            address_book_link = wait.until(lambda x: x.find_element_by_xpath("//div[text()='通讯录']"))
            address_book_link.click()
            time.sleep(2)
            add_contact_button = wait.until(lambda x: x.find_element_by_xpath("//span[text()='新建联系人']"))
            add_contact_button.click()
            contact_name = wait.until(
                lambda x: x.find_element_by_xpath("//a[@title='编辑详细姓名']/preceding-sibling::div/input"))
            contact_name.send_keys("徐凤钗")
            contact_email = wait.until(lambda x: x.find_element_by_xpath("//*[@id='iaddress_MAIL_wrap']//input"))
            contact_email.send_keys("593152023@qq.com")
            contact_is_star = wait.until(
                lambda x: x.find_element_by_xpath("//span[text()='设为星标联系人']/preceding-sibling::span/b"))
            contact_is_star.click()
            contact_mobile = wait.until(lambda x: x.find_element_by_xpath("//*[@id='iaddress_TEL_wrap']//input"))
            contact_mobile.send_keys("18141134488")
            contact_other_info = wait.until(lambda x: x.find_element_by_xpath("//textarea"))
            contact_other_info.send_keys("my wife")
            contact_save_button = wait.until(lambda x: x.find_element_by_xpath("//span[.='确 定']"))
            contact_save_button.click()
            time.sleep(2)

        except TimeoutException as e:
            print(traceback.print_exc())

        except NoSuchElementException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())

    def address_book_link(self):
        locateType, locateExpression = self.address_book_page['home_page.address_book'].split('>')
        contactBtn = getElement(self.driver, locateType, locateExpression)
        return contactBtn

    def add_contact_button(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.createcontactsbtn'].split('>')
        contactBtn = getElement(self.driver, locateType, locateExpression)
        return contactBtn

    def contact_name(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersonname'].split('>')
        contactName = getElement(self.driver, locateType, locateExpression)
        return contactName

    def contact_email(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.cotactpersonemail'].split('>')
        concatEmail = getElement(self.driver, locateType, locateExpression)
        return concatEmail

    def contact_is_star(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.starcontacts'].split('>')
        starContact = getElement(self.driver, locateType, locateExpression)
        return starContact

    def contact_mobile(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersonmobile'].split('>')
        concatMobile = getElement(self.driver, locateType, locateExpression)
        return concatMobile

    def contact_other_info(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersoncomment'].split('>')
        contactComment = getElement(self.driver, locateType, locateExpression)
        return contactComment

    def contact_save_button(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.savecontactperson'].split('>')
        contactBtn = getElement(self.driver, locateType, locateExpression)
        return contactBtn


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
    driver.get('http://mail.126.com')
    login(driver, "w465898125", "Wen11281128#m")
    ab = AddressBook(driver)
    ab.address_book_link().click()
    time.sleep(2)
    ab.add_contact_button().click()
    ab.contact_name().send_keys("徐凤钗")
    ab.contact_email().send_keys("593152023@qq.com")
    ab.contact_is_star().click()
    ab.contact_mobile().send_keys("18141134488")
    ab.contact_other_info().send_keys("my wife")
    ab.contact_save_button().click()
    time.sleep(2)
    login.logout()
