from models.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groups.create(Group(name="Group for modify"))
    old_groups = db.get_group_list()
    randomgroups = random.choice(old_groups)
    index = old_groups.index(randomgroups)
    group = Group(id=randomgroups.id, name="edit name", header="edit header", footer="edit footer")
    app.groups.edit_group_by_id(randomgroups.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.groups.get_group_list(), key=Group.id_or_max)



