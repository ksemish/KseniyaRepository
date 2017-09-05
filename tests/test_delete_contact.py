from models.contact import Contacts
from random import randrange

def test_delete_some_contact(app):
    if app.contacts.count_contact() == 0:
        app.contacts.create_contact(Contacts(firstname="User Deleted"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    app.contacts.test_delete_contact_by_index(index)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts