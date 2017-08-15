from models.group import Group

def test_delete_first_group(app):
    if app.groups.count_groups() == 0:
        app.groups.create(Group(name="TEST"))
    app.groups.delete_first_group()