from models.contact import Contacts
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create_contact(Contacts(lastname="LastNameUser", firstname="User Modify"))
    old_contacts = db.get_contact_list()
    randomcontact = random.choice(old_contacts)
    index = old_contacts.index(randomcontact)
    contact = Contacts(id=randomcontact.id, lastname="Lastname", firstname="ModifyFirstname")
    app.contacts.test_edit_contact_by_id(randomcontact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    # assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.contact_id_or_max) == sorted(app.contacts.get_contact_list(), key=Contacts.contact_id_or_max)