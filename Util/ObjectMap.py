from selenium.webdriver.support.ui import WebDriverWait


# 获取单个元素对象
def getElement(driver, locateType, locateExpression):
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by=locateType, value=locateExpression))
        return element
    except Exception as e:
        raise e


# 获取多个元素对象
def getElements(driver, locateType, locateExpression):
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=locateType, value=locateExpression))
        return element
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "xpath", "//input[@id='kw']")
    print(searchBox)
    driver.quit()
