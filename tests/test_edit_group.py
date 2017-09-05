from models.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.groups.count_groups() == 0:
        app.groups.create(Group(name="Group for modify"))
    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edit name")
    group.id = old_groups[index].id
    app.groups.edit_group_by_index(index, group)
    new_groups = app.groups.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

