import mysql.connector
from fixture.db_data import DbFixture

db = DbFixture(host="localhost", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_in_group()
    for contact in contacts:
            print("Contact id: " + str(contact.id) + ", group id: " + str(contact.group_id) )
    print(len(contacts))
finally:
    db.destroy()