#Page 304
from socket import *
import sys


def GetSocket():
	global SOCK
	"""get socket that is connected to server"""
	server = raw_input("Server name (Ex. gmail-smtp-in.l.google.com): ")
	SOCK = socket(AF_INET, SOCK_STREAM)
	# port 25 is smtp port
	SOCK.connect((server, 25))
	if "220" != SOCK.recv(1000)[:3]:
		sys.exit("Invalid response from server")

def CloseConnection():
	"""close connection to smtp server"""
	global SOCK
	SOCK.shutdown(SHUT_RDWR)
	SOCK.close()

def GetSenderAndTarget():
	"""Get user pc name to say HELO"""
	global SOCK
	SenderMail = raw_input("FROM: ")
	SOCK.sendall("MAIL FROM: <" + SenderMail + "> \n")
	if "250" != SOCK.recv(1000)[:3]:
		sys.exit("Sender mail is not valid!")

	TargetMail = raw_input("To: ")
	SOCK.sendall("RCPT TO: <" + TargetMail + "> \n")
	if "250" != SOCK.recv(1000)[:3]:
		sys.exit("Target mail is not valid!")

	return SenderMail, TargetMail

def SendPcName():
	"""Get user pc name to say HELO"""
	global SOCK
	PcName = raw_input("Host name (Ex. www.hotmail.com):")
	SOCK.sendall("HELO " + PcName + "\n")
	if "250" != SOCK.recv(1000)[:3]:
		sys.exit("Error Mail server refused access")

def SendMessage(SenderMail,TargetMail):
	"""send message"""
	global SOCK
	SOCK.sendall("DATA\n")
	if "354" != SOCK.recv(1000)[:3]:
		sys.exit("Mail host not allowing to send data")
	Subject = raw_input("Subject: ")
	SOCK.sendall("From: " + SenderMail + "\n" + \
				"To: " + TargetMail + "\n" + \
		     	"Subject: " + Subject + "\n\n")
	print "Type message body, end message with \".\" on a line by itself"
	line = raw_input("")
	while line != ".":
		SOCK.sendall(line + "\n")
		line = raw_input("")
	SOCK.sendall("\r\n.\r\n")
	Resp = SOCK.recv(1000)
	if "250" != Resp[:3]:
		print Resp
		sys.exit("Error, mail server didn't send message")
	SOCK.sendall("QUIT \n")
	print "message sent"

SOCK = None
GetSocket()
SendPcName()
SenderMail, TargetMail = GetSenderAndTarget()
SendMessage(SenderMail, TargetMail)
CloseConnection()
