from random import randrange
import re


def test_contacts_on_home_page(app):
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

# def test_phones_on_contact_view_page(app):
#     contacts_list = app.contacts.get_contact_list()
#     index = randrange(len(contacts_list))
#     view_contact = app.contacts.get_contact_from_view_page(index)
#     contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
#     assert view_contact.home == contact_from_edit_page.home
#     assert view_contact.mobile == contact_from_edit_page.mobile
#     assert view_contact.work == contact_from_edit_page.work
#     assert view_contact.homephone == contact_from_edit_page.homephone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.homephone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))