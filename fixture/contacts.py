class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.wd

    def change_contact_field(self, contact_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(text)

    def create_contact(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contacts)
        # submit_create_contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_xpath("//div/div[4]/div/i/a[2]").click()

    def fill_contact_form(self, Contacts):
        wd = self.app.wd
        # fill name of contact
        self.change_contact_field("firstname", Contacts.firstname)
        self.change_contact_field("middlename", Contacts.middlename)
        self.change_contact_field("lastname", Contacts.lastname)
        self.change_contact_field("nickname", Contacts.nickname)
        # fill company information
        self.change_contact_field("company", Contacts.company)
        self.change_contact_field("address", Contacts.address_new_company)
        # fill contact information
        self.change_contact_field("home", Contacts.home)
        self.change_contact_field("mobile", Contacts.mobile)
        self.change_contact_field("work", Contacts.work)
        self.change_contact_field("fax", Contacts.fax)
        # fill email of contact
        self.change_contact_field("email", Contacts.email1)
        self.change_contact_field("email2", Contacts.email2)
        self.change_contact_field("email3", Contacts.email3)
        # fill homepage
        self.change_contact_field("homepage", "homepage.ru")
        # fill homeaddress
        self.change_contact_field("address2", Contacts.homeaddress)
        # fill homephone
        self.change_contact_field("phone2", Contacts.homephone)
        # fill comments
        self.change_contact_field("notes", Contacts.notes)


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def test_delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()

    def test_edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        # select contact
        self.select_first_contact()
        #submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill name of contact
        self.fill_contact_form(new_contact_data)
        # submit editing
        wd.find_element_by_name("update").click()
        # return to homepage
        wd.find_element_by_link_text("home page").click()

    def count_contact(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))



