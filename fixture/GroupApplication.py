from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class GroupApplication:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']//h1[.='Groups']").click()

    def create_new_group(self, Group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()


    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()


    def destroygrouptest(self):
        self.wd.quit()