from models.contact import Contacts
from random import randrange

def test_edit_some_contact(app):
    if app.contacts.count_contact() == 0:
        app.contacts.create_contact(Contacts(firstname="User Modify"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contacts(firstname="ModifyFirstname", lastname="ModifyLastname")
    contact.id = old_contacts[index].id
    app.contacts.test_edit_contact_by_index(index, contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)


