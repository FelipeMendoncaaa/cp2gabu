# GET Request

import requests

def get_request():
    try:
        # Solicita ao usuário que insira o URL do site
        url = input("Digite o URL do site: ")
        
        # Define os cabeçalhos desejados
        headers = {
            'User-Agent': 'Meu Bot de Teste',
            'Custom-Header': 'Valor Customizado'
        }
        
        # Define os parâmetros desejados
        parametro = {
            'parametro1': 'Esse é o parâmetro um',
            'parametro2': 'Esse é o parâmetro dois'
        }
        
        # Faz a solicitação HTTP GET
        resposta = requests.get(url, headers=headers, params=parametro)
        
        # Verifica se a solicitação foi bem sucedida
        if resposta.status_code == 200:
            print("Solicitação bem-sucedida!")
            print("Conteúdo da resposta:")
            print(resposta.text)
        else:
            print(f"A solicitação falhou com o código de status: {resposta.status_code}")
    except Exception as e:
        print(f"Erro ao fazer a solicitação HTTP GET: {str(e)}")

if __name__ == "__main__":
    get_request()



