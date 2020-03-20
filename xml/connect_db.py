import  pyodbc
import pandas as pd

def az_connect_read(username,password,server,database,driver,appintent,auth):
    engn = pyodbc.connect(
                r'DRIVER={'+driver+'};'
                r'SERVER='+server+';'
                r'DATABASE='+database+';'
                r'UID='+username+';'
                r'PWD='+password+';'
                r'ApplicationIntent='+appintent+';'
                r'Authentication='+auth+''
                )
    return engn 

def az_get_data0(query,engn):
    dfsql = pd.read_sql(query, engn)
    return dfsql

class ConnAZ():
    def __init__(self):
        self.username = 'malo@lendify.se'
        self.password = 'PAwin01123*1'
        self.server = 'po4ncqs1n2.database.windows.net'
        self.database = 'Export'
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.appintent = 'ReadOnly'
        self.auth = 'ActiveDirectoryPassword'
        pass



# environ['AZURESQL_SERVER'] = 'po4ncqs1n2.database.windows.net'
# environ['DATABASE'] ='Export'
# environ['DRIVER'] ='ODBC Driver 17 for SQL Server'
# environ['APPINTENT'] ='ReadOnly'

def main():
    connAZ = ConnAZ()
    engn = az_connect_read(connAZ.username,
                            connAZ.password,
                            connAZ.server,
                            connAZ.database,
                            connAZ.driver,
                            connAZ.appintent,
                            connAZ.auth)

    query = 'SELECT TOP (10) ScoreId,UCData FROM dbo.UserCreditScores ORDER BY ScoreId DESC;'
    df = az_get_data0(query,engn)
    
    print(df)

main()