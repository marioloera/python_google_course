import xml.etree.ElementTree as ET
import pprint
pp = pprint.PrettyPrinter(indent=0)

# Download the xml file
#!wget https://raw.githubusercontent.com/Jokezor/Lendify_test/master/xmldoc2parse.xml -P .
filename = 'uc_xml_example.xml' #other formats
filename = 'UserCreditScores_UCData.xml' #other formats
filename = 'UserLoans_XMLData.xml'

# tree = ET.parse('xmldoc2parse.xml')
tree = ET.parse('xmldata\\' + filename)

root = tree.getroot()
# Build up dictionary to hold the data
Data_dict = {}
Data_dict[root.attrib['UserId']] = {}
Data_dict[root.attrib['UserId']][root.attrib['LoanId']] = {}
for child in root:
    Data_dict[root.attrib['UserId']][root.attrib['LoanId']][child.tag] = {}
    for key_1 in child.attrib:
        Data_dict[root.attrib['UserId']][root.attrib['LoanId']][child.tag][key_1] = child.attrib[key_1]
    Data_dict[root.attrib['UserId']][root.attrib['LoanId']][child.tag]['Results'] = {}
    for Result in root.iter('Result'):
        for key_2 in Result.attrib:
            if key_2 == 'Id':
                if key_2 not in Data_dict[root.attrib['UserId']][root.attrib['LoanId']][child.tag]['Results']:
                    Data_dict[root.attrib['UserId']][root.attrib['LoanId']][child.tag]['Results'][Result.attrib['Id']] = {}
                else:
                    pass
            else:
                Data_dict[root.attrib['UserId']][root.attrib['LoanId']][child.tag]['Results'][Result.attrib['Id']][key_2] = Result.attrib[key_2]
# As we now can see the data is now structured in the dict and ready for processing or storage.
# Hierarchy: {UserId: {LoanId: {Rating: {Results: Result_1: {}, Result_2: {} ... Result_N: {} } } } }
# The Hierarchy of UserId and LoanId is to allow a user to have several LoanIds.

pp.pprint(Data_dict)