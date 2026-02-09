import email.message
import smtplib
import os.path
import smtplib


def generate_email_body(sender, receiver, subject, body, attachment_path):
    """Generate an email body."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    maintype, subtype = mime_type.split("/",1)

    if attachment_path:
        with open(attachment_path, "rb") as f:
            message.add_attachment(f.read(), maintype=maintype, 
                                    subtype=subtype, 
                                    filename=attachment_filename)
    
    return message

def generate_error_email(sender, recipient, subject, body):
    """Creates an email without an attachment."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    
    return message

def send_email(message):
    """Send an email to the configure SMTP server"""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
