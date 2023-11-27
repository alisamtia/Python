import socket

ob=socket.socket()
ob.bind(("localhost",2301))
ob.listen(4)
clientobject,add=ob.accept()
print("Server is Ready to Connect")
print("Conected with this adress",add)

# to recievice data from the clients

conn=True
while conn:
    gotmessage=clientobject.recv(1024)
    gotmessage.decode("utf-8")
    print(gotmessage)

ob.close()
