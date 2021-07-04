from address import Address
from telephone import Telephone
from contact import Contact

import json
import utils.attributes_values as utilsattr


def show_menu():
	print('''Menu
		1) Show contact
		2) New contact
		3) Delete contact
		4) Show all contacts
		5) Exit''')


def show_find_menu():
	print('''Find contacts
		1) Name
		2) Telephone
		3) Back''')


def show_delete_menu():
	print('''Delete contacts by
		1) Name
		2) Telephone
		3) Back''')


def get_option(text):
	"""Retrieves a selected option.

	Returns: 
		 (int) - The option selected.
	"""	
	readed = False
	while not readed:
		try:
			number = int(input(text))
		except ValueError:
			print('Error: Should input a number.')
		else:
			readed = True
	return number


def show_contacts(contacts_map):
	"""Show the a contacts list data."""	
	try:
		print('###### CONTACTS ######')
		for contact_map in contacts_map:
			contact = Contact.load_from_map(contact_map)
			print(f'Name: {contact.name}')
			print(f'Last name: {contact.last_name}')
			print(f'Birth date: {contact.birth_date}')
			for telephone in contact.telephones:
				print(f'Telephone {telephone.description}: {telephone.telephone_number}')
			for address in contact.addresses:
				print(f'Address: {address.street} {address.floor}, {address.city}, {address.zip_code}')
			print('')
		print('#' * 100)
	except Exception as e:
		print('Error: Couldn\'t print the contacts.')


def create_contact():
	"""Create new contact view.

	Returns: 
		 (dict) - New contact data.
	"""	
	try:
		print('###### NEW CONTACT ######')
		new_contact = Contact()
		new_contact.name = input('Name: ')
		new_contact.last_name = input('Last name: ')
		new_contact.birth_date = input('Birth date: ')
		telephones = []
		end = ''
		while end.lower() != 'no':
			end = input('Do you want add a telephone? Yes/No: ')
			if end.lower() == 'yes':
				new_telephone = Telephone()
				new_telephone.telephone_number = input('Number: ')
				new_telephone.description = input('Description: ')
				telephones.append(new_telephone)
		new_contact.telephones = telephones
		addresses = []
		end = ''
		while end.lower() != 'no':
			end = input('Do you want add an address? Yes/No: ')
			if end.lower() == 'yes':
				new_address = Address()
				new_address.street = input('Street: ')
				new_address.floor = input('Floor: ')
				new_address.city = input('City: ')
				new_address.zip_code = input('Zip Code: ')
				addresses.append(new_address)
		new_contact.addresses = addresses
		return new_contact.to_map()
	except:
		print('Error: Couldn\'t create the contact.')
		return None
