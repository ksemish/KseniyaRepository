

def test_delete_first_group(app):
    success = True
    app.session.login(user="admin", pas="secret")
    app.groups.delete_first_group()
    app.session.logout()