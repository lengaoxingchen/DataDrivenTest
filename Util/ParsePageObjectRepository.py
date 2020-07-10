from configparser import ConfigParser
from Projectar.var import page_object_repository_path


class ParsePageObjectRepositoryConfig(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(page_object_repository_path, encoding='utf-8')

    def getItemSection(self, sectionName):
        print(self.cf.items(sectionName))
        return dict(self.cf.items(sectionName))

    def getOptionValue(self, sectionName, optionValue):
        print(self.cf.get(sectionName, optionValue))
        return self.cf.get(sectionName, optionValue)


if __name__ == '__main__':
    pp = ParsePageObjectRepositoryConfig()
    print(pp.getItemSection("126mail_login"))
    print(pp.getOptionValue("126mail_login", "login_page.username"))
