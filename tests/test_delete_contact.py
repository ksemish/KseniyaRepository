
def test_delete_first_contact(app):
    success = True
    app.session.login(user="admin", pas="secret")
    app.contacts.test_delete_first_contact()
    app.session.logout()

