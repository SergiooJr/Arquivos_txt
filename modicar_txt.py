valores_celulares = [850, 2230, 1500, 3500, 5000]

'''
 
 "r"  -> Usado somente para ler algo
 "w"  -> Usado somente para escrever algo
 "r+" -> Usado para ler e escrever algo
 "a"  -> Usado para acrescentar algo

'''

# # COM "r"
# with open("valores_celulares.txt", "r") as arquivo:
#     for valor in arquivo:
#         print(valor)

# # COM "w"
# with open("valores_celulares.txt", "w") as arquivo: # se nn existir o arquivo, ele será criado
#     for valor in valores_celulares:
#         arquivo.write(str(valor) + "\n")

# # COM "r+"
# with open("valores_celulares.txt", "r+") as arquivo:
#     for valor in arquivo:
#         print(valor)
#     arquivo.write("9000")

# # COM "a"
with open("valores_celulares.txt", "a") as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + "\n")


