from PageObject.AddressBook import *
from selenium import webdriver


def add_contact(driver, name="", email="", is_star=True, mobile="", other_info=""):
    time.sleep(2)
    driver.switch_to.default_content()
    address_book = AddressBook(driver)
    address_book.address_book_link().click()
    address_book.add_contact_button().click()
    address_book.contact_name().send_keys(name)
    address_book.contact_email().send_keys(email)
    if is_star:
        address_book.contact_is_star().click()
    address_book.contact_mobile().send_keys(mobile)
    address_book.contact_other_info().send_keys(other_info)
    address_book.contact_save_button().click()


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
    driver.get('http://mail.126.com')
    login(driver, "w465898125", "Wen11281128#m")
    add_contact(driver, "daimen", "323432434@qq.com", True, "12323456567", "saddsf")
