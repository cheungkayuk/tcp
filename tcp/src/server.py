#!/usr/bin/python
#coding=UTF-8

from geometry_msgs.msg import Twist
import rospy
import socket
import string
import threading
import serial
import struct

bind_ip = socket.gethostname()
bind_port = 9999
def handle_client(client_socket):
	while (True):
		print("run1")
		request = client_socket.recv(1024)
		print "[*] Received: %s" % request  
		#client_socket.send("ACK!")
		print("run2")

def callback(data):
	msg=struct.pack("<fff",data.linear.x,data.linear.y,data.linear.z)
	print("i sended", msg)
	client.send(msg)


if __name__ == '__main__':
	rospy.init_node("server")
	sub = rospy.Subscriber("/turtle1/cmd_vel",Twist,callback)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server.bind((bind_ip, bind_port))
				
	server.listen(1)

	print "[*] Listening on %s:%d" % (bind_ip, bind_port)
	client, addr = server.accept()
	#sub = rospy.Subscriber("/turtle1/cmd_vel",Twist,callback)
	
	print "[*] Acepted connection from: %s:%d" % (addr[0],addr[1])
	
	client_handler = threading.Thread(target=handle_client,args=(client,))
	
	client_handler.start()
	sub = rospy.Subscriber("turtle/cmd_vel", Twist,callback)
	msg=raw_input("Type exit")
	while not(msg=="exit"):
		msg=raw_input("")
	server.close()
		
