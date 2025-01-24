import os
import pyaes

# Função para encontrar o arquivo criptografado
def find_encrypted_file(directory, suffix=".ransomwaretroll"):
    for filename in os.listdir(directory):
        if filename.endswith(suffix):
            return os.path.join(directory, filename)
    return None  # Nenhum arquivo encontrado

# Diretório atual
current_directory = os.getcwd()

# Procurar o arquivo criptografado
encrypted_file = find_encrypted_file(current_directory)

if encrypted_file:
    print(f"Arquivo criptografado encontrado: {encrypted_file}")

    # Abrir o arquivo criptografado
    with open(encrypted_file, "rb") as file:
        file_data = file.read()

    # Chave de descriptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar o arquivo
    decrypt_data = aes.decrypt(file_data)

    # Criar o nome do arquivo descriptografado (restaurando o nome original)
    new_file_name = encrypted_file.replace(".ransomwaretroll", "")

    # Salvar o arquivo descriptografado
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    print(f"Arquivo descriptografado e salvo como {new_file_name}.")
else:
    print("Nenhum arquivo criptografado encontrado no diretório.")
