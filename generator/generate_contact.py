from models.contact import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits*10
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

testdata = [Contacts(firstname="", middlename="", lastname="", nickname="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="", homeaddress="",
                     homephone="", notes="")] + [
     Contacts(**generate_contact_info())
     for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
