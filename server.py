from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 

# Serviço para calculadora simples
conn.send(str.encode("Calculadora basica\n\nUtilize os operadores \"+\", \"-\", \"*\", \"/\" para adicionar, subtrair, multiplicar e dividir respectivamente.\n\nDigite \"exit\" para encerrar."))

# Loop para interação entre client e server. Servidor irá parar apenas se o client enviar a mensagem "exit".
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if data == "exit": break       # stop if client stopped
  else:
    if data.find("+">=0):
      numeros = data.split('+')
    elif data.find("-">=0):
      numeros = data.split('-')
    elif data.find("*">=0):
      numeros = data.split('*')
    elif data.find("/">=0):
      numeros = data.split('/')
    else:
      print("\nEntrada invalida.")
      conn.send(str.encode("\nEntrada inválida. Tente novamente!"))
      continue
    
    primeiro_numero = numeros[0].strip()
    segundo_numero = numeros[1].strip()
    try:
        primeiro_numero = int(primeiro_numero)
    except ValueError:
        try:
            primeiro_numero = float(primeiro_numero)
        except ValueError:
            try:
                primeiro_numero = float(primeiro_numero.replace(",", "."))
            except ValueError:
                print("\nEntrada invalida.")
                conn.send(str.encode("\nEntrada inválida. Tenten novamente!"))
                continue
      
    try:
        segundo_numero = int(segundo_numero)
    except ValueError:
        try:
            segundo_numero = float(segundo_numero)
        except ValueError:
            try:
                segundo_numero = float(segundo_numero.replace(",", "."))
            except ValueError:
                print("\nEntrada invalida.")
                conn.send(str.encode("\nEntrada invalida. Tente novamente!"))
                continue
              
    print("Entrada valida. Processando...")
    if data.find("+">=0):
      print("\n" + primeiro_numero + " + " + segundo_numero + " = " + (primeiro_numero+segundo_numero))
      conn.send(str.encode("\n" + primeiro_numero + " + " + segundo_numero + " = " + (primeiro_numero+segundo_numero)))
    elif data.find("-">=0):
      print("\n" + primeiro_numero + " - " + segundo_numero + " = " + (primeiro_numero-segundo_numero))
      conn.send(str.encode("\n" + primeiro_numero + " - " + segundo_numero + " = " + (primeiro_numero-segundo_numero)))
    elif data.find("*">=0):
      print("\n" + primeiro_numero + " * " + segundo_numero + " = " + (primeiro_numero*segundo_numero))
      conn.send(str.encode("\n" + primeiro_numero + " * " + segundo_numero + " = " + (primeiro_numero*segundo_numero)))
    elif data.find("/">=0):
      print("\n" + primeiro_numero + " / " + segundo_numero + " = " + (primeiro_numero/segundo_numero))
      conn.send(str.encode("\n" + primeiro_numero + " / " + segundo_numero + " = " + (primeiro_numero/segundo_numero)))

conn.close()               # close the connection
