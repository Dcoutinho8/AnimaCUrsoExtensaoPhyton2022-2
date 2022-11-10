# Funções 

preco = 19.90 

#Calcular 5% de imposto , guardar na variavel imposto e exibir na tela 

imposto = preco * 0.05 
print( imposto) 

preco2 = 100 
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcula um  imposto de 5% e retorna a quem pediu...
#isso é a declaração da função (como ela funciona)
def calcular_imposto(preco_produto): 
    imposto = preco_produto * 0.5
    return imposto

#Aqui é o uso do imposto a calcular
preco = 299 
imposto = calcular_imposto(preco)
print(imposto)

#agora calcular imposto a alíquota agora é 7% 
def calcular_imposto(preco_produto): 
    imposto = preco_produto * 0.5
    return imposto

#vc apenas troca o valor, caso n usasse a função teria q trocar um por um q vc utilizou essa conta de impsoto 

preco = 299 
imposto = calcular_imposto(preco)
print(imposto)
#Esse utiliza os 7% 

valores = [1.99,24.50,78.27,1515.5]
#Se eu quiser calcular o imposto destes quatros valores exemplo: "o imposto de... é ..." (1o. preço, 2o. imposto)
for valor in valores:
    print(f"o Imposto de {valores} é {calcular_imposto(valores)}")