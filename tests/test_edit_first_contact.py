from models.contact import Contacts

def test_edit_first_contact(app):
    if app.contacts.count_contact() == 0:
        app.contacts.create_contact(Contacts(firstname = "User Modify"))
    app.contacts.test_edit_first_contact(Contacts(firstname="User EDIT"))

