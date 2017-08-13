# -*- coding: utf-8 -*-
from models.group import Group


def test_FullForm(app):
        app.groups.create(Group(name="name", header="logo", footer="comment"))

def test_EmptyForm(app):
        app.groups.create(Group(name="", header="", footer=""))