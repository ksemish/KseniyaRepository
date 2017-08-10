# -*- coding: utf-8 -*-
from models.group import Group


def test_FullForm(app):
        success = True
        app.session.login(user="admin", pas="secret")
        app.groups.create(Group(name="name", header="logo", footer="comment"))
        app.session.logout()

def test_EmptyForm(app):
        success = True
        app.session.login(user="admin", pas="secret")
        app.groups.create(Group(name="", header="", footer=""))
        app.session.logout()


