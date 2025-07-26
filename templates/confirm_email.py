from datetime import datetime

def create_template(nome, codigo):
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")

    conteudo_html = f"""
    <!DOCTYPE html>
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
        <div style="background-color: white; padding: 20px; border-radius: 8px;">
        <h2 style="color: #0d6efd;">Olá, {nome}!</h2>
        <p>Para finalizar seu cadastro na plataforma utilize o código de verificação</p>
        <p><strong>Data:</strong> {date}</p>
        <p style="margin-top: 20px;">{codigo}</p>
        <p style="margin-top: 40px; font-size: 12px; color: #666;">Este é um e-mail automático. Por favor, não responda.</p>
        </div>
    </body>
    </html>
    """

    return conteudo_html