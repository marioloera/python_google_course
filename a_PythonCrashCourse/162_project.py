# # Here are all the installs and imports you will need for your word cloud script and uploader widget

# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload

# import wordcloud
# import numpy as np
# from matplotlib import pyplot as plt
# from IPython.display import display
# import fileupload
# import io
# import sys

# This is the uploader widget

# def _upload():

#     _upload_widget = fileupload.FileUploadWidget()

#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()

#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)

# _upload()

##
#split text in words
#remove punctuation marks
#lower case
#remove irrelevant words 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ['if', 'the', 'a', 'an', 'is', 'are', 'to', 'if', 'and', 'or'] 


file_contents = 'Miguel Ángel Félix Gallardo (born January 8, 1946), miguel  ÁNGEL   referred to by his alias El Padrino ("The Godfather")'
print(file_contents)

#remove punctuation marks
clean_text = ''
for c in file_contents:
    if c not in punctuations:
        clean_text += c
print(clean_text)

#split into words
words = clean_text.split(' ')
print(words)

#count frequecies and ignore 
frequencies = {}
for word in words:
    w = word.lower()
    if w not in uninteresting_words:
        if w not in frequencies.keys():
            frequencies[w] = 0
        frequencies[w] += 1
print(frequencies)

# cloud = wordcloud.WordCloud()
# cloud.generate_from_frequencies(frequencies)
# cloud.to_file("myfile.jpg")
