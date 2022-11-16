#Aula de estrutura de repetição

#Contado de 1 até 10 
contador = 1 
while (contador <= 10):
    print(contador)
    contador = contador + 1 
    #contador += 1 == contador = contador + 1 


#Arraylist exemlos e vetores 
fruta = morango
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3= "pêra"

#Lista 
frutas = ["Morango", "Laranja", "Pêra"]

#frutas = ["Morango", "Laranja", "Pêra"] -> Morango 0 / Laranja 1 / Pêra 2 
#Exibir só a 3a fruta 
print(frutas[2])

#Exibir quantas frutas tem na minha lista
print(len(frutas)) # length = tamanho 

#Quero incluir um fruta nova
frutas.append("manga")

print(frutas[0])
print(frutas[1])
print(frytas[2])
print(frutas[3])

i = 0 
while(i < len(frutas) ):
    print (frutas[i])
    i += 1 

# Laço for (python for = for each )

print("Exemplo das frutas com FOR")
for fruta in frutas:
        print(fruta)