from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

while True:
  operacao = input("\n\nDigite a operação: ")
  s.send(str.encode(operacao))  # send some data
  data = s.recv(1024)     # receive the response
  if data=="exit":
    print ("Encerrando...")
    break
  else:
    print (bytes.decode(data))            # print the result
s.close()               # close the connection
