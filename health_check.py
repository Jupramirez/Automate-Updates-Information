import psutil
import os
from dotenv import load_dotenv
load_dotenv()
import send_email

sender = os.getenv("EMAIL_SENDER")
receiver = os.getenv("EMAIL_RECIPIENT")
body = "Please check your system and fix the issue."

# checks disk usage and send email if available space is less than 20%
def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    du_present = disk_usage.free / disk_usage.total * 100
    du_threshold = 20
    if du_present < du_threshold:
        subject = "Error - available disk space is less than 20%"
        message = send_email.generate_error_email(sender, receiver, subject, body)
        send_email.send_email(sender, receiver, subject, message)
    else:
        return f"Disk usage is {du_present}%"

# Checks CPU usage and sends email if usage > 80%
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_threshold = 80
    if cpu_usage > cpu_threshold:
        subject = "Error - CPU usage is greater than 80%"
        message = send_email.generate_error_email(sender, receiver, subject, body)
        send_email.send_email(sender, receiver, subject, message)
    else:
        return f"CPU usage is {cpu_usage}%"

# Checks for available memory if less than 100MB
def check_memory_usage():
    memory_usage = psutil.virtual_memory()
    memory_threshold = 100 * 1024 * 1024
    if memory_usage.free < memory_threshold:
        subject = "Error - available memory is less than 100MB"
        message = send_email.generate_error_email(sender, receiver, subject, body)
        send_email.send_email(sender, receiver, subject, message)
    else:
        return f"Memory usage is {memory_usage.percent}%"

# Checks hostname and if cannot be resolved to "127.0.0.1"
def check_hostname():
    hostname = socket.gethostname()
    if hostname != "127.0.0.1":
        subject = "Error - hostname cannot be resolved to 127.0.0.1"
        message = send_email.generate_error_email(sender, receiver, subject, body)
        send_email.send_email(sender, receiver, subject, message)
    else:
        return f"Hostname is {hostname}"