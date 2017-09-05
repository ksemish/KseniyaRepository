# -*- coding: utf-8 -*-
from models.group import Group


def test_FullForm(app):
        old_groups = app.groups.get_group_list()
        group = Group(name="New group name", header="logo", footer="comment")
        app.groups.create(group)
        assert len(old_groups) + 1 == app.groups.count_groups()
        new_groups = app.groups.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_EmptyForm(app):
#         old_groups = app.groups.get_group_list()
#         group = Group(name="", header="", footer="")
#         app.groups.create(group)
#         new_groups = app.groups.get_group_list()
#         assert len(old_groups) + 1 == len(new_groups)
#         old_groups.append(group)
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)