#CALCULADOR DE CHURRASCO
import os                   #Importar OS
import pandas as pd         #Importar Pandas
import numpy as np          #Importar Numpy

#Variáveis
escolha = ""
total = 0
continuar = ""
despesas = 0

nomesingredientes = []          #Vetor Para os nomes
tiposingredientes = []          #Vetor para os tipos
qgingredientes = []             #Vetor para o formato de quantidades
quantidadeppessoa = []          #Vetor para a quantidade por pessoa
precoingredientes =[]           #Vetor para os preços

precomostrar = []               #Vetor para os preços na tabela final

#Carregar os arquivos .txt
arquivo = open("ingredientes.txt", "r", encoding="utf-8")       #Carregar o nome dos ingredientes
linhas = arquivo.readlines()            #Ler as linhas
for i in linhas:
    nomesingredientes.append(i)             #Adicionar o nome
    total += 1      #Adicionar 1 ao total
arquivo.close()

arquivo = open("tipos.txt", "r", encoding="utf-8")               #Carregar o tipo dos ingredientes
linhas = arquivo.readlines()            #Ler as linhas
for i in linhas:
    tiposingredientes.append(i)             #Adicionar o tipo
arquivo.close()

arquivo = open("qg.txt", "r", encoding="utf-8")                  #Carregar o formato de quantidade dos ingredientes
linhas = arquivo.readlines()            #Ler as linhas
for i in linhas:
    qgingredientes.append(i)             #Adicionar o formato de quantidade
arquivo.close()

arquivo = open("preços.txt", "r", encoding="utf-8")              #Carregar o preço dos ingredientes
linhas = arquivo.readlines()            #Ler as linhas
for i in linhas:
    precoingredientes.append(i)             #Adicionar o valor da quantidade por pessoa
arquivo.close()

arquivo = open("quantidades.txt", "r", encoding="utf-8")        #Carregar a quantidade dos ingredientes por pessoa
linhas = arquivo.readlines()            #Ler as linhas
for i in linhas:
    quantidadeppessoa.append(i)             #Adicionar o preço
arquivo.close()

