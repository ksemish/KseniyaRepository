from random import randrange
import re
from models.contact import Contacts

def test_contacts_on_home_page(app, db, check_ui):
    contacts_list_db = db.get_contact_list()
    contacts_list_web = app.contacts.get_contact_list()
    assert len(contacts_list_db) == len(contacts_list_web)
    if check_ui:
        for el_web in contacts_list_web:
            for el_db in contacts_list_db:
                if el_web.id == el_db.id:
                    assert el_web.firstname == el_db.firstname
                    assert el_web.lastname == el_db.lastname
                    assert el_web.address == el_db.address
                    assert el_web.all_emails_from_home_page == el_db.all_emails_from_home_page
                    assert el_web.all_phones_from_home_page == el_db.all_phones_from_home_page
                    break


# def test_contacts_on_home_page(app):
#     contacts_list = app.contacts.get_contact_list()
#     index = randrange(len(contacts_list))
#     contact_from_home_page = contacts_list[index]
#     contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

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