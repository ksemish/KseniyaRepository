from models.contact import Contacts

def test_NewContact(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create_contact(Contacts("User", "Test", "New", "New Test User",
                                            "New Company", "Address new company", "12345",
                                            "4567", "789", "234", "one@gmail.com", "two@gmail.com",
                                            "three@gmail.com", "secondary address", "home address", "comments"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)