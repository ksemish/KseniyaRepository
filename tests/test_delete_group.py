from models.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.groups.count_groups() == 0:
        app.groups.create(Group(name="TEST"))
    old_groups = app.groups.get_group_list()
    index = randrange(len(old_groups))
    app.groups.delete_group_by_index(index)
    new_groups = app.groups.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups