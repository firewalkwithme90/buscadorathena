import requests
import os

def fetch_new_laws():
    url = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    query_params = {
        'siglaTipo': 'PL',
        'ordenarPor': 'dataApresentacao',
        'ordem': 'DESC',
        'itens': 10,  # Limit to 10 items for demonstration
        'palavrasChave': 'privacidade, proteção de dados'
    }
    response = requests.get(url, params=query_params)
    laws = response.json()['dados']

    new_laws_content = ""
    for law in laws:
        new_laws_content += f"### {law['siglaTipo']} {law['numero']}/{law['ano']}\n"
        new_laws_content += f"**Ementa**: {law['ementa']}\n\n"

    # Replace 'laws.md' with your filename
    with open('laws.md', 'w') as file:
        file.write(new_laws_content)

if __name__ == "__main__":
    fetch_new_laws()
