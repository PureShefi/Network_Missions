#Page 307
from socket import *
import thread
import datetime

def NewClient(Client_s, Client_addr):
	"""Handle new client connection"""
	#Add shutdown in finally
	Request = Client_s.recv(10000)
	CleanReq = Request.split(" ")
	if len(CleanReq) < 2:
		Client_s.sendall("Error, Not enough parameters")
		Client_s.shutdown(SHUT_RDWR)
		Client_s.close()
		return
	if CleanReq[0].upper() != "GET":
		Client_s.sendall("Error, Not GET request")
		Client_s.shutdown(SHUT_RDWR)
		Client_s.close()
		return

	#everything is ok, Get file
	LogData(Client_addr, CleanReq[1])
	Data = ParseFileRequest(CleanReq[1])
	Client_s.sendall(Data)

def ParseFileRequest(FileName):
	"""Parse requested file"""
	global BaseDir
	if FileName == "/":
		FileName = "/index.html"
	elif "." not in FileName:
		FileName += ".html"
	try:
		File = open(BaseDir + FileName).read()
		HttpData = "HTTP/1.0 200 Document Follows\n" + \
				"Content-Length:" + str(len(File)) + \
				"\n\n" + File
	except:
		HttpData = 'HTTP/1.0 404 Not Found\n\n'
	return HttpData

def StartServer():
	"""call function to start the HTTP server"""
	global BaseDir
	#get base directory containing files 
	BaseDir = raw_input("Base Directory: ")

	#start server listening on port 80 waiting for requests
	Server_s = socket(AF_INET, SOCK_STREAM)
	Server_s.bind(("0.0.0.0",80)) #80 default HTTP port
	Server_s.listen(5)
	print "listening on port 80"
	while 1:
		thread.start_new_thread(NewClient, (Server_s.accept()))

#Log incoming request in order to sell data to GOOGLE for money
def LogData(Client_addr, File):
	"""Log Data to file"""
	LogFile = open("Log.txt", "a")
	if ".js" not in File and ".css" not in File:
		LogFile.write(str(datetime.datetime.now()) + " " + str(Client_addr) + " requested " + File + "\n")
	LogFile.close()
	

BaseDir = ""
StartServer()
