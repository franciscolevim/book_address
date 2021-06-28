import utils.attributes_values as utilsattr

import json


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
		return self.to_json()
			

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


	def to_map(self):
		"""Transform the data object in a map object."""
		return {
			'id':self.id
			,'street':self.street
			,'floor':self.floor
			,'city':self.city
			,'zip_code':self.zip_code
		}
		

	def to_json(self):
		"""Transform the data object in a json object."""
		return json.dumps(self.to_map(), ensure_ascii=False)


	@staticmethod
	def load_from_map(map_data):
		"""Transform a map object in a Address object."""
		return Address(
			id=map_data['id']
			, street=map_data['street']
			, floor=map_data['floor']
			, city=map_data['city']
			, zip_code=map_data['zip_code'])
	

	@staticmethod
	def load_from_json(json_data):
		"""Transform a json object in a Address object."""
		return Address.load_from_map(json.loads(json_data))
