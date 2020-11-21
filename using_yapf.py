#!/usr/bin/env python3
import os
from yapf.yapflib.yapf_api import FormatFile  # reformat a file

os.chdir(os.path.dirname(os.path.realpath(__file__)))

style = 'google'

LT_dir = r'C:\Users\MarioLoeraLozano\Dropbox\LT'
files_to_format = [
    #'etl_userloans_dic.py',
    LT_dir + r'\etl_usrloan\examples\usrloan_tojson.py',
    LT_dir + r'\etl_usrloan\examples\usrloan_toavro.py',
    LT_dir + r'\etl_usrloan\examples\usrloanfiles_to_bq.py',
    LT_dir + r'\etl_usrloan\src\extract_userloans.py',
    LT_dir + r'\etl_usrloan\test\extract_userloans_test.py',
    LT_dir + r'\etl_usrloan\test\extract_userloans_df2_test.py',
    LT_dir + r'\dictofile\src\save_as_avro.py',
    LT_dir + r'\dictofile\src\save_as_json.py',
    #'metrics_loading.py',
    #'etl_to_bigquery.py',
]

print('Formated files with {s}_style:'.format(s=style))

for file in files_to_format:
    FormatFile(file, style_config=style, in_place=True)
    print('\t{f}'.format(f=file))
