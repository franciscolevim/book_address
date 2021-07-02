import server
import socket
import threading


def main():
	server_socket = socket.socket()
	host = '127.0.0.1'
	port = 30_000
	server_socket.bind((host, port))
	server_socket.listen()
	print('The server is ready')
	while True:
		client, address = server_socket.accept()
		print(f'New client connected: {address[0]}:{address[1]}')
		thread = threading.Thread(target=server.thread_client, args=(client, f'{address[0]}:{address[1]}'))
		thread.start()
	server_socket.close()


if __name__ == '__main__':
	main()