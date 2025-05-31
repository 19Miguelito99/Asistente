import smtplib
from config import EMAIL, PASSWORD

def enviar_correo(para, asunto, mensaje):
    cuerpo = f"Subject: {asunto}\n\n{mensaje}"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, para, cuerpo)
        server.quit()
        return "Correo enviado exitosamente."
    except Exception as e:
        return f"Error al enviar el correo: {e}"
