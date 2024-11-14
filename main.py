nome = input("Digite o seu nome;")

 #aqui o sistema pede o usuário            
idade = 15 

#aqui o sistema pedeno nome do usuário
def menu
print(f"Bem vindo {nome}, você tem {idade} anos.")
print("Como posso te ajudar hoje?")
print("1 - Bebidas")
print("2 - Salgados")
print("3 - Doces")
#aqui grava a opção que o usuário decidiu
opc_user = int(input("Digite o número da opção desejada:") 

if opc_user == 1:
      print("Temos coca, guaraná")
elif opc_user == 2:
      print("temos coxinha")
elif  opc_user == 3:
      print("Temos bala")
else:
      print("Escolha um número de 1 a 3")
menu()