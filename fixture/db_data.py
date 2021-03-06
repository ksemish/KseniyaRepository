import mysql.connector
from models.group import Group
from models.contact import Contacts
from fixture.contacts import ContactHelper

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, phone2, mobile, work, home, email, email2, email3"
                           " from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, phone2, mobile, work, home, email, email2, email3) = row
                all_phones = home+mobile+work+phone2
                all_emails = email+email2+email3
                new_contact = ContactHelper.clean_spaces(Contacts(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                     all_phones_from_home_page=all_phones,
                                     all_emails_from_home_page=all_emails))

                list.append(new_contact)
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self):
        list_adreesses = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list_adreesses.append(Contacts(id=str(id), group_id=group_id))
        finally:
            cursor.close()
        return list_adreesses

    def destroy(self):
        self.connection.close()