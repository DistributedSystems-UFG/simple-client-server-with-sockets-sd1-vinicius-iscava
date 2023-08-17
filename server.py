from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 

# Serviço para calculadora simples
conn.send(str.encode(bytes.decode(data)+"*")) # return sent data plus an "*"

opcao = Null
# Loop para interação entre client e server. Servidor irá parar apenas se o client enviar a mensagem "exit".
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if data == "exit": break       # stop if client stopped
  else:
    match data:
    case "multiplicar":
        return "ok"
    case "dividir":
        return "Ok"
    case "Adicionar":
        return "Ok"
    case "Subtrair":
        return "Ok"
    case _:
        return "Something's wrong with the internet"
    print(bytes.decode(data))
    conn.send(str.encode(bytes.decode(data)+"*")) # return sent data plus an "*"
conn.close()               # close the connection