while True:
    os.system("cls")        #Limpar a tela

    #Mostrar as escolhas
    print("Escolha uma das opções abaixo:\n(1) = Alterar Ingredientes;\n(2) = Alterar Quantidade por Pessoa / Preço;\n(3) = Fazer um Churrasco;\n(4) = Finalizar Programa;")
    escolha = input(" :: ")

    while escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":      #Caso o valor digitado não seja válido
        os.system("cls")
        print("O valor digitado não é válido!\n")
        print("Escolha uma das opções abaixo:\n(1) = Alterar Ingredientes;\n(2) = Alterar Quantidade por Pessoa / Preço;\n(3) = Fazer um Churrasco;\n(4) = Finalizar Programa;")
        escolha = input(" :: ")
    os.system("cls")

    match escolha:
        case "1":       #Caso tenha escolhido "(1) = Alterar Ingredientes"
            while True:
                os.system("cls")
                print("Escolha uma das opções abaixo:\n(1) = Adicionar novo Ingrediente;\n(2) = Apagar Ingrediente;\n(3) = Mostrar Lista;\n(4) = Voltar;")
                escolha2 = input(" :: ")
                while escolha2 != "1" and escolha2 != "2" and escolha2 != "3" and escolha2 != "4":      #Caso o valor digitado não seja válido
                    os.system("cls")
                    print("O valor digitado não é válido!\n")
                    print("Escolha uma das opções abaixo:\n(1) = Adicionar novo Ingrediente;\n(2) = Apagar Ingrediente;\n(3) = Mostrar Lista;\n(4) = Voltar;")
                    escolha2 = input(" :: ")
                os.system("cls")
                
                match escolha2:
                    case "1":       #Caso tenha escolhido "(1) = Adicionar novo ingrediente"
                        #Variáveis placeholder
                        ingredientedig = ""
                        tiposelec = 0
                        qgselec = 0
                        quantidadedig = 0
                        precodig = 00.00
                        sle = ""

                        #Digitar o nome do ingrediente
                        ingredientedig = input("Digite o nome do ingrediente: ")
                        os.system("cls")

                        #Digitar o tipo do ingrediente
                        print("Digite o tipo do ingrediente digitado:\n(1) = Comida;\n(2) = Bebida;\n(3) = Outros;\n")
                        tiposelec = int(input(" :: "))
                        while tiposelec < 1 or tiposelec > 3:       #Caso o valor digitado não seja válido
                            os.system("cls")
                            print("O valor digitado não é válido!\n")
                            print("Digite o tipo do ingrediente digitado:\n(1) = Comida;\n(2) = Bebida;\n(3) = Outros;\n")
                            tiposelec = int(input(" :: "))
                        os.system("cls")

                        if tiposelec==1:        #Caso tenha selecionado "Comida"
                            sle="gramas"            #Mudar o formato de quantidade
                            tiposelec = "Comida"
                        if tiposelec==2:        #Caso tenha selecionado "Bebida"
                            sle="ml"            #Mudar o formato de quantidade
                            tiposelec = "Bebida"
                        if tiposelec==3:        #Caso tenha selecionado "Outros"
                            sle="gramas"            #Mudar o formato de quantidade
                            tiposelec = "Outro"

                        #Digitar o formato de quantidade do ingrediente
                        print("Digite o formato de quantidade do ingrediente digitado:\n(1) = Por Unidade;\n(2) = Por Gramas/ml;\n")
                        qgselec = int(input(" :: "))
                        while qgselec < 1 or qgselec > 2:       #Caso o valor digitado não seja válido
                            os.system("cls")
                            print("O valor digitado não é válido!\n")
                            print("Digite o formato de quantidade do ingrediente digitado:\n(1) = Por Unidade;\n(2) = Por Gramas/ml;\n")
                            qgselec = int(input(" :: "))
                        os.system("cls")
                            
                        if qgselec==1:      #Caso tenha selecionado "Unidade"
                            qgselec = "Unidades"
                        if qgselec==2:      #Caso tenha selecionado "Gramas/ml"
                            if sle=="gramas":               #Caso seja uma comida
                                qgselec = "Gramas"
                            elif sle=="ml":                 #Caso seja uma bebida
                                qgselec = "Mililitros"
                        
                        #Digitar a quantidade que cada pessoa receberá
                        print("Digite a quantidade de", qgselec, "de", ingredientedig, "que cada pessoa receberá:")
                        quantidadedig = int(input(" :: "))
                        while quantidadedig <= 0:       #Caso o valor digitado não seja válido
                            os.system("cls")
                            print("O valor digitado não é válido!\n")
                            print("Digite a quantidade de", qgselec, "de", ingredientedig, "que cada pessoa receberá:")
                            quantidadedig = int(input(" :: "))
                        os.system("cls")

                        #Digitar o preço do ingrediente
                        print("Digite o preço de", quantidadedig, qgselec, "de", ingredientedig, ":")
                        precodig = float(input(" :: "))
                        while precodig <= 0:       #Caso o valor digitado não seja válido
                            os.system("cls")
                            print("O valor digitado não é válido!\n")
                            print("Digite o preço de", quantidadedig, qgselec, "de", ingredientedig, ":")
                            precodig = float(input(" :: "))
                        os.system("cls")

                        #Mostrar as informações digitadas sobre o ingrediente
                        print("<>Ingrediente: ", ingredientedig, ";\n<>Tipo: ", tiposelec, ";\n<>Fromato de Quantidade: ", qgselec, ";\n<>Quantidade Por Pessoa: ", quantidadedig, ";\n<>Preço: R$%.2f" % precodig, ";\n\n")

                        #Perguntar se deseha ou não adicionar o ingrediente digitado
                        print("Gostaria de adicionar o ingrediente digitado?\n(S) = Sim;\n(N) = Não;")
                        fim = input(" :: ")
                        fim = fim.capitalize()              #Transformar o valor digitado em caixa alta
                        while fim != "S" and fim != "N":       #Caso o valor digitado não seja válido
                            os.system("cls")
                            print("O valor digitado não é válido!\n")
                            #Mostrar as informações digitadas sobre o ingrediente
                            print("<>Ingrediente: ", ingredientedig, ";\n<>Tipo: ", tiposelec, ";\n<>Fromato de Quantidade: ", qgselec, ";\n<>Quantidade Por Pessoa: ", quantidadedig, ";\n<>Preço: R$%.2f" % precodig, ";\n\n")

                            print("Gostaria de adicionar o ingrediente digitado?\n(S) = Sim;\n(N) = Não;")
                            fim = input(" :: ")
                            fim = fim.capitalize()              #Transformar o valor digitado em caixa alta
                        os.system("cls")

                        if fim=="S":        #Caso tenha escolhido SIM
                            nomesingredientes.append(ingredientedig+"\n")                   #Adicionar o nome do ingrediente digitado
                            arquivo = open("ingredientes.txt", "a", encoding="utf-8")       #Abrir o arquivo ingredientes.txt
                            arquivo.write(ingredientedig+"\n")                              #Salvar o nome do ingrediente digitado
                            arquivo.close()                                                 #Fechar o arquivo

                            tiposingredientes.append(tiposelec+"\n")                        #Adicionar o tipo do ingrediente digitado
                            arquivo = open("tipos.txt", "a", encoding="utf-8")              #Abrir o arquivo tipos.txt
                            arquivo.write(tiposelec+"\n")                                   #Salvar o tipo do ingrediente digitado
                            arquivo.close()                                                 #Fechar o arquivo

                            qgingredientes.append(qgselec+"\n")                             #Adicionar o formato de quantidade do ingrediente digitado
                            arquivo = open("qg.txt", "a", encoding="utf-8")                 #Abrir o arquivo qg.txt
                            arquivo.write(qgselec+"\n")                                     #Salvar o formato de quantidade do ingrediente digitado
                            arquivo.close()                                                 #Fechar o arquivo

                            quantidadeppessoa.append(str(quantidadedig)+"\n")               #Adicionar o valor da quantidade por pessoa do ingrediente digitado
                            arquivo = open("quantidades.txt", "a", encoding="utf-8")        #Abrir o arquivo quantidades.txt
                            arquivo.write(str(quantidadedig)+"\n")                          #Salvar o valor da quantidade por pessoa do ingrediente digitado
                            arquivo.close()                                                 #Fechar o arquivo

                            precoingredientes.append(str(precodig)+"\n")                    #Adicionar o preço do ingrediente digitado
                            arquivo = open("preços.txt", "a", encoding="utf-8")             #Abrir o arquivo preços.txt
                            arquivo.write(str(precodig)+"\n")                               #Salvar o preço do ingrediente digitado
                            arquivo.close()                                                 #Fechar o arquivo

                            total += 1      #Adicionar um valor ao total

                    case "2":       #Caso tenha escolhido "(2) = Apagar Ingrediente"
                        if total > 0:
                            cont = 0
                            
                            #Mostrar a lista de ingredientes
                            for i in nomesingredientes:

                                print(cont+1, ". Ingrediente: {0}; - Tipo: {1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3}; Preço: R${4};\n".format(nomesingredientes[cont].rstrip(), tiposingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip(), precoingredientes[cont].rstrip()))
                                cont+=1

                            #Mostrar as opções
                            print("Escolha uma das opções abaixo:\n(0) = Cancelar;\n(1) = Apagar um específico;\n(2) = Apagar todos os ingredientes;")
                            escolha3 = input(" :: ")
                            while escolha3 != "1" and escolha3 != "2" and escolha3 != "0":      #Caso o valor digitado não seja válido
                                os.system("cls")
                                print("O valor digitado não é válido!\n")

                                #Mostrar a lista de ingredientes
                                cont = 0
                                for i in nomesingredientes:

                                    print(cont+1, ". Ingrediente: {0}; - Tipo: {1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3}; Preço: R${4};\n".format(nomesingredientes[cont].rstrip(), tiposingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip(), precoingredientes[cont].rstrip()))
                                    cont+=1

                                print("Escolha uma das opções abaixo:\n(0) = Cancelar;\n(1) = Apagar um específico;\n(2) = Apagar todos os ingredientes;")
                                escolha3 = input(" :: ")
                            os.system("cls")

                            match escolha3:
                                case "0":       #Caso tenha escolhido "(0) = Cancelar"
                                    print("Cancelado!\n")

                                case "1":       #Caso tenha escolhido "(1) = Apagar um Específico"
                                    #Mostrar a lista de ingredientes
                                    cont = 0
                                    for i in nomesingredientes:
                                    
                                        print(cont+1, ". Ingrediente: {0}; - Tipo: {1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3}; Preço: R${4};\n".format(nomesingredientes[cont].rstrip(), tiposingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip(), precoingredientes[cont].rstrip()))
                                        cont+=1

                                    deletar = int(input("Digite o número do ingrediente que deseja apagar: "))

                                    while deletar > total or deletar < 1:      #Caso o valor digitado não seja válido
                                        os.system("cls")
                                        print("O valor digitado não é válido!\n")
                                        #Mostrar a lista de ingredientes
                                        cont = 0
                                        for i in nomesingredientes:

                                            print(cont+1, ". Ingrediente: {0}; - Tipo: {1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3}; Preço: R${4};\n".format(nomesingredientes[cont].rstrip(), tiposingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip(), precoingredientes[cont].rstrip()))
                                            cont+=1

                                        deletar = int(input("Digite o número do ingrediente que deseja apagar: "))
                                    os.system("cls")

                                    #Apagar os valores dos vetores
                                    total -= 1                              #Diminuir 1 do total
                                    nomesingredientes.pop(deletar-1)        #Apagar o nome do ingrediente
                                    tiposingredientes.pop(deletar-1)        #Apagar o tipo do ingrediente
                                    qgingredientes.pop(deletar-1)           #Apagar o formato de quantidade do ingrediente
                                    precoingredientes.pop(deletar-1)        #Apagar o preço do ingrediente
                                    quantidadeppessoa.pop(deletar-1)        #Apagar o valor da quantidade por pessoa do ingrediente

                                case "2":       #Caso tenha escolhido "(2) = Apagar todos os ingredientes"
                                    total = 0                       #Zerar o total
                                    nomesingredientes.clear()       #Limpar o vetor dos nomes dos ingredientes
                                    tiposingredientes.clear()       #Limpar o vetor dos tipos dos ingredientes
                                    qgingredientes.clear()          #Limpar o vetor dos formatos de quantidades dos ingredientes
                                    quantidadeppessoa.clear()       #Limpar o vetor dos valores de quantidade por pessoas dos ingredientes
                                    precoingredientes.clear()       #Limpar o vetor dos preços dos ingredientes

                            #Limpar os arquivos .txt
                            if escolha3 != "0":             #Caso a opção escolhida não seja 0
                                arquivo = open("ingredientes.txt", "w", encoding="utf-8")       #Abrir o arquivo ingredientes.txt
                                arquivo.write("")           #Limpar o arquivo
                                arquivo.close()             #Fechar o arquivo
                                arquivo = open("tipos.txt", "w", encoding="utf-8")              #Abrir o arquivo tipos.txt
                                arquivo.write("")           #Limpar o arquivo
                                arquivo.close()             #Fechar o arquivo
                                arquivo = open("qg.txt", "w", encoding="utf-8")                 #Abrir o arquivo qg.txt
                                arquivo.write("")           #Limpar o arquivo
                                arquivo.close()             #Fechar o arquivo
                                arquivo = open("preços.txt", "w", encoding="utf-8")             #Abrir o arquivo preços.txt
                                arquivo.write("")           #Limpar o arquivo
                                arquivo.close()             #Fechar o arquivo
                                arquivo = open("quantidades.txt", "w", encoding="utf-8")        #Abrir o arquivo quantidades.txt
                                arquivo.write("")           #Limpar o arquivo
                                arquivo.close()             #Fechar o arquivo

                            #Reescrever o valor dos arquivos .txt
                            if escolha3 == "1":         #Caso a opção escolhida seja 1
                                arquivo = open("ingredientes.txt", "a", encoding="utf-8")       #Carregar o nome dos ingredientes
                                for i in nomesingredientes:
                                    arquivo.write(i)                                            #Escrever os valores do vetor
                                arquivo.close()                                                 #Fechar o arquivo

                                arquivo = open("tipos.txt", "a", encoding="utf-8")              #Abrir o arquivo tipos.txt
                                for i in tiposingredientes:
                                    arquivo.write(i)                                            #Escrever os valores do vetor
                                arquivo.close()                                                 #Fechar o arquivo

                                arquivo = open("qg.txt", "a", encoding="utf-8")                 #Abrir o arquivo qg.txt
                                for i in qgingredientes:
                                    arquivo.write(i)                                            #Escrever os valores do vetor
                                arquivo.close()                                                 #Fechar o arquivo

                                arquivo = open("preços.txt", "a", encoding="utf-8")             #Abrir o arquivo preços.txt
                                for i in precoingredientes:
                                    arquivo.write(i)                                            #Escrever os valores do vetor
                                arquivo.close()                                                 #Fechar o arquivo

                                arquivo = open("quantidades.txt", "a", encoding="utf-8")        #Abrir o arquivo quantidades.txt
                                for i in quantidadeppessoa:
                                    arquivo.write(i)                                            #Escrever os valores do vetor
                                arquivo.close()                                                 #Fechar o arquivo

                            continuar = input("Pressione Enter para continuar...")              #Pressionar Enter para continuar o programa
                        
                        else:       #Caso não tenha ingredientes cadastrados

                            print("Você não possui nenhum ingrediente cadastrado!\n")
                            continuar = input("Pressione Enter para continuar...")              #Pressionar Enter para continuar o programa

                    case "3":       #Caso tenha escolhido "(3) = Mostrar Lista"
                        #Mostrar a lista de ingredientes
                        cont = 0
                        for i in nomesingredientes:

                            print(cont+1, ". Ingrediente: {0}; - Tipo: {1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3}; Preço: R${4};\n".format(nomesingredientes[cont].rstrip(), tiposingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip(), precoingredientes[cont].rstrip()))
                            cont+=1
                        
                        continuar = input("Pressione Enter para continuar...")              #Pressionar Enter para continuar o programa
                    case "4":       #Caso tenha escolhido "(4) = Voltar"
                        break
             
        case "2":       #Caso tenha escolhido "(2) = Alterar Quantidade por Pessoa / Preço"
            while True:
                os.system("cls")

                #Mostrar escolhas
                print("Escolha uma das opções abaixo:\n(1) = Mudar a Quantidade Por Pessoa;\n(2) = Mudar o Preço;\n(3) = Voltar;")
                escolha2 = input(" :: ")
                while escolha2 != "1" and escolha2 != "2" and escolha2 != "3" and escolha2 != "4":      #Caso o valor digitado não seja válido
                    os.system("cls")
                    print("O valor digitado não é válido!\n")
                    print("Escolha uma das opções abaixo:\n(1) = Mudar a Quantidade Por Pessoa;\n(2) = Mudar o Preço;\n(3) = Voltar;")
                    escolha2 = input(" :: ")
                os.system("cls")

                match escolha2:
                    case "1":       #Caso tenha escolhido "(1) = Mudar a Quantidade Por Pessoa"
                        if total > 0:       #Caso possua ingredientes cadastrados

                            #Mostar a lista de ingredientes
                            cont = 0
                            for i in nomesingredientes:

                                print(cont+1, ". Ingrediente: {0}; - Fromato de Quantidade: {1}; - Quantidade Por Pessoa: {2};\n".format(nomesingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip()))
                                cont+=1

                            #Selecionar o ingrediente que deseja alterar a quantidade recebida por pessoa
                            alterar = int(input("Digite o número do ingrediente que deseja alterar (0 = Cancelar): "))

                            while alterar > total or alterar < 0:      #Caso o valor digitado não seja válido
                                os.system("cls")
                                print("O valor digitado não é válido!\n")
                                
                                #Mostar a lista de ingredientes
                                cont = 0
                                for i in nomesingredientes:

                                    print(cont+1, ". Ingrediente: {0}; - Tipo: {1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3}; Preço: R${4};\n".format(nomesingredientes[cont].rstrip(), tiposingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip(), precoingredientes[cont].rstrip()))
                                    cont+=1

                                #Selecionar o ingrediente que deseja alterar a quantidade recebida por pessoa
                                alterar = int(input("Digite o número do ingrediente que deseja alterar (0 = Cancelar): "))
                            os.system("cls")

                            if alterar == 0:        #Caso escolha cancelar
                                print("Cancelado!\n")
                                continuar = input("Pressione Enter para continuar...")          #Pressionar enter para continuar o programa
                            else:

                                #Digitar a quantidade recebida por pessoa do ingrediente selecionado
                                print("Digite a quantidade de", qgingredientes[alterar-1].rstrip(), "de", nomesingredientes[alterar-1].rstrip(), "que cada pessoa receberá:")
                                quantidadeppessoa[alterar-1] = int(input(" :: "))
                                while quantidadeppessoa[alterar-1] <= 0:      #Caso o valor digitado não seja válido
                                    os.system("cls")
                                    print("O valor digitado não é válido!\n")
                                    print("Digite a quantidade de", qgingredientes[alterar-1].rstrip(), "de", nomesingredientes[alterar-1].rstrip(), "que cada pessoa receberá:")
                                    quantidadeppessoa[alterar-1] = int(input(" :: "))
                                os.system("cls")

                                quantidadeppessoa[alterar-1] = str(quantidadeppessoa[alterar-1])+"\n"       #Converter o valor int em str e adicionar um "\n"

                                #Limpar o arquivo "quantidades.txt"
                                arquivo = open("quantidades.txt", "w", encoding="utf-8")            #Abrir o arquivo
                                arquivo.write("")                                                   #Limpar o arquivo
                                arquivo.close()                                                     #Fechar o arquivo
                                
                                #Reescrever o arquivo "quantidades.txt"
                                arquivo = open("quantidades.txt", "a", encoding="utf-8")            #Abrir o arquivo
                                for i in quantidadeppessoa:
                                    arquivo.write(i)                                                #Escrever o valor do vetor
                                arquivo.close()                                                     #Fechar o arquivo

                        else:       #Caso não tenha ingredientes cadastrados

                            print("Você não possui nenhum ingrediente cadastrado!\n")
                            continuar = input("Pressione Enter para continuar...")          #Pressionar enter para continuar o programa

                    case "2":
                        if total >0:

                            #Mostar a lista de ingredientes
                            cont = 0
                            for i in nomesingredientes:

                                print(cont+1, ". Ingrediente: {0}; - Preço: R${1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3};\n".format(nomesingredientes[cont].rstrip(), precoingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip()))
                                cont+=1

                            #Selecionar o ingrediente que deseja alterar o preço
                            alterar = int(input("Digite o número do ingrediente que deseja alterar (0 = Cancelar): "))

                            while alterar > total or alterar < 0:      #Caso o valor digitado não seja válido
                                os.system("cls")
                                print("O valor digitado não é válido!\n")

                                #Mostar a lista de ingredientes
                                cont = 0
                                for i in nomesingredientes:

                                    print(cont+1, ". Ingrediente: {0}; - Preço: R${1}; - Fromato de Quantidade: {2}; - Quantidade Por Pessoa: {3};\n".format(nomesingredientes[cont].rstrip(), precoingredientes[cont].rstrip(), qgingredientes[cont].rstrip(), quantidadeppessoa[cont].rstrip()))
                                    cont+=1

                                #Selecionar o ingrediente que deseja alterar o preço
                                alterar = int(input("Digite o número do ingrediente que deseja alterar (0 = Cancelar): "))
                            os.system("cls")

                            if alterar == 0:        #Caso escolha cancelar
                                print("Cancelado!\n")
                                continuar = input("Pressione Enter para continuar...")          #Pressionar enter para continuar o programa
                            else:

                                #Digitar o preço do ingrediente selecionado
                                print("Digite o preço de", quantidadeppessoa[alterar-1].rstrip(), qgingredientes[alterar-1].rstrip(), "de", nomesingredientes[alterar-1].rstrip())
                                precoingredientes[alterar-1] = float(input(" :: "))
                                while precoingredientes[alterar-1] <= 0:      #Caso o valor digitado não seja válido
                                    os.system("cls")
                                    print("O valor digitado não é válido!\n")
                                    print("Digite o preço de", quantidadeppessoa[alterar-1], qgingredientes[alterar-1].rstrip(), "de", nomesingredientes[alterar-1].rstrip())
                                    precoingredientes[alterar-1] = float(input(" :: "))
                                os.system("cls")

                                precoingredientes[alterar-1] = str(precoingredientes[alterar-1])+"\n"       #Converter o valor int em str e adicionar um "\n"

                                #Limpar o arquivo "preços.txt"
                                arquivo = open("preços.txt", "w", encoding="utf-8")                 #Abrir o arquivo
                                arquivo.write("")                                                   #Limpar o arquivo
                                arquivo.close()                                                     #Fechar o arquivo
                                
                                #Reescrever o arquivo "preços.txt"
                                arquivo = open("preços.txt", "a", encoding="utf-8")                 #Abrir o arquivo
                                for i in precoingredientes:
                                    arquivo.write(i)                                                #Escrever o valor do vetor
                                arquivo.close()                                                     #Fechar o arquivo

                        else:       #Caso não tenha ingredientes cadastrados

                            print("Você não possui nenhum ingrediente cadastrado!\n")
                            continuar = input("Pressione Enter para continuar...")          #Pressionar enter para continuar o programa

                    case "3":       #Caso tenha escolhido "(3) = Voltar"
                        break

        case "3":       #Caso tenha escolhido "(3) = Fazer um Churrasco"
            if total > 0:       #Caso possua ingredientes cadastrados
                #Definir a quantidade de homens que vão ao churrasco
                print("Quantos homens vão?")
                homens = int(input(" :: "))
                os.system("cls")

                #Definir a quantidade de mulheres que vão ao churrasco
                print("Quantas mulheres vão?")
                mulheres = int(input(" :: "))
                os.system("cls")

                totalpessoas = homens+mulheres      #Definir o total de pessoas

                #Criar a tabela
                tabela=pd.DataFrame()       #Nome da tabela
                cont = 0
                
                #Converter os valores dos vetores
                for i in nomesingredientes:
                    nomesingredientes[cont] = nomesingredientes[cont].rstrip()                          #Remover os "\n" dos valores do vetor "nomesingredientes"
                    qgingredientes[cont] = qgingredientes[cont].rstrip()                                #Remover os "\n" dos valores do vetor "qgingredientes"
                    quantidadeppessoa[cont] = int(quantidadeppessoa[cont].rstrip())*totalpessoas        #Remover os "\n" dos valores do vetor, converter para int e multiplicar pela quantidade de pessoas no vetor "quantidadeppesoa"
                    precoingredientes[cont] = float(precoingredientes[cont].rstrip())*totalpessoas      #Remover os "\n" dos valores do vetor, converter para float e multiplicar pela quantidade de pessoas no vetor "precoingredientes"
                    cont+=1

                cont=0

                #Adicionar "R$" no final dos valores do vetor "precoingredientes", converter para str e salvar no vetor "precomostrar"
                for i in precoingredientes:
                    precomostrar.append("R$"+str(precoingredientes[cont]))      #Adicionar "R$" no começo do valor e converter para str
                    cont+=1

                #Definir os valores da tabela
                tabela["            Ingrediente"]=nomesingredientes         #Definir a tabela dos nomes dos ingredientes
                tabela["            Tipo"]=qgingredientes                   #Definir a tabela dos formatos de quantidade dos ingredientes
                tabela["            Quantidade"]=quantidadeppessoa          #Definir a tabela dos valores das quantidades por pessoa dos ingredientes
                tabela["            Preço"]=precomostrar                    #Definir a tabela dos preços dos ingredientes

                tabela.index = np.arange(1, len(tabela)+1)      #Mudar a formatação do index na tabela

                print("╔═══╦╗░░░░░░░░░░░░░░░░░░░░░	╔═══╗░░╔╗░░░░░░╔╗░░░╔╗░░░░░░\n║╔═╗║║░░░░░░░░░░░░░░░░░░░░░	║╔═╗║░░║║░░░░░░║║░░╔╝╚╗░░░░░\n║║░╚╣╚═╦╗╔╦═╦═╦══╦══╦══╦══╗	║║░╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗\n║║░╔╣╔╗║║║║╔╣╔╣╔╗║══╣╔═╣╔╗║	║║░╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝\n║╚═╝║║║║╚╝║║║║║╔╗╠══║╚═╣╚╝║	║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║░\n╚═══╩╝╚╩══╩╝╚╝╚╝╚╩══╩══╩══╝	╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝░\n")
                
                print(tabela)           #Mostrar a tabela

                #Mostrar informações adicionais
                print("\n<> TOTAL DE HOMENS:", homens, "  -   TOTAL DE MULHERES:", mulheres)        #Total de homens e mulheres
                print("<> TOTAL DE PESSOAS:", totalpessoas)                                         #Total de pessoas
                
                #Definir o valor da despesa total
                cont = 0
                for i in precoingredientes:
                    despesas += precoingredientes[cont]             #Somar os valores do vetor e salvar na variável "despesas"
                    cont+=1
                
                print("<> TOTAL DE DESPESAS: R$", despesas)                                         #Mostrar a despesa
                print("<> VALOR A SER PAGO POR CADA UM: R$", round(despesas/totalpessoas, 2))       #Mostrar o valor a ser pago por quem for ao churrasco

                continuar = input("\nPressione Enter para continuar...")          #Pressionar enter para continuar o programa
                print("\nCHURRAS FEITO COM SUCESSO!")
                break
    
            else:           #Caso não possua ingredientes cadastrados
                print("Não há ingredientes cadastrados para o churrasco!\n")
                continuar = input("Pressione Enter para continuar...")          #Pressionar enter para continuar o programa
            
        case "4":       #Caso tenha escolhido "(4) = Finalizar Programa"
            print("PROGRAMA FINALIZADO, SEM CHURRAS!")
            break