import pprint
from lxml import etree
import re

pp = pprint.PrettyPrinter(indent=0)

filename = 'uc_xml_example6.xml'

tree = etree.parse(filename)
root = tree.getroot()

ucReplay = root[0][0]
status = ucReplay[0]
ucReport=ucReplay[1]
statusResult = status.attrib['{https://www.uc.se.schemas/ucOrderReply/}result']
print('statusResult:' + statusResult)

xmlReplays = []
regex_namespace = r'({.*}).*'
regex_att = r'{.*}(.*)'
namespace = re.search(regex_namespace, ucReport.tag)[1]

for xmlReply in ucReport.findall('xmlReply', ucReport.nsmap):
    report = xmlReply[0][0]
    report_dic = {}

    for a in report.attrib:
        att = re.search(regex_att, a)[1]
        data = report.attrib[a]
        report_dic[att] = data

    groups = []
    for group in report:
        group_dic = {}
        for a in group.attrib:
            att = re.search(regex_att, a)[1]
            data = group.attrib[a]
            group_dic[att] = data
        print(group_dic)
        terms = []
        for term in group:
            term_dic = {}
            for a in term.attrib:
                att = re.search(regex_att, a)[1]
                data = term.attrib[a]
                term_dic[att] = data
            term_dic['text'] = term.text
            terms.append(term_dic)
        group_dic['terms'] = terms 
        groups.append(group_dic)
    report_dic['groups'] = groups   

    xmlReplays.append(report_dic)

pp.pprint(xmlReplays)

# for replay in xmlReplays:
#     for group in replay['groups']:
#         pp.pprint(group)