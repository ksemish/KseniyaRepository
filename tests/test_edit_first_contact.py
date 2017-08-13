from models.contact import Contacts

def test_edit_first_contact(app):
    app.contacts.test_edit_first_contact(Contacts("User EDIT", "Test EDIT", "New EDIT", "New Test User EDIT", " ", " ", " ",
                                                  " ", " ", " ", " ", " ", " ", " ", " ", " "))

