import random
from time import sleep 
from os import system, name 

# definicao da funcao clear para limpar a consola
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  

numjogos=1
vitorias_utilizador=0
vitorias_pc=0
empates=0
i=1
#ficheiro para guardar resultados
f = open("data.txt", "w")
f.close()

while i==1:
    #menu
    print("---------------------------------------------------------------------------")
    print("Jogo do Pedra , Papel , Tesoura!")
    print("---------------------------------------------------------------------------")
    print("Jogo número: %s , Vitorias do utilizador: %s , Vitorias PC: %s , Empates: %s" %(numjogos,vitorias_utilizador,vitorias_pc,empates))
    print("---------------------------------------------------------------------------")
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("---------------------------------------------------------------------------")
    # input do utlizador
    opcao = int(input())
    if opcao==1:
        print("Voce escolheu Pedra!")  
    if opcao==2:
        print("Voce escolheu Papel!")
    if opcao==3:    
        print("Voce escolheu Tesoura!")
    # criar a opção do computador
    numerorandom=random.randint(0, 12)
    print(" ")
    if numerorandom <= 4:
        opcaopc=1
        print("O adversário escolheu Pedra!")
    elif numerorandom > 4 and numerorandom <= 8:
        opcaopc=2
        print("O adversário escolheu Papel!")
    elif numerorandom > 8 and numerorandom <= 12:
        opcaopc=3
        print("O adversário escolheu Tesoura!")

    # escolher qual dos dois ganhou ou perdeu
    print(" ")
    if opcao==opcaopc:
        print("Ambos escolheram a mesma opção o resultado foi empate!")
        empates=empates+1
    elif opcao == 1 and opcaopc == 2:
        print("O adversário ganhou!")
        vitorias_pc=vitorias_pc+1
    elif opcao == 1 and opcaopc == 3:
        print("O utilizador ganhou!")
        vitorias_utilizador=vitorias_utilizador+1
    elif opcao == 2 and opcaopc == 1:
        print("O utilizador ganhou!")
        vitorias_utilizador=vitorias_utilizador+1
    elif opcao == 2 and opcaopc == 3:
        print("O adversário ganhou!")
        vitorias_pc=vitorias_pc+1
    elif opcao == 3 and opcaopc == 1:
        print("O adversário ganhou!")
        vitorias_pc=vitorias_pc+1
    elif opcao == 3 and opcaopc == 2:
        print("O utilizador ganhou!")
        vitorias_utilizador=vitorias_utilizador+1
    f = open("data.txt", "a")
    f.write("%s %s %s %s %s %s \n" %(numjogos,vitorias_utilizador,vitorias_pc,empates,opcao,opcaopc))
    f.close()
    numjogos=numjogos+1
    # pausa no programa 5 segundos
    print("------------------------------------------------------------------")
    sleep(2)
    print("Por favor aguarde 5 segundos")
    sleep(1)
    print("Por favor aguarde 4 segundos")
    sleep(1)
    print("Por favor aguarde 3 segundos")
    sleep(1)
    print("Por favor aguarde 2 segundos")
    sleep(1)
    print("Por favor aguarde 1 segundos")
    sleep(1)
    #apagar a consola 
    clear() 