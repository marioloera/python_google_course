#!/usr/bin/env python3
import os
import requests

def main():
    url = "http://localhost/upload/"
    src_dir = os.path.join('supplier-data', 'images')
    for i in os.listdir(src_dir):
        if '.jpeg' not in i:
            continue
        print(i)
        uppload_image(os.path.join(src_dir, i), url)

def uppload_image(image, url):
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

if __name__ == '__main__':
    main()
