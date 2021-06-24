import utils.attributes_values as utilsattr


class Address:
	"""Saves the data of a address record."""


	__id = 0
	__street = ''
	__floor = ''
	__city = ''
	__zip_code = None


	def __init__(self, id, street, floor, city, zip_code=None):
		"""
		Args:
			id(int)
			street(str)
			floor(str)
			city(str)
			zip_code(str) - Is Optional		
		"""
		self.id = id
		self.street = street
		self.floor = floor
		self.city = city
		self.zip_code = zip_code


	def __str__(self):
		return f'{"{"}id:{self.id}, ' \
			+ f'street:{self.street}, ' \
			+ f'floor:{self.floor}, ' \
			+ f'city:{self.city}, ' \
			+ f'zip_code:{utilsattr.parse_attribute_to_string(self.zip_code)}{"}"}'
			

	@property
	def id(self):
		"""Identifier of the address record."""
		return self.__id
	@id.setter
	def id(self, id):
		utilsattr.validate_mandatory_attribute(id)
		utilsattr.validate_positive_int_attribute(id)
		self.__id = id


	@property
	def street(self):
		"""Street name and number."""
		return self.__street
	@street.setter
	def street(self, street):
		utilsattr.validate_mandatory_str_attribute(street)
		self.__street = street


	@property
	def floor(self):
		"""Aditional information of the address."""
		return self.__floor
	@floor.setter
	def floor(self, floor):
		utilsattr.validate_mandatory_str_attribute(floor)
		self.__floor = floor


	@property
	def city(self):
		"""City name."""
		return self.__city
	@city.setter
	def city(self, city):
		utilsattr.validate_mandatory_str_attribute(city)
		self.__city = city


	@property
	def zip_code(self):
		"""City name."""
		return self.__zip_code
	@zip_code.setter
	def zip_code(self, zip_code):
		self.__zip_code = zip_code