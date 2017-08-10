# -*- coding: utf-8 -*-

import pytest
from contact import Contacts
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_NewContact(app):
        success = True
        app.login("admin", "secret")
        app.fill_contact_form(Contacts("User", "Test", "New", "New Test User", "New Company", "Address new company", "12345", "4567", "789", "234", "one@gmail.com", "two@gmail.com", "three@gmail.com", "secondary address", "home address", "comments"))
        app.logout()
