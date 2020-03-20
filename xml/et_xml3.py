import xml.etree.ElementTree as ET
import pprint

filename = 'uc_xml_example4.xml'
filename = 'uc_xml_example5.xml'

tree = ET.parse('xmldata\\' + filename)
root = tree.getroot()

print('_'*100)
e = root
l = '{tag}-{att}-{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
print(l)

for c1 in root:
    e =  c1
    l = '{tag}-{att}-{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
    print(l)
    for c2 in c1:
        e =  c2
        l = '\t{tag}-{att}-{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
        print(l)
        for c3 in c2:
            e =  c3
            l = '\t{tag}-{att}-{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
            print(l)
            for c4 in c3:
                e =  c4
                l = '\t{tag}-{att}-{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
                print(l)

print('_'*100)
namespaces = {'owl': 'http://www.w3.org/2002/07/owl#'} # add more as needed
root.findall('owl:Class', namespaces)

namespaces = {'soapenv':'https://schemas.xmlsoap.org/soap/envelope/',
               'ns2':'https://www.uc.se.schemas/ucOrderReply/'}

# for x in root.iter('Body', namespaces):
#     print(x.attrib)
#     print(x.text)

# for term in root.findall('soapenv:Body', namespaces):
#     e =  term
#     l = '\t{tag}-{att}-{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
#     print(l)

# print('*'*100)
# for item in root.iter():
#     print('_'*10)
#     print(item)
#     for a in item.attrib:
#         l = '{att}-{text}'.format(att=a, text=item.attrib[a])
#         print(l)
#     print(item.text)

# for replay in root.iter('xmlReply'):
#     print('')
#     print(replay.text)

ucReplay = root[0][0]
status=ucReplay[0]
statusattrib = status.attrib
print(status)
print(statusattrib)

print('result with namespace:')
statusResult = status.attrib['{https://www.uc.se.schemas/ucOrderReply/}result']
print(statusResult)

xmlReply=ucReplay[1]

print('*'*100)
for item in xmlReply.iter():
    print('*'*100)
    print(item)
    for a in item.attrib:
        l = '{att}-{text}'.format(att=a, text=item.attrib[a])
        print(l)
    print(item.text)
