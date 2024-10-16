"""
.Synopsis
    email in python
.Description


    Example - https://realpython.com/python-send-email/

    For highly sensitive or production environments, use secrets management tools like AWS Secrets Manager, Azure Key Vault, Google Cloud Secret Manager, or HashiCorp Vault. These services provide more robust security and management capabilities.
.Author
    James Lewis
.Date
    09/30/2024
"""

import smtplib
import ssl
import getpass


#user info
senderEmail = "supercamlabs@gmail.com"
receiverEmail = "supercamlabs+alerts@gmail.com"
message = ("test alert"
           "This was sent from Python")


#port for SSL
port = 465
password = getpass.getpass(prompt= 'enter your password ')


#create a secure SSL context
context = ssl.create_default_context()

#send emails with this
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("supercamlabs@gmail.com", password)
    server.sendmail(senderEmail, receiverEmail, message)
