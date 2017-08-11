from models.group import Group

def test_edit_first_group(app):
    success = True
    app.session.login(user="admin", pas="secret")
    app.groups.edit_first_group(Group(name="edit name", header="edit logo", footer="edit comment"))
    app.session.logout()