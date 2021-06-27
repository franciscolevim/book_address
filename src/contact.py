import utils.attributes_values as utilsattr
from address import Address
from telephone import Telephone


class Contact:
	"""Saves the data of a contact record."""


	__id = 0
	__name = ''
	__last_name = ''
	__birth_date = None
	__telephones = None
	__addresses = None


	def __init__(self, id, name , last_name, birth_date=None, telephones=[], addresses=[]):
		"""
		Args:
			id(int)
			name(str)
			lats_name(str)
			birth_date(str) - Is Optional
			telephones(list) - Is Optional
			addresses(list) - Is Optional
		"""
		self.id = id
		self.name = name
		self.last_name = last_name
		self.birth_date = birth_date
		self.telephones = telephones
		self.addresses = addresses


	def __str__(self):
		return f'{"{"}id:{self.id}, ' \
			+ f'name:{self.name}, ' \
			+ f'last_name:{self.last_name}, ' \
			+ f'birth_date:{utilsattr.parse_datetime_to_str(self.birth_date)}, ' \
			+ f'telephones:[{utilsattr.parse_attribute_to_string(self.telephones)}], ' \
			+ f'addresses:[{utilsattr.parse_attribute_to_string(self.addresses)}]{"}"}'


	@property
	def id(self):
		"""Identifier of the contact record."""
		return self.__id
	@id.setter
	def id(self, id):
		utilsattr.validate_mandatory_attribute(id)
		utilsattr.validate_positive_int_attribute(id)
		self.__id = id


	@property
	def name(self):
		"""Contact name."""
		return self.__name
	@name.setter
	def name(self, name):
		utilsattr.validate_mandatory_str_attribute(name)
		self.__name = name


	@property
	def last_name(self):
		"""Contact last name."""
		return self.__last_name
	@last_name.setter
	def last_name(self, last_name):
		utilsattr.validate_mandatory_str_attribute(last_name)
		self.__last_name = last_name


	@property
	def birth_date(self):
		"""Contact birth date."""
		return utilsattr.parse_datetime_to_str(self.__birth_date)
	@birth_date.setter
	def birth_date(self, birth_date):
		utilsattr.validate_datetime_attribute(birth_date)
		self.__birth_date = utilsattr.parse_str_to_datetime(birth_date)


	@property
	def telephones(self):
		"""List of telephones records."""
		return self.__telephones
	@telephones.setter
	def telephones(self, telephones):
		self.__telephones = telephones


	@property
	def addresses(self):
		"""List of addresses records."""
		return self.__addresses
	@addresses.setter
	def addresses(self, addresses):
		self.__addresses = addresses
