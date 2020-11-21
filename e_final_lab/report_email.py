#!/usr/bin/env python3
import os
import sys
import reports
import emails
from datetime import date


def main():
    src_dir = os.path.join('supplier-data', 'descriptions')
    today = date.today().strftime("%B %d, %Y")
    title = 'Processed Update on {}'.format(today)
    filename = '/tmp/processed.pdf'
    filename = 'processed.pdf'
 
    lines = []
    data = file_to_dic(src_dir)
    for d in data:
        lines.append('name: ' + d['name'])
        lines.append('weight: ' + d['weight'])
        lines.append('')

    reports.generate_report(filename, title, '<br/>'.join(lines))

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate(sender, receiver, subject, body, filename)
    print(message)
    emails.send(message)


def file_to_dic(src_dir):
    _reviews = []
    keys = [
        'name',
        'weight',
        'description',
        'image_name'
    ]
    for file in os.listdir(src_dir):
        review = {}
        path = os.path.join(src_dir, file)
        with open(path, 'r') as f:
            for i, line in enumerate(f):
                data = line.rstrip()

                review[keys[i]] = data
                if i == 2:
                    continue
        f.close()
        _reviews.append(review)
    return _reviews


if __name__ == '__main__':
    main()
