import smtplib
import getpass


# mail_server = smtplib.SMTP('localhost')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   (...We deleted a bunch of lines here...)
# ConnectionRefusedError: [Errno 61] Connection refused


mail_server = smtplib.SMTP_SSL('smtp.example.com')
#mail_server.set_debuglevel(1)


sender = "me@example.com"
mail_pass = getpass.getpass('Password? ')


# we can authenticate to the email server using the SMTP
mail_server.login(sender, mail_pass)



mail_server.send_message(message)
"""
The send_message method returns a 
dictionary of any recipients 
that weren’t able to receive the message.

"""

mail_server.quit()
