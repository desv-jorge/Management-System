import smtplib
from email.message import EmailMessage

from templates.confirm_email import create_template

from models.email import Model_email_confirm

def confirm_email(confirm_email_body: Model_email_confirm):
    conteudo_html = create_template(confirm_email_body.nome,confirm_email_body.codigo)

    msg = EmailMessage()
    msg["Subject"] = "Confirmação de Email"
    msg["From"] = "jorgenathanael53@gmail.com"
    msg["To"] = confirm_email_body.email

    # Conteúdo em texto simples (fallback)
    msg.set_content("Seu e-mail não suporta HTML.")

    # Conteúdo em HTML
    msg.add_alternative(conteudo_html, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("jorgenathanael53@gmail.com", "tjimejazwiumrhwd")
        smtp.send_message(msg)

    return {"message" : "Código de confirmação enviado"}

