from models.contact import Contacts


def test_add_contact_into_group(app):
    group_id = app.contacts.choose_random_group_id()
    if len(app.contacts.get_contact_list()) == 0:
        app.contacts.create_contact(Contacts(lastname="LastNameUser", firstname="User Modify"))
    result = app.contacts.add_random_contact_into_group(group_id)
    app.contacts.contact_in_group(result)



