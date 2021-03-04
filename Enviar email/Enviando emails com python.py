from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


meu_email = 'nenesandro10@gmail.com'
minha_senha = '1049637227'

# with open('template.html', 'r') as html:
# template = Template(html.read())
# data_atual = datetime.now().strftime('%d/%m/%Y')
# corpo_msg = template.substitute(nome='Nene', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Nene Sandro'
msg['to'] = 'laa.guimaraess89@gmail.com'
#ASSUNTO
msg['subject'] = 'Atenção: esse é um email de teste.'

#MENSAGEM
corpo = MIMEText('Eu te amo')
msg.attach(corpo)

#ENVIO DE IMAGEM EM ANEXO
with open('aaa.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('nenesandro10@gmail.com', 1049637227)
        smtp.send_message(msg)
        print('Email enviado com sucesso!')
    except Exception as e:
        print('Email não enviado!')
        print('Erro: ', e)
