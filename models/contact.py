from sys import maxsize
class Contacts:
   def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None,
                 address_new_company=None, home=None, mobile=None, work=None, fax=None, email1=None,
                 email2=None, email3=None, homeaddress=None, homephone=None, notes=None, id =None):
      self.firstname = firstname
      self.middlename = middlename
      self.lastname = lastname
      self.nickname = nickname
      self.company = company
      self.address_new_company = address_new_company
      self.home = home
      self.mobile = mobile
      self.work = work
      self.fax = fax
      self.email1 = email1
      self.email2 = email2
      self.email3 = email3
      self.homeaddress = homeaddress
      self.homephone = homephone
      self.notes = notes
      self.id = id

   def __repr__(self):
      return "%s:%s:s%" % (self.id, self.firstname, self.lastname)

   def __eq__(self, other):
      return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.name and self.lastname == other.name




