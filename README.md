# Criptografia e Descriptografia de Arquivos

Este projeto implementa um sistema simples de **criptografia e descriptografia** de arquivos, utilizando o algoritmo **AES (Advanced Encryption Standard)** no modo **CTR (Counter)**. O projeto foi desenvolvido para ilustrar como proteger arquivos sensíveis, criptografando-os de maneira segura e permitindo a restauração dos arquivos originais mediante a descriptografia.

## OBS: Caso precise mais de um arquivo para criptograia e desccriptografia  use encriptdiversos o descriptdiversos###


## Funcionalidades

- **Criptografar** arquivos: O arquivo original é criptografado utilizando uma chave definida pelo usuário e o resultado é salvo com um sufixo `.ransomwaretroll`.
- **Descriptografar** arquivos: O arquivo criptografado pode ser restaurado ao seu formato original, utilizando a chave correta.

## Como funciona

1. **Criptografia**:
   - O arquivo de entrada é lido e criptografado usando o algoritmo **AES-CTR**.
   - O arquivo criptografado é salvo com o sufixo `.ransomwaretroll`.
   - O arquivo original é removido após a criptografia ser concluída com sucesso.

2. **Descriptografia**:
   - O arquivo criptografado é procurado no diretório de trabalho.
   - Após encontrá-lo, o arquivo é descriptografado de volta ao seu estado original.
   - O arquivo descriptografado é salvo com o nome original (sem o sufixo `.ransomwaretroll`).

## Requisitos

- Python 3.x
- Biblioteca `pyaes` (para criptografia AES)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
Instale as dependências:
pip install pyaes
Exemplo de Uso
Criptografando teste.txt:

python criptografar.py
Isso irá gerar o arquivo teste.txt.ransomwaretroll e excluir o arquivo original teste.txt.

Descriptografando teste.txt.ransomwaretroll:

python descriptografar.py
Isso irá gerar o arquivo original teste.txt a partir do arquivo criptografado teste.txt.ransomwaretroll.

Observações
A chave de criptografia usada no projeto é fixa, definida como testeransomwares. Em um ambiente de produção, é recomendável utilizar chaves mais seguras e gerenciadas dinamicamente.
A criptografia é realizada no modo CTR do algoritmo AES, o que garante que a operação seja segura e eficiente.
O projeto não armazena chaves nem realiza autenticação, então é importante garantir a segurança da chave de criptografia.
Contribuição
Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades. Para isso, basta fazer um fork do repositório, realizar suas alterações e enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

