from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def login(self, user, passw):
            wd = self.wd
            wd.get("http://localhost/addressbook/index.php")
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(user)
            wd.find_element_by_id("content").click()
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(passw)
            wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
            wd.find_element_by_id("content").click()
            wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, Contacts):
            # fill name of contact
            wd = self.wd
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(Contacts.firstname)
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(Contacts.middlename)
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(Contacts.lastname)
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(Contacts.nickname)
            wd.find_element_by_name("theform").click()
            # fill company information
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(Contacts.company)
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(Contacts.address_new_company)
            # fill contact information
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(Contacts.home)
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(Contacts.mobile)
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(Contacts.work)
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(Contacts.fax)
            # fill email of contact
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(Contacts.email1)
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(Contacts.email2)
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(Contacts.email3)
            # fill homepage
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys("homepage.ru")
            # fill birhday date
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys("1990")
            # fill aniversary date
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").click()
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys("2013")
            # fill homeaddress
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(Contacts.homeaddress)
            # fill homephone
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(Contacts.homephone)
            # fill comments
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(Contacts.notes)
            # submit_create_contact
            wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
            wd.find_element_by_xpath("//div/div[4]/div/i/a[2]").click()

    def logout(self):
            wd = self.wd
            wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()