import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def fetch_new_laws():
    url = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    params = {
        'siglaTipo': 'PL',
        'ordenarPor': 'dataApresentacao',
        'ordem': 'DESC',
        'itens': 10,
        'palavrasChave': 'privacidade, proteção de dados'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        laws = response.json()['dados']
        return laws
    else:
        return []

def send_email(laws):
   sender = os.getenv('EMAIL_USER')
    receiver = os.getenv('EMAIL_USER')  # ou outro e-mail de destino, se desejar
    password = os.getenv('EMAIL_PASS')
    subject = "Novas Leis de Privacidade e Proteção de Dados"

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    # Email body
    body = "Confira as últimas leis propostas:\n\n"
    for law in laws:
        body += f"{law['siglaTipo']} {law['numero']}/{law['ano']} - {law['ementa']}\n"
    message.attach(MIMEText(body, 'plain'))

    # SMTP session
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Use smtp.gmail.com for Gmail
    session.starttls()  # Enable security
    session.login(sender, password)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()

if __name__ == "__main__":
    laws = fetch_new_laws()
    if laws:
        send_email(laws)
