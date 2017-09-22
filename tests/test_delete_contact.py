from models.contact import Contacts
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create_contact(Contacts(firstname="User Deleted"))
    old_contacts = db.get_contact_list()
    randomcontact = random.choice(old_contacts)
    app.contacts.test_delete_contact_by_id(randomcontact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(randomcontact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.contact_id_or_max) == sorted(app.contacts.get_contact_list(),
                                                                         key=Contacts.contact_id_or_max)
