from models.contact import Contacts
import time


def test_delete_first_contact(app):
    if app.contacts.count_contact() == 0:
        app.contacts.create_contact(Contacts(firstname="User Deleted"))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.test_delete_first_contact()
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts