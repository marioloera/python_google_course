import pprint
import pandas as pd
import xml.etree.ElementTree as ET
import re

pp = pprint.PrettyPrinter(indent=0)

filename = 'xmldata\\uc_xml_example1.xml'
tree = ET.parse(filename)
root = tree.getroot()

ucReplay = root[0][0]
status = ucReplay[0]
ucReport=ucReplay[1]
# statusResult = status.attrib['{https://www.uc.se.schemas/ucOrderReply/}result']
# print('statusResult:')
# print(statusResult)


xmlReplays = []
regex_namespace = r'({.*}).*'
regex_att = r'{.*}(.*)'
namespace = re.search(regex_namespace, ucReport.tag)[1]

class DataFrameHeaders:
    pass
#for xmlReply in ucReport.findall('xmlReply', ucReport.nsmap):
dfLendifyUserId = 'LendifyUserId'
dfScoreId = 'ScoreId'
dfReportId = 'ReportId'
dfReportIndex = 'ReportIndex'
dfReportName = 'ReportName'
dfReportStyp = 'ReportStyp'
dfGroupId = 'GroupId'
dfGroupIndex = 'GroupIndex'
dfGroupKey = 'GroupKey'
dfGroupName = 'GroupName'
dfTermId = 'TermId'
dfTermData = 'TermData'

headers = {}
headers[0] = dfLendifyUserId
headers[1] = dfScoreId
headers[2] = dfReportId
headers[3] = dfReportIndex
headers[4] = dfReportName
headers[5] = dfReportStyp
headers[6] = dfGroupId
headers[7] = dfGroupIndex
headers[8] = dfGroupKey
headers[9] = dfGroupName
headers[10] = dfTermId
headers[11] = dfTermData

data_dic = {}
dbdfLendifyUserId = 'axf392de323'
dbScoreID = 23988329

for header in headers.values():
    if header in data_dic.keys():
        error = 'DUPLICATE HEADER ({h}): IN data dict'.format(h=header)
        raise ValueError(error)
    data_dic[header] = []

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

            data_dic[dfLendifyUserId].append(dbdfLendifyUserId) # 0
            data_dic[dfScoreId].append(dbScoreID) # 1

            data_dic[dfReportId].append(report_dic['id']) # 2
            data_dic[dfReportIndex].append(report_dic['index']) # 3
            data_dic[dfReportName].append(report_dic['name']) # 4
            data_dic[dfReportStyp].append(report_dic['styp']) # 5

            data_dic[dfGroupId].append(group_dic['id']) # 6
            data_dic[dfGroupIndex].append(group_dic['index']) # 7
            data_dic[dfGroupName].append(group_dic['name']) # 8
            data_dic[dfGroupKey].append(group_dic['key']) # 9

            data_dic[dfTermId].append(term_id) # 10
            data_dic[dfTermData].append(term_dic[term_id]) # 11

        g_id = group_dic['id']
        g_index = group_dic['index']

        if g_id not in report_dic.keys():
            report_dic[g_id] = {}

        if g_index not in report_dic[g_id].keys():
            report_dic[g_id][g_index] = {}

        report_dic[g_id][g_index] = term_dic

    xmlReplays.append(report_dic)



#pp.pprint(xmlReplays)

rows = None
for key, value in data_dic.items():
    if rows == None:
        continue
    if rows != len(value):
        print('error in rows')
    rows = len(value)


df = pd.DataFrame(data_dic)
print(df)
# commond data
print('report data')
print(df.iloc[0:1,0:6])
print('group and term data')
print(df.iloc[:,6:])