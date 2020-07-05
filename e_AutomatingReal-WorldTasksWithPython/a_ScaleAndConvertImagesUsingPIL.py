
#!/usr/bin/env python3
import os
from PIL import Image


def main():
    src_dir = 'images'
    target_dir = 'test'
    target_dir = '/opt/icons'
    for i in os.listdir(src_dir):
        print(i)
        if (i.split('.')[0] != ''):
            format(i, src_dir, target_dir)

def format(image_name, src_dir, target_dir):
    im = Image.open(os.path.join(src_dir, image_name)).convert('RGB')
    new_name = os.path.join(target_dir, image_name+'.jpeg')
    im.rotate(90).resize((128, 128)).save(new_name)
    im2 = Image.open(new_name)
    print('\t', im2.format, im2.size)

if __name__ == '__main__':
    main()
