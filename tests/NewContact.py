from models.contact import Contacts
from data.data_for_contacts import constant as testdata
import pytest



def test_NewContact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count_contact()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)