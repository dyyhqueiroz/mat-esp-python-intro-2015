# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
cartas  = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]  

cincomais = [19, 18, 17, 16, 15] # estao sendo apontados os cinco maiores valores da lista original  
cincomenos = [0, 1, 2, 3, 4]      # estao sendo descritos os cinco menores valores da lista original 

print("lista original: ",cartas) # serve para mostrar a ordem original das cartas quando o programa rodar"

N = 20                            #N e o numero total de cartas"
count_troca = 0                   # Essa ferramenta serve para dizer que a contagem de troca começa pelo zero 
count_it = 0                      # Estamos definindo que as iterações iniciam a partir do zero

plt.figure() # aqui uma figura em branco é criada
plt.plot(range(N),cartas,'ok') #aqui preenchemos-na com os dados crus
plt.title("Lista Original") #para dar nome ao meu gráfico
plt.xlabel(u"Posição") #nomeamos o eixo X
plt.ylabel("Valor") #nomeamos o eixo Y
plt.savefig("fig/bubble-inicio.png") #comando para salvar a figura na pasta fig
plt.close #fecha a figura


for i in range(0 , N - 1, 1):     #i= representa a primeira carta a ser considerada"
    for j in range(i + 1, N , 1): #j= e a carta posterior a carta[i]"
        

        plt.figure() # aqui uma figura em branco é criada
        plt.plot(range(N),cartas,'ok') #aqui preenchemos-na com os dados crus
        plt.plot(i, cartas[i], 'or')
        plt.plot(j, cartas[j], 'ob')
        count_it = count_it+1 #ai no contador eu adiciono um numero a mais pra ser o numero do meu grafico
        plt.title(u"Iteração-{}".format(count_it)) #para dar nome ao meu gráfico
        plt.xlabel(u"Posição") #nomeamos o eixo X
        plt.ylabel("Valor") #nomeamos o eixo Y
        plt.savefig("fig/bubble-it-{}.png".format(count_it)) #comando para salvar a figura na pasta fig
        plt.close #fecha a figura
        

        if cartas[i] > cartas[j]: #Assim se a carta[i] for maior que [j] inverte-se a ordem delas"
            temp = cartas[i]      #O temp serve como um opcao auxiliar onde a carta[i] e guardada para que haja uma permutacao com a carta [j]"
            cartas[i] = cartas[j] #Armazenando-se a carta[i] no temp e possivel colocar a carta[j] em seu lugar" 
            cartas[j] = temp      #O temp nesse caso vai servir de auxiliar para a carta[j] e assim entao e possivel fazer a permutacao com a carta[i]" 
            

            plt.figure() # aqui uma figura em branco é criada
            plt.plot(range(N),cartas,'ok') #aqui preenchemos-na com os dados crus
            count_troca = count_troca+1 #ai no contador eu adiciono um numero a mais pra ser o numero do meu grafico
            plt.title("Troca-{}".format(count_troca)) #para dar nome ao meu gráfico
            plt.xlabel(u"Posição") #nomeamos o eixo X
            plt.ylabel("Valor") #nomeamos o eixo Y
            plt.savefig("fig/bubble-troca-{}.png".format(count_troca)) #comando para salvar a figura na pasta fig
            plt.close #fecha a figura

print("lista final em ordem crescente: ",cartas)                     #O print e um comando para ordenar as cartas"  

plt.figure() # aqui uma figura em branco é criada
plt.plot(range(N),cartas,'ok') #aqui preenchemos-na com os dados crus
plt.title("Lista Final") #para dar nome ao meu gráfico
plt.xlabel(u"Posição") #nomeamos o eixo X
plt.ylabel("Valor") #nomeamos o eixo Y
plt.savefig("fig/bubble-fim.png") #comando para salvar a figura na pasta fig
plt.close #fecha a figura


print("cinco maiores valores", cincomais)      # Esse comando serve para que o programa faça a leitura dos cinco maiores valores
print("cinco menores valores", cincomenos)      # Esse comando faz com que o python indique os cincos menores valores quando o programa rodar


