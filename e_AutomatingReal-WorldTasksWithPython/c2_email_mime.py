
#!/usr/bin/env python3
import os.path
import mimetypes


attachment_path = "/tmp/example.png"
attachment_path = os.path.join('data', 'example.png')
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)