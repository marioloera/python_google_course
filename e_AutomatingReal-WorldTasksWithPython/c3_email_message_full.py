
#!/usr/bin/env python3
import os
import mimetypes
from email.message import EmailMessage


message = EmailMessage()

sender = 'me@example.com'
recipient = 'you@example.com'
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)


attachment_path = os.path.join('data', 'example.png')
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

print(message)


