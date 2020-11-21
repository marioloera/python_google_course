#!/usr/bin/env python3
import os
from PIL import Image


def main():
    src_dir = os.path.join('supplier-data', 'images')
    target_dir = src_dir
    for i in os.listdir(src_dir):
        if '.tiff' not in i:
            continue
        print(i)
        if (i.split('.')[0] != ''):
            format_img(i, src_dir, target_dir)

def format_img(image_name, src_dir, target_dir):
    im = Image.open(os.path.join(src_dir, image_name)).convert('RGB')
    new_name = os.path.join(target_dir, image_name.replace('.tiff','.jpeg'))
    im.resize((600, 400)).save(new_name)
    im2 = Image.open(new_name)
    print('\t', im2.format, im2.size)

if __name__ == '__main__':
    main()