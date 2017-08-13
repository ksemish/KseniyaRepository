from models.contact import Contacts

def test_NewContact(app):
    app.contacts.fill_contact_form(Contacts("User", "Test", "New", "New Test User",
                                            "New Company", "Address new company", "12345",
                                            "4567", "789", "234", "one@gmail.com", "two@gmail.com",
                                            "three@gmail.com", "secondary address", "home address", "comments"))
