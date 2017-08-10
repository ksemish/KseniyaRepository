# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application
from models.contact import Contacts


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_NewContact(app):
        success = True
        app.session.login("admin", "secret")
        app.contacts.fill_contact_form(Contacts("User", "Test", "New", "New Test User", "New Company", "Address new company", "12345", "4567", "789", "234", "one@gmail.com", "two@gmail.com", "three@gmail.com", "secondary address", "home address", "comments"))
        app.session.logout()
