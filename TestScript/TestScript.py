import sys

sys.path.append("C:\\Users\\v_lvjichao\\PycharmProjects\\dataDrivenTestPractice")

from Action.AddContact import *
from Util.Excel import *

# driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
if __name__ == '__main__':

    driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
    driver.get('http://mail.126.com')
    pe = parseExcel("C:\\Users\\v_lvjichao\\PycharmProjects\\dataDrivenTestPractice\\TestData\\126mail.xlsx")
    pe.set_sheet_by_name(u"126账号")
    print(pe.get_default_sheet())
    rows = pe.get_all_rows()[1:]
    for id, row in enumerate(rows):
        if row[4].value == 'y':
            username = row[1].value
            password = row[2].value
            print(username, password)
            try:
                login(driver, username, password)
                pe.set_sheet_by_name(u"联系人")
                print(pe.get_default_sheet())
                rows1 = pe.get_all_rows()[1:]
                print(rows1)

                for id1, row1 in enumerate(rows1):
                    if row1[7].value == 'y':
                        try:
                            add_contact(driver, row1[1].value, row1[2].value, row1[3].value, row1[4].value,
                                        row1[5].value)
                            result = row1[6].value in driver.page_source
                            print(result)
                            print(row1[6].value)
                            pe.write_cell_current_time(id1 + 2, 9)
                            pe.write_cell_content(id1 + 2, 10, "pass")
                        except Exception as e:
                            print(u"异常信息:", e)
                            pe.write_cell_current_time(id1 + 2, 9)
                            pe.write_cell_content(id1 + 2, 10, "fail")
                    else:
                        pe.write_cell_current_time(id1 + 2, 9)
                        pe.write_cell_content(id1 + 2, 10, "忽略")
                        continue
            except Exception as e:
                pe.set_sheet_by_name("126账号")
                print(u"异常信息:", e)
                pe.write_cell_content(id + 2, 5, "fail")
        else:
            pe.set_sheet_by_name(u"126账号")
            pe.write_cell_content(id + 2, 5, "忽略")
