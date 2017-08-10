# -*- coding: utf-8 -*-

import pytest
from group import Group
from GroupApplication import GroupApplication

@pytest.fixture
def appgroup(request):
    fixture = GroupApplication()
    request.addfinalizer(fixture.destroygrouptest)
    return fixture

def test_FullForm(appgroup):
        success = True
        appgroup.login(user="admin", pas="secret")
        appgroup.create_new_group(Group(name="name", header="logo", footer="comment"))
        appgroup.logout()

def test_EmptyForm(appgroup):
        success = True
        appgroup.login(user="admin", pas="secret")
        appgroup.create_new_group(Group(name="", header="", footer=""))
        appgroup.logout()

