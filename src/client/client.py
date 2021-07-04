from address import Address
from telephone import Telephone
from contact import Contact

import utils.attributes_values as utilsattr
import constants
import view
import json
import socket


def show_contact(message, socket_client):
	"""Show the view to retrieve a contact list.
	
	Args:
		message (str) - Request.
		socket_client (socket) - Client connection.
	"""
	view.show_find_menu()
	end_find = False
	while not end_find:
		parameters = {'name':None, 'telephone':None}
		option_find = view.get_option('Option: ')
		if option_find == constants.FIND_BY_NAME:
			parameters['name'] = input('Find by name: ')
			end_find = True
		elif option_find == constants.FIND_BY_TELEPHONE:
			parameters['telephone'] = input('Find by telephone: ')
			end_find = True
		elif option_find == constants.BACK:
			end_find = True
	if option_find != constants.BACK:
		message['parameters'] = parameters
		find_contacts(message, socket_client)


def find_contacts(message, socket_client):
	"""Show the contacts list that meet the search parameters.
	
	Args:
		message (str) - Request.
		socket_client (socket) - Client connection.
	"""
	try:
		request = json.dumps(message, ensure_ascii=False)
		socket_client.send(str.encode(request))
		response = socket_client.recv(4096)
		response = response.decode('utf-8')
		response = json.loads(response)
		view.show_contacts(response['contacts'])
	except Exception as e:
		print('ERROR: Couldn\'t find contacts!')


def insert_contact(message, socket_client):
	"""Show the view to insert a new data contact.
	
	Args:
		message (str) - Request.
		socket_client (socket) - Client connection.
	"""
	try:
		message['contact'] = view.create_contact()
		request = json.dumps(message, ensure_ascii=False)
		socket_client.send(str.encode(request))
		response = socket_client.recv(4096)
		response = response.decode('utf-8')
		response = json.loads(response)
		if response['code'] == '1':
			print('Client inserted')
		elif response['code'] == '0':
			print('ERROR: Couldn\'t insert contact!')
	except Exception as e:
		print('ERROR: Couldn\'t create a new contact!')


def drop_contacts(message, socket_client):
	"""Delete a data contact.
	
	Args:
		message (str) - Request.
		socket_client (socket) - Client connection.
	"""
	try:
		request = json.dumps(message, ensure_ascii=False)
		socket_client.send(str.encode(request))
		response = socket_client.recv(4096)
		response = response.decode('utf-8')
		response = json.loads(response)
		if response['code'] == '1':
			print('Client deleted')
		elif response['code'] == '0':
			print('ERROR: Couldn\'t delete the contact!')
	except:
		print('ERROR: Couldn\'t drop the contact!')


def delete_contact(message, socket_client):
	"""Show the view to delete a data contact.
	
	Args:
		message (str) - Request.
		socket_client (socket) - Client connection.
	"""
	view.show_delete_menu()
	end_find = False
	while not end_find:
		parameters = {'name':None, 'telephone':None}
		option_find = view.get_option('Option: ')
		if option_find == constants.DELETE_BY_NAME:
			parameters['name'] = input('Find by name: ')
			end_find = True
		elif option_find == constants.DELETE_BY_TELEPHONE:
			parameters['telephone'] = input('Find by telephone: ')
			end_find = True
		elif option_find == constants.BACK:
			end_find = True
	if option_find != constants.BACK:
		message['parameters'] = parameters
		drop_contacts(message, socket_client)
	request = json.dumps(message, ensure_ascii=False)


def main():
	socket_client = socket.socket()
	host = '127.0.1'
	port = 30_000
	socket_client.connect((host, port))
	print('Connected to server!')
	while True:
		view.show_menu()
		message = {'command':''}
		message['command'] = view.get_option('Option: ')
		if message['command'] == constants.SHOW_CONTACT:
			show_contact(message, socket_client)
		elif message['command'] == constants.NEW_CONTACT:
			insert_contact(message, socket_client)
		elif message['command'] == constants.DELETE_CONTACT:
			delete_contact(message, socket_client)
		elif message['command'] == constants.SHOW_ALL_CONTACTS:
			find_contacts(message, socket_client)
		elif message['command'] == constants.EXIT:
			request = json.dumps(message, ensure_ascii=False)
			socket_client.send(str.encode(request))
			print('Clossing client...')
			break


if __name__ == '__main__':
	main()