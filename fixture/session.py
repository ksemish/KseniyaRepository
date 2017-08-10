
class SessionHelper:

    def __init__(self, appgroup):
        self.appgroup = appgroup

    def login(self, user, pas):
        wd = self.appgroup.wd
        self.appgroup.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pas)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.appgroup.wd
        wd.find_element_by_link_text("Logout").click()