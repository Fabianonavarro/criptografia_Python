import os
import pyaes
import logging

# Configurar o log
log_file = "log_descriptdiversos.txt"  # Nome do arquivo de log
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Início do processo
logging.info("Início do processo")
print("Início do processo")

# Obter o diretório onde o script está sendo executado
diretorio = os.getcwd()  # Obtém o diretório de execução atual
logging.info(f"Diretório encontrado: OK")
print(f"Diretório encontrado: OK")

# Verificação do diretório
if not os.path.exists(diretorio):
    logging.error(f"[ERRO] O diretório {diretorio} não existe.")
    print(f"[ERRO] O diretório {diretorio} não existe.")
else:
    try:
        # Listar os arquivos encontrados no diretório
        arquivos = os.listdir(diretorio)
    except Exception as e:
        logging.error(f"[ERRO] Falha ao listar arquivos no diretório: {e}")
        print(f"[ERRO] Falha ao listar arquivos no diretório: {e}")
        arquivos = []

    # Filtrar apenas arquivos criptografados .txt.ransomwaretroll
    arquivos_criptografados = [file for file in arquivos if file.endswith(".txt.ransomwaretroll")]
    
    # Exibir apenas os arquivos criptografados encontrados
    if arquivos_criptografados:
        logging.info(f"Arquivos criptografados encontrados: {arquivos_criptografados}")
        print(f"Arquivos criptografados encontrados: {arquivos_criptografados}")
    else:
        logging.info("Nenhum arquivo criptografado encontrado.")
        print("Nenhum arquivo criptografado encontrado.")

    arquivos_restaurados = []  # Para armazenar os arquivos que serão restaurados

    # Foco na descriptografia de cada arquivo .txt.ransomwaretroll
    for file_name in arquivos_criptografados:
        logging.info(f"Iniciando descriptografia do arquivo: {file_name}")
        print(f"Iniciando descriptografia do arquivo: {file_name}")
        
        file_path = os.path.join(diretorio, file_name)

        try:
            # Verifique se o arquivo existe antes de abrir
            if not os.path.isfile(file_path):
                logging.error(f"[ERRO] O arquivo {file_name} não foi encontrado.")
                print(f"[ERRO] O arquivo {file_name} não foi encontrado.")
                continue  # Pular para o próximo arquivo
            
            # Ler o arquivo criptografado em blocos (chunks)
            logging.info(f"Lendo arquivo criptografado: {file_name}")
            print(f"Lendo arquivo criptografado: {file_name}")
            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            logging.info(f"Arquivo {file_name} lido com sucesso!")
            print(f"Arquivo {file_name} lido com sucesso!")

            # Descriptografar o arquivo
            logging.info(f"Descriptografando o arquivo: {file_name}")
            print(f"Descriptografando o arquivo: {file_name}")
            aes = pyaes.AESModeOfOperationCTR(b"testeransomwares")
            decrypted_data = aes.decrypt(encrypted_data)

            logging.info(f"Arquivo {file_name} descriptografado com sucesso!")
            print(f"Arquivo {file_name} descriptografado com sucesso!")

            # Criar o nome do arquivo original (removendo o sufixo .ransomwaretroll)
            new_file_name = file_name.replace(".ransomwaretroll", "")
            new_file_path = os.path.join(diretorio, new_file_name)

            # Salvar o arquivo descriptografado
            logging.info(f"Salvando arquivo descriptografado como: {new_file_name}")
            print(f"Salvando arquivo descriptografado como: {new_file_name}")
            with open(new_file_path, "wb") as new_file:
                new_file.write(decrypted_data)

            logging.info(f"Arquivo {file_name} descriptografado e salvo como {new_file_name}")
            print(f"Arquivo {file_name} descriptografado e salvo como {new_file_name}")

            # Remover o arquivo criptografado após descriptografia
            logging.info(f"Removendo arquivo criptografado: {file_name}")
            print(f"Removendo arquivo criptografado: {file_name}")
            os.remove(file_path)

            logging.info(f"Arquivo criptografado {file_name} removido com sucesso.")
            print(f"Arquivo criptografado {file_name} removido com sucesso.")

            # Adicionar ao registro de arquivos restaurados
            arquivos_restaurados.append(new_file_name)

        except Exception as e:
            logging.error(f"[ERRO] Falha ao processar o arquivo {file_name}: {e}")
            print(f"[ERRO] Falha ao processar o arquivo {file_name}: {e}")

    # Exibir arquivos restaurados ao final
    if arquivos_restaurados:
        logging.info(f"Arquivos restaurados: {arquivos_restaurados}")
        print(f"Arquivos restaurados: {arquivos_restaurados}")
    else:
        logging.info("Nenhum arquivo foi restaurado.")
        print("Nenhum arquivo foi restaurado.")

logging.info("Processamento concluído.")
print("Processamento concluído.")
