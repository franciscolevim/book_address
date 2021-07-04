from address import Address
from telephone import Telephone
from contact import Contact
from database import DataBase

import utils.attributes_values as utilsattr

import json
import socket


def thread_client(connection, direction):
	end = False
	while not end:
		try:
			recived = connection.recv(1024)
			recived = recived.decode('utf-8')
			print('Command recived: ', recived)
			message = process_message(recived)
			if message == 5:
				end = True
				message = json.dumps({'code':message}, ensure_ascii=False)
			connection.send(str.encode(message))
		except Exception as e:
			print('ERROR: Thread client')
			end = True
	connection.close()


def process_message(message):
	try:
		messages = json.loads(message)
		if messages['command'] == 1:
			return find_contact(messages['parameters'])
		elif messages['command'] == 2:
			return create_contact(messages['contact'])
		elif messages['command'] == 3:
			return delete_contact(messages['parameters'])
		elif messages['command'] == 4:
			return find_all_contacts()
		elif messages['command'] == 5:
			return messages['command'] 
		else:
			return ''
	except Exception as e:
		print('ERROR: Processing the recived message.')
		return json.dumps({'code':'0'}, ensure_ascii=False)


def create_contact(contact_json):
	contact = Contact.load_from_map(contact_json)
	database = DataBase()
	if database.save_contact(contact):
		return json.dumps({'code':'1'}, ensure_ascii=False)
	else:
		return json.dumps({'code':'0'}, ensure_ascii=False)


def find_all_contacts():
	database = DataBase()
	contacts = database.read_contacts()
	if len(contacts) > 0:
		result_map = {
			'code':'1'
			, 'contacts':[contact.to_map() for contact in contacts]
		}
		return  json.dumps(result_map, ensure_ascii=False)
	else:
		return json.dumps({'code':'0'}, ensure_ascii=False)


def find_contact(json_request):	
	database = DataBase()
	contacts = []
	if json_request['name'] and json_request['name'].strip() != '':
		contacts = database.read_contacts_with_name(json_request['name'])
	elif json_request['telephone'] and json_request['telephone'].strip() != '':
		contacts = database.read_contacts_by_telephone_number(json_request['telephone'])
	if len(contacts) > 0:
		result_map = {
			'code':'1'
			, 'contacts':[contact.to_map() for contact in contacts]
		}
		return  json.dumps(result_map, ensure_ascii=False)
	else:
		return json.dumps({'code':'0'}, ensure_ascii=False)


def delete_contact(json_request):
	database = DataBase()
	contacts = []
	if json_request['name'] and json_request['name'].strip() != '':
		contacts = database.read_contacts_with_name(json_request['name'])
	elif json_request['telephone'] and json_request['telephone'].strip() != '':
		contacts = database.read_contacts_by_telephone_number(json_request['telephone'])
	for contact in contacts:
		if not database.delete_contact(contact.id):
			return json.dumps({'code':'0'}, ensure_ascii=False)
	return json.dumps({'code':'1'}, ensure_ascii=False)
