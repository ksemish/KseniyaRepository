from models.group import Group

def test_edit_first_group(app):
    if app.groups.count_groups() == 0:
        app.groups.create(Group(name="Group for modify"))
    app.groups.edit_first_group(Group(name="edit name"))
