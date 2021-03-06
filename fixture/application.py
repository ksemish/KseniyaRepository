from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contacts import ContactHelper
from fixture.groups import GroupHelper


class Application:

    def __init__(self, browser, base_url):
        print(browser)
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
            print("chrome")
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.groups = GroupHelper(self)
        self.contacts = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()