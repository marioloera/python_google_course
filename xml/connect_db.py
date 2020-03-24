import  pyodbc
import pandas as pd
import xml.etree.ElementTree as ET
from extract_uc_data import UCData as UC
import pprint
import csv

pp = pprint.PrettyPrinter(indent=0)

class ConnAZ():
    
    def __init__(self):
        self.username = 'malo@lendify.se'
        self.password = 'PAwin01123*1'
        self.server = 'po4ncqs1n2.database.windows.net'
        self.database = 'Export'
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.appintent = 'ReadOnly'
        self.auth = 'ActiveDirectoryPassword'
        self.__connect_read__()
        return

    def __connect_read__(self):
        self.__engn__ = pyodbc.connect(
                    r'DRIVER={'+self.driver+'};'
                    r'SERVER='+self.server+';'
                    r'DATABASE='+self.database+';'
                    r'UID='+self.username+';'
                    r'PWD='+self.password+';'
                    r'ApplicationIntent='+self.appintent+';'
                    r'Authentication='+self.auth+''
                    )
        return

    def get_data(self,query):
        dfsql = pd.read_sql(query, self.__engn__)
        return dfsql


def main():
    print('start.')

    records_to_fetch = 150

    ids_with_error_file = 'ids_with_error.log'
    ids_without_error_file = 'ids_without_error.log'
    max_id_file = 'max_id_file.log'

    ids_with_error = {}
    ids_without_error = set()
    new_errors = 0

    with open(ids_with_error_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_with_error[int(row['score_id'])] = row['error_message']
        f.close()
    max_id = 0

    with open(max_id_file, 'r') as f:
        lines = f.readline()
        max_id = int(lines)
        f.close()
    ids_error_str  = ','.join(str(id) for id in ids_with_error)
    
    where_condition = '\nAND ScoreId < {0}'.format(max_id)
    if len(ids_with_error) > 0:
        where_condition += '\nAND ScoreId IN ({ids})'.format(ids=ids_error_str)

    query = "SELECT TOP ({rec}) ScoreId, LendifyUser_Id, UCData \
            \nFROM dbo.UserCreditScores \
            \nWHERE UCData != '' {where_condition}\
            \nORDER BY ScoreId;".format(rec=records_to_fetch, where_condition=where_condition)

    print('fetching {rec} rows from the database.'.format(rec=records_to_fetch))
    connAZ = ConnAZ()
    df = connAZ.get_data(query)

    print('fetched rows: {rec}.'.format(rec=len(df.index)))
    print('et script:')
    uc = UC()
    print('total_errors:'+str(len(ids_with_error)))
    for index, row in df.iterrows():
        score_id = int(row['ScoreId'])
        #uc_dic = uc.get_dic_xml(row['UCData'])
        try:
            flat_uc_df, uc_replay_status = uc.get_dataframe(row['UCData'], score_id, row['LendifyUser_Id'])
                                                
            if uc_replay_status == 'ok':
                ids_without_error.add(score_id)

            else:
                new_errors += 1
                ids_with_error[score_id] = uc_replay_status
                filename = 'xml_error\{id}_{msg}.xml'.format(id=score_id, msg=uc_replay_status)
                make_new_file(filename, row['UCData'])
        
        except:
            new_errors += 1
            # ids_with_error.add(score_id)
            # ids_with_error.append('{id}, {er}'.format(id=score_id, er='except'))
            ids_with_error[score_id] = 'except'

            #print('\n\terror at ScoreID: {id}'.format(id=score_id)) 
            pass
    
    print('total_errors:'+str(len(ids_with_error)))

    #max_id = score_id
    
    dic_to_file(ids_with_error_file, ids_with_error)
    #set_to_file(ids_without_error_file, ids_without_error)
    #save_max_id(max_id_file, max_id)
    
    print('new_errors:',new_errors)
    print('\nend!')

def make_new_file(filename, text):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(str(text))
        f.close()

def save_max_id(filename, max_id):
    with open(filename, 'w') as f:
        f.write(str(max_id))
        f.close()

def dic_to_file(filename, dic):
    with open(filename, 'w') as f:
        f.write('{k},{v}'.format(k='score_id', v='error_message'))

        for key, value in dic.items():
            f.write('\n{k},{v}'.format(k=key, v=value.strip()))
        f.close()

def set_to_file(filename, set_ids):
    list_id = list(set_ids)
    list_id.sort()
    with open(filename, 'a') as f:
        f.writelines("%s\n" % id for id in list_id)
        f.close()


main()