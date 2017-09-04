from models.group import Group

def test_edit_first_group(app):
    if app.groups.count_groups() == 0:
        app.groups.create(Group(name="Group for modify"))
    old_groups = app.groups.get_group_list()
    group = Group(name="edit name")
    group.id = old_groups[0].id
    app.groups.edit_first_group(group)
    new_groups = app.groups.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

