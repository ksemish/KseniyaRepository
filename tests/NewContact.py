from models.contact import Contacts
from sys import maxsize
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def generate_contact_info(symbols_count=10):
    params = {}
    keys = ['firstname', 'middlename', 'lastname', 'nickname', 'company',
            'address', 'home', 'mobile', 'work', 'fax',
            'email', 'email2', 'email3', 'homeaddress', 'homephone', 'notes']

    for key in keys:
        params[key] = random_string('', symbols_count)

    return params

testcontact = Contacts(**generate_contact_info())

testdata = [Contacts(firstname="", middlename="", lastname="")] + [
    Contacts(**generate_contact_info())
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_NewContact(app, contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count_contact()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)