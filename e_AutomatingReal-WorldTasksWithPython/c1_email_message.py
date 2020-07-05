
#!/usr/bin/env python3
import os
from email.message import EmailMessage


message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)

print(message)


# if __name__ == '__main__':
#     main()