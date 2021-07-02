import datetime


DATE_FORMAT = '%d-%m-%Y'


def validate_mandatory_attribute(value):
	"""Validate if a value is mandatory.

	Args:
		value

	Throws: 
		AttributeError - If the attribute is a None value.
	"""
	if value is None:
		raise AttributeError('The attribute cannot have a None value.')


def validate_mandatory_str_attribute(value):
	"""Validate if a string value is mandatory.

	Args:
		value

	Throws: 
		AttributeError - If the attribute is an empty or None value.
	"""
	if value is None:
		raise AttributeError('The attribute cannot have a None value.')
	elif isinstance(value, str) and len(value.strip()) == 0:
		raise AttributeError('The attribute cannot have a None or empty value.')


def validate_positive_int_attribute(value):
	"""Validate if a value is a positive number.
	
	Args:
		value - Value of the attribute.

	Throws: 
		AttributeError - If the attribute value isn\'t a integer or is less than 1.
	"""
	message = 'The attribute must be an integer greater than zero.'
	if value and not isinstance(value, int):
		raise TypeError(message)
	elif value and value < 1:
		raise AttributeError(message)


def validate_datetime_attribute(value):
	"""Validate if a value is a datetime.
	
	Args:
		value - Value of the attribute.

	Throws: 
		AttributeError - If the attribute value isn\'t a datetime or str.
	"""
	if value and not isinstance(value, datetime.datetime) and not isinstance(value, str):
		raise TypeError('The attribute must be an datetime or str.')


def parse_str_to_datetime(value):
	"""Convert a string value in datetime object with the DATE_FORMAT.

	Args:
		value - Value of the string.

	Returns: 
		datetime.
	"""
	return datetime.datetime.strptime(value, DATE_FORMAT) if value and isinstance(value, str) else value


def parse_datetime_to_str(value):
	"""Convert a datetime value in str with the DATE_FORMAT.

	Args:
		value - Value of the datetime.

	Returns: 
		str. String datetime value
	"""
	return value.strftime(DATE_FORMAT) if value and isinstance(value, datetime.datetime) else value


def to_json(object):
	"""Transform the data object in a json object."""
	return json.dumps(object.to_map(), ensure_ascii=False)


