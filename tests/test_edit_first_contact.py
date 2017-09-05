from models.contact import Contacts

def test_edit_first_contact(app):
    if app.contacts.count_contact() == 0:
        app.contacts.create_contact(Contacts(firstname="User Modify"))
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(firstname="ModifyFirstname", lastname="ModifyLastname")
    contact.id = old_contacts[0].id
    app.contacts.test_edit_first_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.contact_id_or_max) == sorted(new_contacts, key=Contacts.contact_id_or_max)


