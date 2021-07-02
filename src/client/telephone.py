import utils.attributes_values as utilsattr

import re
import json


class Telephone:
	"""Saves the data of a telephone record."""
	
	__NUMBER_PATTERN = r'^[\(]?(\+?[0-9]{2,3})?[\)]?([0-9]{2,3}[^0-9a-zA-Z\n]?){3,5}[0-9]*$'

	__id = None
	__telephone_number = None
	__description = None


	def __init__(self):
		""" 
		"""		
		self.id = 0
		self.telephone_number = ''
		self.description = None


	def __str__(self):
		return utilsattr.to_json(self)


	@property
	def NUMBER_PATTERN(self):
		"""Telephone number pattern to regular expressions: ^\\+?([0-9]{2,3}[^0-9a-zA-Z\\n]?){3,5}[0-9]*$."""
		return self.__NUMBER_PATTERN


	@property
	def id(self):
		"""Identifier of the telephone record."""
		return self.__id
	@id.setter
	def id(self, id):
		self.__id = id


	@property
	def telephone_number(self):
		"""Telephone number."""
		return self.__telephone_number
	@telephone_number.setter
	def telephone_number(self, telephone_number):
		self.__telephone_number = telephone_number


	@property
	def description(self):
		"""Description of the telephone record."""
		return self.__description
	@description.setter
	def description(self, description):
		self.__description = description


	def __validate_telephone_number(self, telephone_number):
		"""Validate if a telephone number is valid.
		
		Args:
			telephone_number

		Throws: 
			AttributeError - If the telephone number isn\'t valid.
		"""
		if not re.search(self.NUMBER_PATTERN, telephone_number):
			message = f'the telephone number isn\'t valid: {telephone_number}'
			raise AttributeError(message)


	def to_map(self):
		"""Transform the data object in a map object."""
		return {
			'id':self.id
			,'telephone_number':self.telephone_number
			,'description':self.description
		}


	@staticmethod
	def load_from_map(map_data):
		"""Transform a map object in a Telephone object."""
		telephone = Telephone()
		telephone.id = map_data['id']
		telephone.telephone_number = map_data['telephone_number']
		telephone.description = map_data['description']
		return telephone
	

	@staticmethod
	def load_from_json(json_data):
		"""Transform a json object in a Telephone object."""
		return Telephone.load_from_map(json.loads(json_data))
