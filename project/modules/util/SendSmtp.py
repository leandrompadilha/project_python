import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pretty_html_table import build_table

import project as md

email_login = os.getenv('EMAIL_LOGIN')
email_pass = os.getenv('EMAIL_PASS')
email_send = os.getenv('EMAIL_SEND')


#! Envia relatório de erros por email
def enviarEmail(erro):
    md.MessageColor.white('Enviando e-mail com aviso de erro...')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email_login, email_pass)

    corpo = f"""
    <p>Erro na execução do script:</p>
    <br>
    {erro}
    """

    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'Email automático do Python'
    email_msg.attach(MIMEText(corpo, 'html'))

    server.sendmail(email_login,
                    email_send, email_msg.as_string())
    server.quit()


def enviarEmailBase(b2c, b2b, conddm, alivios):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email_send, email_pass)

    corpo = f"""
    {build_table(b2c, 'blue_light', font_size='12px')}
    <br>
    {build_table(conddm, 'blue_light', font_size='12px')}
    <br>
    {build_table(b2b, 'blue_light', font_size='12px')}
    <br>
    {build_table(alivios, 'blue_light', font_size='12px')}
    <br>
    """

    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'Bases'
    email_msg.attach(MIMEText(corpo, 'html'))

    server.sendmail(email_login,
                    email_pass, email_msg.as_string())
    server.quit()
