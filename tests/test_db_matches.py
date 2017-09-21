
from fixture.groups import Group

def test_group_list(app, db):
    ui_list = app.groups.get_group_list()
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)