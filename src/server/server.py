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
			if recived == '5':
				end = True
			message = str(process_message(recived))
			connection.send(str.encode(message))
		except:
			print('ERROR: Thread client')
			end = True
	connection.close()


def process_message(message):
	try:
		messages = json.loads(message)
		if messages['command'] == '1':
			return find_contact(messages['parameters'])
		elif messages['command'] == '2':
			return create_contact(messages['contact'])
		elif messages['command'] == '3':
			return delete_contact(messages['parameters'])
		elif messages['command'] == '4':
			return find_all_contacts()
	except:
		print('ERROR: Processing the recived message.')
		return ''


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


def main():
	#json_request = json.loads('{"command": "1", "parameters": {"name":"Dorotea", "telephone":""}}')
	json_request = json.loads('{"command": "1", "parameters": {"name":"", "telephone":"5568790013"}}')
	#result = find_contact(json_request)
	#json_request = json.loads(' {"command": "2", "contact": '\
	#	+ '{"id": 0, "name": "Dorotea", "last_name": "Martinez", "birth_date": "22-08-1930", '\
	#	+ '"telephones": [{"id": 0, "telephone_number": "5512546702", "description": "Casa"}], '\
	#	+ '"addresses": [{"id": 0, "street": "New York", "floor": "303A", "city": "Ciudad de México", '\
	#	+ '"zip_code": "08900"}]}}')
	#json_request = json.loads('{"command": "3", "parameters": {"name":"", "telephone":"5512546702"}}')
	#json_request = json.loads('{"command": "3", "parameters": {"name":"Dorotea", "telephone":""}}')
	#result = create_contact(json_request['contact'])
	result = find_contact(json_request['parameters'])
	#result = delete_contact(json_request['parameters'])
	print(f'Result = {result}')


if __name__ == '__main__':
	main()