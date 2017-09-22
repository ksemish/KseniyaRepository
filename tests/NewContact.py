from models.contact import Contacts
from data.data_for_contacts import constant as testdata
import pytest



def test_NewContact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contacts.create_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)