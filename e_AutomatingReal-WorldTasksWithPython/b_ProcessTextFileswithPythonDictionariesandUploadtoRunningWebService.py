
#! /usr/bin/env python3
import os
import requests


def main():
    src_dir = '/data/feedback'
    src_dir = 'data'
    ip = '104.197.242.231'
    url = 'http://' + ip + '/feedback/'
    reviews = file_to_dic(src_dir)
    for review in reviews:
        print(review)
        #post_review(url, review)


def post_review(url, review):
    response = requests.post(url, data=review)
    # response = requests.post(url, json=review)
    response.raise_for_status()
    if response.status_code == 201:
        print('review ok')


def file_to_dic(src_dir):
    _reviews = []
    keys = [
        'title',
        'name',
        'date',
        'feedback'
    ]
    for file in os.listdir(src_dir):
        review = {}
        path = os.path.join(src_dir, file)
        with open(path, 'r') as f:
            for i, line in enumerate(f):
                review[keys[i]] = line.rstrip()
        f.close()
        _reviews.append(review)
    return _reviews

if __name__ == '__main__':
    main()


