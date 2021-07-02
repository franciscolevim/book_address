from contact import Contact
from address import Address
from telephone import Telephone
import sqlite3


class DataBase:


	__PATH = '../db/BookAddress.db'


	def __init__(self):
		pass


	def read_contacts(self):
		"""Retrieve all contacts of the database.

		Returns: 
			list - A list with all contacts, or an empty list if the data could not be obtained.
		"""
		try:
			database = sqlite3.connect(self.__PATH)
			cursor = database.cursor()
			cursor.execute('SELECT * FROM contact')
			contacts = []
			for record in cursor:
				contact = Contact(id=record[0], name=record[1], last_name=record[2], birth_date=record[3])
				contact.telephones = self.__read_telephones(database, contact.id)
				contact.addresses = self.__read_addresses(database, contact.id)
				contacts.append(contact)
			database.close()
			return contacts
		except Exception as e:
			print('Error: Couldn\'t read the contacts.')
			return []


	def __read_telephones(self, database, contact_id):
		"""Retrieve all telphones of a contact.

		Args:
			contact_id.

		Returns: 
			list - A list with all telephones, or an empty list if the data could not be obtained.
		"""
		try:
			cursor_phone = database.cursor()
			cursor_phone.execute(f'SELECT id, number, description FROM telephone WHERE contact_id = {contact_id}')
			telephones = []
			for record in cursor_phone:
				telephones.append(Telephone(id=record[0], telephone_number=record[1], description=record[2]))
			return telephones
		except:
			print('Error: Couldn\'t read the telephones.')
			return []


	def __read_addresses(self, database, contact_id):
		"""Retrieve all addresses of a contact.

		Args:
			contact_id.

		Returns: 
			list - A list with all addresses, or an empty list if the data could not be obtained.
		"""
		try:
			cursor_address = database.cursor()
			cursor_address.execute(f'SELECT id, street, floor, city, zip_code FROM address WHERE contact_id = {contact_id}')
			addresses = []
			for record in cursor_address:
				addresses.append(Address(id=record[0], street=record[1], floor=record[2], city=record[3], zip_code=record[4]))
			return addresses
		except:
			print('Error: Couldn\'t read the addresses.')
			return []


	def read_contacts_with_name(self, name):
		"""Retrieve all contacts with the name value.

		Args:
			name - name of the contact.

		Returns: 
			list - Contact list, or an empty list if the data could not be obtained.
		"""
		try:
			database = sqlite3.connect(self.__PATH)
			cursor = database.cursor()
			cursor.execute(f'SELECT * FROM contact WHERE name = \'{name}\'')
			contacts = []
			for record in cursor:
				contact = Contact(id=record[0], name=record[1], last_name=record[2], birth_date=record[3])
				contact.telephones = self.__read_telephones(database, contact.id)
				contact.addresses = self.__read_addresses(database, contact.id)
				contacts.append(contact)
			database.close()
			return contacts
		except Exception as e:
			print('Error: Couldn\'t read the contacts with name.')
			return []


	def read_contacts_by_telephone_number(self, telephone_number):
		"""Retrieve all contacts with the telephone number value.

		Args:
			telephone_number - A telphone number of the contact.

		Returns: 
			list - Contact list, or an empty list if the data could not be obtained.
		"""
		try:
			database = sqlite3.connect(self.__PATH)
			cursor = database.cursor()
			cursor.execute(f'SELECT DISTINCT * FROM telephone WHERE number = \'{telephone_number}\'')
			contacts = []
			for record in cursor:
				cursor_contact = database.cursor()
				cursor_contact.execute(f'SELECT * FROM contact WHERE id = {record[1]}')
				for contact_record in cursor_contact:
					contact = Contact(
						id=contact_record[0]
						, name=contact_record[1]
						, last_name=contact_record[2]
						, birth_date=contact_record[3])
					contact.telephones = self.__read_telephones(database, contact.id)
					contact.addresses = self.__read_addresses(database, contact.id)
					contacts.append(contact)
			database.close()
			return contacts
		except Exception as e:
			print(f'Error: Couldn\'t read the contacts by telephone number.')
			return []


	def save_contact(self, contact):
		"""Insert a contact on the database.

		Args:
			contact - Contacta data.

		Returns: 
			bool - True if the contact was saved successfully, else False.
		"""
		try:
			database = sqlite3.connect(self.__PATH)
			cursor = database.cursor()
			data_contact = (contact.name, contact.last_name, contact.birth_date)
			cursor.execute('INSERT INTO contact (name, last_name, birth_date) values (?, ?, ?)', data_contact)
			contact_id = cursor.lastrowid
			for telephone in contact.telephones:
				data_telephone = (contact_id, telephone.telephone_number, telephone.description)
				cursor.execute('INSERT INTO telephone (contact_id, number, description) values (?, ?, ?)', data_telephone)
			for address in contact.addresses:
				data_address = (contact_id, address.street, address.floor, address.city, address.zip_code)
				cursor.execute('INSERT INTO address (contact_id, street, floor, city, zip_code) values (?, ?, ?, ?, ?)', data_address)
			database.commit()
			return True
		except Exception as e:
			print(f'Error: Couldn\'t insert the contact.')
			False


	def delete_contact(self, contact_id):
		"""Delete a contact of the database.

		Args:
			contact_id

		Returns: 
			bool - True if the contact was deleted successfully, else False.
		"""
		try:
			database = sqlite3.connect(self.__PATH)
			cursor = database.cursor()
			cursor.execute(f'DELETE FROM telephone WHERE contact_id = {contact_id}')
			cursor.execute(f'DELETE FROM address WHERE contact_id = {contact_id}')
			cursor.execute(f'DELETE FROM contact WHERE id = {contact_id}')
			database.commit()
			return True
		except:
			print(f'Error: Couldn\'t delete the contact.')
			False	
