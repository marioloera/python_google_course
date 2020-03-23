import  pyodbc
import pandas as pd
import xml.etree.ElementTree as ET
from ucdata import UCData as UC
import pprint

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

    connAZ = ConnAZ()
    records = 1000

    print('getting ids_with_error from file')
    ids_with_error_file = 'ids_with_error.log'
    ids_without_error_file = 'ids_without_error.log'


    ids_with_error = set()
    ids_without_error = set()

    new_errors = 0
    with open(ids_with_error_file, 'r') as f:
        for line in f:
            ids_with_error.add(int(line.strip()))
        f.close()

    min_id = None
    with open(ids_without_error_file, 'r') as f:
        for line in f:
            id = int(line.strip())
            ids_without_error.add(id)
            if min_id == None:
                min_id = id
            min_id = min(min_id, id)
        f.close()
    ids_error_str  = ','.join(str(id) for id in ids_with_error)
    where_condition = '\nAND ScoreId < {0}'.format(min_id)
    if len(ids_with_error) > 0:
        pass
        # where_condition += '\nAND ScoreId NOT IN ({ids})'.format(ids=ids_error_str)

    query = 'SELECT TOP ({rec}) ScoreId, UCData \
            \nFROM dbo.UserCreditScores \
            \nWHERE UCData IS NOT NULL {where_condition}\
            \nORDER BY ScoreId DESC;'.format(rec=records, where_condition=where_condition)
    print(query)
    print('fetching {rec} rows from the database.'.format(rec=records))
    df = connAZ.get_data(query)
    print('fetched rows: {rec}.'.format(rec=len(df.index)))

    uc = UC()

    print('et script:')
    for index, row in df.iterrows():
    #for index in range(records):  
        #uc_dic = uc.get_dic_xml(xml_string)
        # pp.pprint(uc_dic)
        # reportId = flat_uc_df.at[0, uc.reportId]
        # print(flat_uc_df)
        score_id = int(row['ScoreId'])

        try:
            flat_uc_df = uc.get_df_xml(row['UCData'])
            ids_without_error.add(score_id)

            if index%100 == 0:
                print('.')


        except:
            new_errors += 1
            ids_with_error.add(score_id)
            #print('\n\terror at ScoreID: {id}'.format(id=score_id)) 
            pass
    
    update_file_id(ids_with_error_file, ids_with_error)
    update_file_id(ids_without_error_file, ids_without_error)

    
    print('new_errors:',new_errors)
    print('\nend!')

def update_file_id(filename, set_ids):
    list_id = list(set_ids)
    list_id.sort()
    with open(filename, 'w') as f:
        f.writelines("%s\n" % id for id in list_id)
        f.close()

main()