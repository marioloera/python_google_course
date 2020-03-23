import pprint
import xml.etree.ElementTree as ET
import re

pp = pprint.PrettyPrinter(indent=0)

filename = 'xmldata\\uc_xml_example1.xml'
#root = ET.fromstring(country_data_as_string)

def get_uc_data(xml_string):
    dt = None # dataframe
    return dt
    
tree = ET.parse(filename)
root = tree.getroot()

ucReplay = root[0][0]
status = ucReplay[0]
ucReport=ucReplay[1]
# statusResult = status.attrib['{https://www.uc.se.schemas/ucOrderReply/}result']
# print('statusResult:')
# print(statusResult)



class UCDataHeaders:

    def __init__(self):
        self.lendifyUserId = 'LendifyUserId' # 0
        self.scoreId = 'ScoreId' # 1
        self.reportId = 'ReportId' # 2
        self.reportIndex = 'ReportIndex' # 3
        self.reportName = 'ReportName' # 4
        self.reportStyp = 'ReportStyp' # 5
        self.groupId = 'GroupId' # 6
        self.groupIndex = 'GroupIndex' # 7
        self.groupKey = 'GroupKey' # 8
        self.groupName = 'GroupName' # 9
        self.termId = 'TermId' # 10 
        self.termData = 'TermData' # 11
        self.dic = self.__get_data_dic()
        
    
    def __fill_headers__(self):
        self.headers = [self.lendifyUserId, # 0 
                    self.scoreId, # 1
                    self.reportId, # 2 
                    self.reportIndex, # 3
                    self.reportName, # 4 
                    self.reportStyp, # 5
                    self.groupId, # 6
                    self.groupIndex, # 7
                    self.groupKey, # 8
                    self.groupName, # 9
                    self.termId, # 10 
                    self.termData] # 11
        return


    def __get_data_dic(self):
        self.__fill_headers__()
        dic = {}
        for i, header in enumerate(self.headers):
            if header in dic.keys():
                error = 'DUPLICATE HEADER ({h}): IN dic at poss({p})'.format(
                        h=header, p=i)
                raise ValueError(error)
            dic[header] = []
        return dic


uc = UCDataHeaders()
dbdfLendifyUserId = 'axf392de323'
dbScoreID = 23988329

xmlReplays = []
regex_namespace = r'({.*}).*'
regex_att = r'{.*}(.*)'
namespace = re.search(regex_namespace, ucReport.tag)[1]


for xmlReply in ucReport.findall(namespace+'xmlReply'):
    report = xmlReply[0][0]

    report_dic = {}
    report_dic['id'] = report.attrib[namespace+'id']
    report_dic['index'] = report.attrib[namespace+'index']
    report_dic['name'] = report.attrib[namespace+'name']
    report_dic['styp'] = report.attrib[namespace+'styp']

    for group in report:

        group_dic = {}
        group_dic['id'] = group.attrib[namespace+'id']
        group_dic['index'] = group.attrib[namespace+'index']
        group_dic['name'] = group.attrib[namespace+'name']
        group_dic['key'] = group.attrib[namespace+'key']

        term_dic = {}
        for term in group:
            term_id = term.attrib[namespace+'id']
            term_dic[term_id] = term.text

            uc.dic[uc.lendifyUserId].append(dbdfLendifyUserId) # 0
            uc.dic[uc.scoreId].append(dbScoreID) # 1
            uc.dic[uc.reportId].append(report_dic['id']) # 2
            uc.dic[uc.reportIndex].append(report_dic['index']) # 3
            uc.dic[uc.reportName].append(report_dic['name']) # 4
            uc.dic[uc.reportStyp].append(report_dic['styp']) # 5
            uc.dic[uc.groupId].append(group_dic['id']) # 6
            uc.dic[uc.groupIndex].append(group_dic['index']) # 7
            uc.dic[uc.groupName].append(group_dic['name']) # 8
            uc.dic[uc.groupKey].append(group_dic['key']) # 9
            uc.dic[uc.termId].append(term_id) # 10
            uc.dic[uc.termData].append(term_dic[term_id]) # 11

        g_id = group_dic['id']
        g_index = group_dic['index']

        if g_id not in report_dic.keys():
            report_dic[g_id] = {}

        if g_index not in report_dic[g_id].keys():
            report_dic[g_id][g_index] = {}

        report_dic[g_id][g_index] = term_dic

    xmlReplays.append(report_dic)



#pp.pprint(xmlReplays)
# check number of rows
rows = None
for key, value in uc.dic.items():
    if rows == None:
        continue
    if rows != len(value):
        print('error in rows')
    rows = len(value)


import pandas as pd


df = pd.DataFrame(uc.dic)
print(df)
# commond data
print('report data')
print(df.iloc[0:1,0:6])
print('group and term data')
print(df.iloc[:,6:])

