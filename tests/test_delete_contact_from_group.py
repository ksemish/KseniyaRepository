from models.contact import Contacts
import random


def test_delete_contact_from_group(app):
    result = []
    group_id = app.contacts.choose_random_group_id()
    group_contacts = app.contacts.get_contacts_in_group(group_id)
    if len(group_contacts) == 0:
        result = app.contacts.add_random_contact_into_group(group_id)
    else:
        random_contact_id = random.choice(group_contacts)
        result = [group_id, random_contact_id]

    app.contacts.test_delete_contact_from_group(result[0], result[1])
