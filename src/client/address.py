import utils.attributes_values as utilsattr

import json


class Address:
	"""Saves the data of a address record."""


	__id = None
	__street = None
	__floor = None
	__city = None
	__zip_code = None


	def __init__(self):
		"""
		"""
		self.id = 0
		self.street = ''
		self.floor = ''
		self.city = ''
		self.zip_code = None


	def __str__(self):
		return utilsattr.to_json(self)
			

	@property
	def id(self):
		"""Identifier of the address record."""
		return self.__id
	@id.setter
	def id(self, id):
		self.__id = id


	@property
	def street(self):
		"""Street name and number."""
		return self.__street
	@street.setter
	def street(self, street):
		self.__street = street


	@property
	def floor(self):
		"""Aditional information of the address."""
		return self.__floor
	@floor.setter
	def floor(self, floor):
		self.__floor = floor


	@property
	def city(self):
		"""City name."""
		return self.__city
	@city.setter
	def city(self, city):
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


	@staticmethod
	def load_from_map(map_data):
		"""Transform a map object in a Address object."""
		address = Address()
		address.id = map_data['id']
		address.street = map_data['street']
		address.floor = map_data['floor']
		address.city = map_data['city']
		address.zip_code = map_data['zip_code']
		return address
	

	@staticmethod
	def load_from_json(json_data):
		"""Transform a json object in a Address object."""
		return Address.load_from_map(json.loads(json_data))
