
# valores_celulares = [850, 2230, 1500, 3500, 5000]
# utf8 = "utf-8"

# '''
 
#  "r"  -> Usado somente para ler algo
#  "w"  -> Usado somente para escrever algo OBS.: sobrepõe as informações antigas
#  "r+" -> Usado para ler e escrever algo
#  "a"  -> Usado para acrescentar algo OBS.: acrescenta sem sobrepor

# '''

# # COM "r"
# with open("arquivos_txt/valores_celulares.txt", "r") as arquivo: # se nn existir o arquivo, ele será criado
#     for valor in arquivo:
#         print(valor)
# # read -> arquivos simples (ex.: senhas, tokens, informações únicas)
# with open("arquivos_txt/email.txt", "r") as arquivo:
#     email = arquivo.read()
# print(email)

# # readline -> para arquivos maiores
# with open("arquivos_txt/mensagem.txt", "r", encoding = utf8) as arquivo: # encoding = "utf-8" é para aceitar caracteres especiais
#     mensagem = arquivo.readlines() # tranforma as linhas do arquivo em uma lista 
# print(mensagem)
# for linha in mensagem:
#     if "faturamento" in linha:
#         print(linha)

# # COM "w"
# with open("arquivos_txt/valores_celulares.txt", "w") as arquivo: 
#     for valor in valores_celulares:
#         arquivo.write(str(valor) + "\n")

# # COM "r+"
# with open("arquivos_txt/valores_celulares.txt", "r+") as arquivo:
#     for valor in arquivo:
#         print(valor)
#     arquivo.write("9000")

# # COM "a"
# with open("arquivos_txt/valores_celulares.txt", "a") as arquivo:
#     for valor in valores_celulares:
#         arquivo.write(str(valor) + "\n")


