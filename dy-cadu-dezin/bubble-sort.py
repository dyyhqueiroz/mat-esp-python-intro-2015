cartas  = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]  
N = 20                            #N e o numero total de cartas"
for i in range(0 , N - 1, 1):     #i= representa a primeira carta a ser considerada"
    for j in range(i + 1, N , 1): #j= e a carta posterior a carta[i]"
        if cartas[i] > cartas[j]: #Assim se a carta[i] for maior que [j] inverte-se a ordem delas"
            temp = cartas[i]      #O temp serve como um opcao auxiliar onde a carta[i] e guardada para que haja uma permutacao com a carta [j]"
            cartas[i] = cartas[j] #Armazenando-se a carta[i] no temp e possivel colocar a carta[j] em seu lugar" 
            cartas[j] = temp      #O temp nesse caso vai servir de auxiliar para a carta[j] e assim entao e possivel fazer a permutacao com a carta[i]" 
print(cartas)                     #O print e um comando para ordenar as cartas"  