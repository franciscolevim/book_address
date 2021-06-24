import utils.attributes_values as utilsattr
import re


class Telephone:
	"""Saves the data of a telephone record."""
	
	__NUMBER_PATTERN = r'^[\(]?(\+?[0-9]{2,3})?[\)]?([0-9]{2,3}[^0-9a-zA-Z\n]?){3,5}[0-9]*$'

	__id = 0
	__telephone_number = ''
	__description = None


	def __init__(self, id, telephone_number, description=None):
		"""
		Args:
			id(int)
			telephone_number(str)
			description(str) - Is Optional
		"""		
		self.id = id
		self.telephone_number = telephone_number #
		self.description = description


	def __str__(self):
		return f'{"{"}id:{self.id}, ' \
			+ f'telephone_number:{self.telephone_number}, ' \
			+ f'description:{utilsattr.parse_attribute_to_string(self.description)}{"}"}'


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
		utilsattr.validate_mandatory_attribute(id)
		utilsattr.validate_positive_int_attribute(id)
		self.__id = id


	@property
	def telephone_number(self):
		"""Telephone number."""
		return self.__telephone_number
	@telephone_number.setter
	def telephone_number(self, telephone_number):
		utilsattr.validate_mandatory_str_attribute(telephone_number)
		self.__validate_telephone_number(telephone_number)
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
