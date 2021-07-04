from address import Address
from telephone import Telephone
from contact import Contact
from database import DataBase

import utils.attributes_values as utilsattr
import constants
import json
import socket


def thread_client(connection, direction):
	"""It processes the client's requests and sends them the response.

	Args:
		connection (socket) - Client socket.
		direction (str) - Direction client data.
	"""
	end = False
	while not end:
		try:
			request = connection.recv(1024).decode('utf-8')
			print(f'Request: {request}')
			response = process_request(request)
			if response == constants.EXIT:
				end = True
				response = json.dumps({'code':response}, ensure_ascii=False)
			connection.send(str.encode(response))
		except Exception as e:
			print(f'ERROR: Thread client from {direction}.\n{e}')
			end = True
	connection.close()


def process_request(request):
	"""It processes the client's request and returns the response.
	
	Args:
		request (str) - JSON client request.

	Returns: 
		(str) - Data generated for the client.
	"""
	try:
		request = json.loads(request)
		if request['command'] == constants.FIND_CONTACT: 
			return find_contact(request['parameters'])
		elif request['command'] == constants.CREATE_CONTACT:
			return create_contact(request['contact'])
		elif request['command'] == constants.DELETE_CONTACT:
			return delete_contact(request['parameters'])
		elif request['command'] == constants.FIND_ALL_CONTACT:
			return find_all_contacts()
		elif request['command'] == constants.EXIT:
			return request['command'] 
		else:
			return ''
	except Exception as e:
		print(f'ERROR: Processing request.\n{e}')
		return json.dumps({'code': '0'}, ensure_ascii=False)


def create_contact(contact_json):
	"""Saves the new contact data.
	
	Args:
		contact_json (str) - JSON with the new contact data.
			"contact": {
				"id": 0,
				"name": "Dorotea",
				"last_name": "Martinez",
				"birth_date": "22-08-1930",
				"telephones": [
				  {
				    "id": 0,
				    "telephone_number": "5512546702",
				    "description": "Casa"
				  }
				],
				"addresses": [
				  {
				    "id": 0,
				    "street": "New York",
				    "floor": "303A",
				    "city": "Ciudad de México",
				    "zip_code": "08900"
				  }
				]
			}

	Returns: 
		(str) - Whether the creation was successful or not.
			- Successful {"code": 1} 
			- Unsuccessful {"code": 0} 
	"""
	contact = Contact.load_from_map(contact_json)
	database = DataBase()
	if database.save_contact(contact):
		return json.dumps({'code': '1'}, ensure_ascii=False)
	else:
		return json.dumps({'code': '0'}, ensure_ascii=False)


def find_all_contacts():
	"""Retrieves the data of all contacts.

	Returns: 
		(str) - The data of all contacts or the failed response.
			- Successful 
				{
				  "code": "1",
				  "contacts": [
				    {
				      "id": 5,
				      "name": "Sayaka",
				      "last_name": "Miki",
				      "birth_date": "15-02-2010",
				      "telephones": [
				        {
				          "id": 4,
				          "telephone_number": "5567432109",
				          "description": "Personal"
				        }
				      ],
				      "addresses": [
				        {
				          "id": 5,
				          "street": "Colinas de Ensenada",
				          "floor": "588D",
				          "city": "Ixtapaluca",
				          "zip_code": "53536"
				        }
				      ]
				    }
				  ]
				}

			- Unsuccessful 
				{"code": 0} 
	"""
	database = DataBase()
	contacts = database.read_contacts()
	if len(contacts) > 0:
		result_map = {
			'code': '1'
			, 'contacts': [contact.to_map() for contact in contacts]
		}
		return  json.dumps(result_map, ensure_ascii=False)
	else:
		return json.dumps({'code':'0'}, ensure_ascii=False)


def find_contact(json_request):
	"""Retrieves the data of the contacts that meet the search parameters.
	
	Args:
		json_request (str) - JSON with the contact data: {"name": "Emilia", "telephone": "5412980051"}

	Returns: 
		(str) - The data of all contacts that meet the search parameters or the failed response.
			- Successful 
				{
				  "code": "1",
				  "contacts": [
				    {
				      "id": 5,
				      "name": "Sayaka",
				      "last_name": "Miki",
				      "birth_date": "15-02-2010",
				      "telephones": [
				        {
				          "id": 4,
				          "telephone_number": "5567432109",
				          "description": "Personal"
				        }
				      ],
				      "addresses": [
				        {
				          "id": 5,
				          "street": "Colinas de Ensenada",
				          "floor": "588D",
				          "city": "Ixtapaluca",
				          "zip_code": "53536"
				        }
				      ]
				    }
				  ]
				}

			- Unsuccessful {"code" : 0} 
	"""
	database = DataBase()
	contacts = []
	if json_request['name'] and json_request['name'].strip() != '':
		contacts = database.read_contacts_with_name(json_request['name'])
	elif json_request['telephone'] and json_request['telephone'].strip() != '':
		contacts = database.read_contacts_by_telephone_number(json_request['telephone'])
	if len(contacts) > 0:
		result_map = {
			'code': '1'
			, 'contacts': [contact.to_map() for contact in contacts]
		}
		return  json.dumps(result_map, ensure_ascii=False)
	else:
		return json.dumps({'code': '0'}, ensure_ascii=False)


def delete_contact(json_request):
	"""Delete the the contacts that meet the parameters.
	
	Args:
		contact_json (str) - JSON with the contact parameters: {"name": "Emilia", "telephone": "5412980051"}

	Returns: 
		(str) - Whether the creation was successful or not.
			- Successful {"code": 1} 
			- Unsuccessful {"code": 0} 
	"""	
	database = DataBase()
	contacts = []
	if json_request['name'] and json_request['name'].strip() != '':
		contacts = database.read_contacts_with_name(json_request['name'])
	elif json_request['telephone'] and json_request['telephone'].strip() != '':
		contacts = database.read_contacts_by_telephone_number(json_request['telephone'])
	for contact in contacts:
		if not database.delete_contact(contact.id):
			return json.dumps({'code': '0'}, ensure_ascii=False)
	return json.dumps({'code': '1'}, ensure_ascii=False)
