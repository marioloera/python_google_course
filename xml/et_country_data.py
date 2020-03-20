import xml.etree.ElementTree as ET
import pprint

f = 'country_data.xml'
tree = ET.parse(f)
root = tree.getroot()
#root = ET.fromstring(country_data_as_string)
print(root)
# print(root.attrib['id'])
# print(root.attrib['index'])
print('_'*100)
e = root
l = '{tag}:{att}:{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
print(l)

for c1 in root:
    e =  c1
    l = '{tag}:{att}:{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
    print(l)
    l = '{tag}:{text}'.format(tag=e.tag, text=e.attrib['name'])
    print(l)

    for c2 in c1:
        e =  c2
        l = '\t{tag}:{att}:{text}'.format(tag=e.tag, att=e.attrib, text=e.text)
        print(l)
        if e.tag != 'neighbor':
            continue
        for a in e.attrib:
            l = '\t\t{att}:{text}'.format(att=a, text=e.attrib[a])
            print(l)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name') # name is an attribute, so use function get
    name2 = country.attrib['name']
    print(name, name2, rank)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
    gdppc = int(country.find('gdppc').text)
    if gdppc > 100000:
        print(country.get('name'))

for gdppc in root.iter('gdppc'):
    print(gdppc.text)



print('_'*13)
for gdppc in root.findall('gdppc'):
    print(gdppc.text)

for country in root.findall('country'):
    print(country)

y = root.find('country').find('year').text
print(y)