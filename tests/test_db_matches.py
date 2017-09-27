
from fixture.groups import Group
from timeit import timeit

# def test_group_list(app, db):
#     print(timeit(lambda : app.groups.get_group_list(), number=1))
#
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#     print(timeit(lambda:  map(clean, db.get_group_list()), number=1000))
#     assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def get_contact_in_group(app, db):
        print(timeit(lambda: app.groups.get_group_list(), number=1))

        def clean(group):
            return Group(id=group.id, name=group.name.strip())

        print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
        assert False  # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
