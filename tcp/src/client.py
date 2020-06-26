#!/usr/bin/python
#coding=UTF-8

"""
"""
import rospy
import socket
import threading
import struct
import serial
def handle_client(client_socket):
        while (True):
		print("running")
		request = client_socket.recv(1024)
		print "[*] Received: %s" % request
		x,y,z=struct.unpack("<fff",request)
		print("x,y,z is : ",x,y,z)
		if not request:
			client.close()
			server_handler.kill()  



if __name__ == '__main__':
	rospy.init_node("client")
	target_host = socket.gethostname()
	target_port = 9999

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	client.connect((target_host, target_port))

	server_handler = threading.Thread(target=handle_client,args=(client,))
	print(1)
	server_handler.start()


	msg = raw_input("input : ")

	while not(msg=="exit"):
		client.send(msg)
		msg = raw_input("input : ")
	client.close()
	server_handler.kill()
