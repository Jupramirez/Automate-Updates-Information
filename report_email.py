#!/usr/bin/env python3
import os
import mimetypes
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
load_dotenv()

gmail_user = os.getenv("EMAIL_USER")
gmail_password = os.getenv("EMAIL_PASSWORD")

def generate_email(sender, recipient, subject, body, attachment_path=None):
    """Create an email message, optionally with a file attachment."""
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path and os.path.exists(attachment_path):
        mime_type, _ = mimetypes.guess_type(attachment_path)
        if mime_type is None:
            mime_type = "application/octet-stream"
        maintype, subtype = mime_type.split("/", 1)

        with open(attachment_path, "rb") as f:
            message.add_attachment(
                f.read(),
                maintype=maintype,
                subtype=subtype,
                filename=os.path.basename(attachment_path),
            )
    return message

def send_email(message):
    """Sends the email using Gmail SMTP server."""
    # It is highly recommended to use environment variables for these
    gmail_user = os.getenv("EMAIL_USER")
    gmail_password = os.getenv("EMAIL_PASSWORD")

    # Connect to Gmail's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(gmail_user, gmail_password)
        server.send_message(message)
        print("Email sent successfully!")

if __name__ == "__main__":
    sender = os.getenv("EMAIL_USER")
    recipient = os.getenv("EMAIL_RECIPIENT")
    subject = "Fruit Store Automation Report"
    body = "The fruit catalog has been updated. Please find the PDF report attached."
    
    attachment = "processed.pdf"
    
    msg = generate_email(sender, recipient, subject, body, attachment)
    send_email(msg)
