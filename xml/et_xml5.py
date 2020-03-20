import pprint
from lxml import etree
import re
import pprint

pp = pprint.PrettyPrinter(indent=0)

filename = 'uc_xml_example4.xml'
filename = 'uc_xml_example5.xml'

tree = etree.parse('xmldata\\' + filename)
root = tree.getroot()

ucReplay = root[0][0]
status = ucReplay[0]
statusattrib = status.attrib
print('status:')
print(status)

print('statusattrib:')
print(statusattrib)

print('result with namespace:')
statusResult = status.attrib['{https://www.uc.se.schemas/ucOrderReply/}result']
print(statusResult)
for a in status.attrib:
    l = '{att}\n\t{text}'.format(att=a, text=status.attrib[a])
    print(l)

# statusResult = status.nsmap['result'] # doesn't work
# statusResult = status.nsmap['ns2:result'] # doesn't work
# statusResult = status.attrib['ns2:result'] # doesn't work
# statusResult = status.attrib['result'] # doesn't work


# print('result no namespace:')
# statusResult = ucReplay[1].nsmap['xmlReply'] #doesn't work

# print(statusResult)

ucReport=ucReplay[1]
print(ucReport)

# xmlReplay = ucReport.attrib['xmlReply'] # doesn't work
# xmlReplay = ucReport.nsmap['xmlReply'] # doesn't work
print('lopp:'+'_'*100) #         'xmlReply'
for xmlReply in ucReport.findall('xmlReply'): # doesn't work
    print(xmlReply)

xmlReplays = []
regex_namespace = r'({.*}).*'
regex_att = r'{.*}(.*)'

for xmlReply in ucReport.findall('xmlReply', ucReport.nsmap):
    report = xmlReply[0][0]
    namespace = re.search(regex_namespace, xmlReply.tag)[1]
    report_dic = {}
    report_dic['id'] = report.attrib[namespace+'id']
    report_dic['index'] = report.attrib[namespace+'index']
    report_dic['name'] = report.attrib[namespace+'name']
    report_dic['styp'] = report.attrib[namespace+'styp']

    #print(report_dic)
    #<ns2:group ns2:id="W080" ns2:index="0" ns2:key="" ns2:name="IDuppgifter, fysiker">
    #find tags programaticall
    report_dic_2 = {}
    for a in report.attrib:
        att = re.search(regex_att, a)[1]
        data = report.attrib[a]
        report_dic_2[att] = data
    #print(report_dic_2)

    groups = []
    for group in report:
        group_dic = {}
        for a in group.attrib:
            att = re.search(regex_att, a)[1]
            data = group.attrib[a]
            group_dic[att] = data

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
        #pp.pprint(group_dic)

    xmlReplays.append(report_dic)


#pp.pprint(xmlReplays)

print(ucReplay)

for child in ucReplay:
    print(child)



print('ucReplay.nsmap')
pp.pprint(ucReplay.nsmap)

print('status:')
for x in ucReplay.findall('status', ucReplay.nsmap):
    print(x)
    print(x.attrib)
    # try to get result attribut
    result = x.get('result', 'DEFAULT VALUE')
    line = '{s}result:<{r}>'.format(s='*'*10,r=result)
    print(line)

    
print('ucReport:')
for x in ucReplay.findall('ucReport', ucReplay.nsmap): # doesn't work
    print(x)
    print(x.attrib)

print('body')
for x in root.findall('soapenv:Body', root.nsmap): # doesn't work
    print('x_________')
    print(x)