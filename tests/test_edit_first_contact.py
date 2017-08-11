from models.contact import Contacts

def test_edit_first_contact(app):
    success = True
    app.session.login(user="admin", pas="secret")
    app.contacts.test_edit_first_contact(Contacts("User EDIT", "Test EDIT", "New EDIT", "New Test User EDIT", " ", " ", " ",
                                                  " ", " ", " ", " ", " ", " ", " ", " ", " "))
    app.session.logout()

