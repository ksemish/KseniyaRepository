from models.group import Group

def test_edit_first_group(app):
    app.groups.edit_first_group(Group(name="edit name"))
