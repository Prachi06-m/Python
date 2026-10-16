import os
import smtplib
from email.message import EmailMessage
from  dotenv import load_dotenv
from app.schemas.email_schema import EmailCreate

load_dotenv()


class EmailService:
    def__init__(self):
        pass
    
    def send_email(self,email):
        if isinstance(email,dict):
            email=EmailCreate(**email)


        sender_email=os.getnv("EMAIL_ADDRESS")
        app_password=os.getenv("EMAIL_APP_PASSWORD") 

        if not sender_email or not app_password:
            raise RuntimeError("EMAIL_ADDRESS or EMAIL_APP_PASSWORD is missing in .env")

        message = EmailMessage()
        message["Subject"] = email.subject
        message["From"] = sender_email
        message["To"] = email.receiver_email
        message.set_content(email.body)

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(message)




