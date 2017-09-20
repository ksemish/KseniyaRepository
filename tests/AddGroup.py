# -*- coding: utf-8 -*-
from models.group import Group

def test_FullForm(app, json_groups):
        group = json_groups
        old_groups = app.groups.get_group_list()
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

# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#     for i in range(5)
# ]

# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]