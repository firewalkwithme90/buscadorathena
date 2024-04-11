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

    name: Fetch New Laws

on:
  schedule:
    - cron: '0 12 * * *'  # Runs at 12:00 UTC every day

jobs:
  fetch-and-update-laws:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Run fetch_laws script
        run: python fetch_laws.py

      - name: Commit and push if changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add .
          git commit -m "Update laws list" -a || echo "No changes to commit"
          git push


    new_laws_content = ""
    for law in laws:
        new_laws_content += f"### {law['siglaTipo']} {law['numero']}/{law['ano']}\n"
        new_laws_content += f"**Ementa**: {law['ementa']}\n\n"
        

    # Replace 'laws.md' with your filename
    with open('laws.md', 'w') as file:
        file.write(new_laws_content)

if __name__ == "__main__":
    fetch_new_laws()
