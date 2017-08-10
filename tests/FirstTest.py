# -*- coding: utf-8 -*-

import pytest

from fixture.GroupApplication import GroupApplication
from models.group import Group


@pytest.fixture
def appgroup(request):
    fixture = GroupApplication()
    request.addfinalizer(fixture.destroygrouptest)
    return fixture

def test_FullForm(appgroup):
        success = True
        appgroup.session.login(user="admin", pas="secret")
        appgroup.create_new_group(Group(name="name", header="logo", footer="comment"))
        appgroup.session.logout()

def test_EmptyForm(appgroup):
        success = True
        appgroup.session.login(user="admin", pas="secret")
        appgroup.create_new_group(Group(name="", header="", footer=""))
        appgroup.session.logout()


