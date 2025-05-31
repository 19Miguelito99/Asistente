import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()
de = os.getenv('EMAIL')
contra = os.getenv('PASS')
# Se puede usar input() para debug sin voz, o recibir todo como parámetro
def enviar_correo(destinatario, asunto, mensaje):
    # if not all([EMAIL, PASS, destinatario, asunto, mensaje]):
    #     return "Todos los campos del correo son obligatorios."

    
    msg = MIMEMultipart()
    msg['From'] = de
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(de,contra)
        servidor.send_message(msg)
        servidor.quit()

        return "Correo enviado correctamente."
    except Exception as e:
        return f"Error al enviar el correo: {str(e)}"