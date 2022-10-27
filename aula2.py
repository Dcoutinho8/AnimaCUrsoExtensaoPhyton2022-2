#Aula 2 
#AS LINHAS DE COMANDO É APENAS PARA DEMONSTRAÇÃO, SE DER RUN NÃO IRA FUNCIONAR CORRETAMENTE 
#Comando input(): JOptionPane do Python
# Qnd n se declara sempre vai ser Str 
nome = input("Digite seu nome: ") 
#X = int/Double (input("xxxxxxxxxxxxx"))
idade = int(input("Qual a sua idade: "))

genero = input("Informe o gênero M=Masculino e F=Feminino: ")

#comando de saída.. exibir na tela 
print(f"Boa noite {nome} você já tem {idade} anos")

dobro = idade * 2 

print("O drobro da sua idade é", dobro)

#ESTRUTURA  CONDICIONAL - IF/ELSE
#PARA "FECHAR" O "ESCOPO" DO IF É SÓ NÃO DEIXAR ALINHADO COM ELE - SEGUE O EXEMPLO ABAIXO 
if (idade >= 18):
   print ("Você é maior de idade, já pode beber e dirigir (ao mesmo tempo)")

print ("Está linha não faz parte do IF")

#EXEMPLO DE ELSE 
if (idade >= 18): 
    print ("Você é maior de idade, já pode beber e dirigir (ao mesmo tempo)")
else: 
    print("Você é de menor")

#EXEMPLO COM ELIF (ELSE + IF)
if (idade >= 18 and genero == "M"): 
    print ("... e você também precisa/precisou prestar o serviço militar obrigatório") 

#EXEMPLO PRÓPRIO
if (idade >= 18): 
    print ("Você é maior de idade, já pode beber e dirigir (ao mesmo tempo)")    
elif (idade >= 11): 
    print ("Você ainda é um adolescente")
elif (idade <= 10):
    print ("Você é um criança") 

