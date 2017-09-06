from models.contact import Contacts
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        #if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("group")) > 0):
        #    wd.find_element_by_link_text("home").click()
        wd.get('http://localhost/addressbook/index.php')

    def change_contact_field(self, contact_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(text)

    def create_contact(self, Contacts):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contacts)
        # submit_create_contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_xpath("//div/div[4]/div/i/a[2]").click()
        self.contact_cache = None

    def fill_contact_form(self, Contacts):
        wd = self.app.wd
        # fill name of contact
        self.change_contact_field("firstname", Contacts.firstname)
        self.change_contact_field("middlename", Contacts.middlename)
        self.change_contact_field("lastname", Contacts.lastname)
        self.change_contact_field("nickname", Contacts.nickname)
        # fill company information
        self.change_contact_field("company", Contacts.company)
        self.change_contact_field("address", Contacts.address)
        # fill contact information
        self.change_contact_field("home", Contacts.home)
        self.change_contact_field("mobile", Contacts.mobile)
        self.change_contact_field("work", Contacts.work)
        self.change_contact_field("fax", Contacts.fax)
        # fill email of contact
        self.change_contact_field("email", Contacts.email)
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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def test_delete_first_contact(self):
        self.test_delete_contact_by_index(0)

    def test_delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cache = None

    # def test_edit_first_contact(self):
    #     self.test_edit_contact_by_index(0)

    def open_contact_edit_form(self, wd, index):
        self.open_contacts_page()
        # select contact
        self.select_contact_by_index(index)
        # submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a").click()

    def open_contact_view_page(self, wd, index):
        self.open_contacts_page()
        # select contact
        self.select_contact_by_index(index)
        # submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[7]/a").click()

    def test_edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_edit_form(wd, index)
        # fill name of contact
        self.fill_contact_form(new_contact_data)
        # submit editing
        wd.find_element_by_name("update").click()
        # return to homepage
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def count_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contacts(id=id, lastname=lastname, firstname=firstname, address=address,
                                                   all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_form(wd, index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        homephone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contacts(firstname=firstname, lastname=lastname, id=id, address=address,
                        email=email, email2=email2, email3=email3,
                        home=home,work=work, mobile=mobile, homephone=homephone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page(wd, index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        homephone = re.search("P: (.*)", text).group(1)
        return Contacts(home=home, work=work, mobile=mobile, homephone=homephone)

