from models.contact import Contacts
from sys import maxsize

def test_NewContact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts("Firstname", "Name", "Lastname", "New Test User",
                       "New Company", "Address new company", "home - 8(495)777-77-77",
                       "work - 8(495)555-55-55", "mobile - 89034567890", "fax - 8(495)456 123 45",
                       "one@gmail.com", "two@gmail.com",
                       "three@gmail.com", "secondary address", "homephone - 8(495)456 123 45", "comments")
    app.contacts.create_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count_contact()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)

# def test_empty_NewContact(app):
#     old_contacts = app.contacts.get_contact_list()
#     contact = Contacts("", "", "")
#     app.contacts.create_contact(contact)
#     new_contacts = app.contacts.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)