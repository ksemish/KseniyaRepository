from models.group import Group
from random import randrange
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groups.create(Group(name="TEST"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.groups.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.groups.get_group_list(), key=Group.id_or_max)
