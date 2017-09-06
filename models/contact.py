from sys import maxsize

class Contacts:
   def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homeaddress=None, homephone=None, notes=None, id =None,
                all_phones_from_home_page=None, all_emails_from_home_page=None):
      self.firstname = firstname
      self.middlename = middlename
      self.lastname = lastname
      self.nickname = nickname
      self.company = company
      self.address = address
      self.home = home
      self.mobile = mobile
      self.work = work
      self.fax = fax
      self.email = email
      self.email2 = email2
      self.email3 = email3
      self.homeaddress = homeaddress
      self.homephone = homephone
      self.notes = notes
      self.id = id
      self.all_phones_from_home_page = all_phones_from_home_page
      self.all_emails_from_home_page = all_emails_from_home_page

   def __repr__(self):
      return "%s: %s: %s %s: %s: %s: %s: %s: %s: %s: %s: %s: %s: %s: %s: %s: %s:" \
             % (self.id, self.lastname, self.firstname, self.middlename, self.nickname,
                self.company, self.address, self.home, self.mobile, self.work, self.fax,
                self.email, self.email2, self.email3, self.homeaddress, self.homephone, self.notes)

   def __eq__(self, other):
      return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

   def contact_id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize