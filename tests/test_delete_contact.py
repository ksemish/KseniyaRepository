from models.contact import Contacts

def test_delete_first_contact(app):
    if app.contacts.count_contact() == 0:
        app.contacts.create_contact(Contacts(firstname = "User Deleted"))
    app.contacts.test_delete_first_contact()

