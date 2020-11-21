
#! /usr/bin/env python3
import os
import requests


def main():
    src_dir = os.path.join('supplier-data', 'descriptions')
    ip = '34.72.39.31'
    url = 'http://' + ip + '/fruits/'
    data = file_to_dic(src_dir)
    for d in data:
        #print(d)
        print(d['name'], d['weight'], d['image_name'])
        #post_review(url, d)


def post_review(url, review):
    response = requests.post(url, data=review)
    response.raise_for_status()
    if response.status_code == 201:
        print('review ok')


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
                # special case for weight: 500 lbs
                if i == 1:
                    weight = data.split(' ')[0]
                    review[keys[i]] = int(weight)
                    continue
                review[keys[i]] = data
            review[keys[3]] = file.replace('.txt', '.jpeg')
        f.close()
        _reviews.append(review)
    return _reviews

if __name__ == '__main__':
    main()


