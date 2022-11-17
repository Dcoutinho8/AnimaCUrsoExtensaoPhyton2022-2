import aula4part3 as bd

conexao, cursor = bd.conectar() 

nome = input("Informe o nome de herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para vilã(o): ")

# Consulta para o valor máximo usado no banco 
sql = "SELECT MAX(pessoa_id)+1 FROM pessoa "
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if tipo_numerico == "1": 
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id,nome, nome_civil,tipo) VALUES ({pessoa_id}, '{nome}','{nome_civil}','{tipo}')"

cursor.execute(sql)
cursor.commit()
cursor.close()