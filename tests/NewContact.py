from models.contact import Contacts
from sys import maxsize

def test_NewContact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts("Firstname", "Name", "Lastname", "New Test User",
                                            "New Company", "Address new company", "12345",
                                            "4567", "789", "234", "one@gmail.com", "two@gmail.com",
                                            "three@gmail.com", "secondary address", "home address", "comments")
    app.contacts.create_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)

def test_empty_NewContact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts("", "", "")
    app.contacts.create_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)