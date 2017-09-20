from models.contact import Contacts
import random
import string


constant = [
    Contacts(firstname="firstname1", middlename="middlename1", lastname="lastname1"),
    Contacts(firstname="firstname2", middlename="middlename2", lastname="lastname2")
]

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def generate_contact_info(symbols_count=10):
#     params = {}
#     keys = ['firstname', 'middlename', 'lastname', 'nickname', 'company',
#             'address', 'home', 'mobile', 'work', 'fax',
#             'email', 'email2', 'email3', 'homeaddress', 'homephone', 'notes']
#     for key in keys:
#         params[key] = random_string('', symbols_count)
#     return params
#
# testcontact = Contacts(**generate_contact_info())
#
# testdata = [Contacts(firstname="", middlename="", lastname="")] + [
#     Contacts(**generate_contact_info())
#     for i in range(5)
# ]
