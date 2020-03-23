import pprint
import xml.etree.ElementTree as ET
import re

pp = pprint.PrettyPrinter(indent=0)

filenames =['uc_xml_example1.xml',
            'uc_xml_example1.2.xml',
            'uc_xml_example2.xml',
            'uc_xml_example4.xml',
            'uc_xml_example5.xml',
            'UserCreditScores_UCData.xml',
            'uc_xml_example6.xml',
            'uc_xml_example7.xml']


def get_ucReport(filename):
    tree = ET.parse('xmldata\\' + filename)
    root = tree.getroot()

    # some xml have different namespaces and differences along the three
    for child in root:

        if 'Body' in child.tag:
            body = child

    for child in body:

        if 'ucReply' in child.tag:
            ucReplay = child

    for child in ucReplay:

        if 'ucReport' in child.tag:
            ucReport = child

        if 'status' in child.tag:
            for att in child.attrib:
                if 'result' in att:
                    ucReplayStatus = child.attrib[att]
        
    return ucReport, ucReplayStatus


def get_xmlReplays(ucReport):
    regex_namespace = r'({.*}).*'
    attrib_regex = r'{.*}(.*)'
    namespace = re.search(regex_namespace, ucReport.tag)[1]
    xmlReplays = []
    for xmlReply in ucReport.findall(namespace+'xmlReply'):
        report = xmlReply[0][0]
        
        report_dic = {}
        report_dic['id'] = report.attrib[namespace+'id']
        report_dic['index'] = report.attrib[namespace+'index']
        report_dic['name'] = report.attrib[namespace+'name']
        report_dic['styp'] = report.attrib[namespace+'styp']

        print(report_dic)
        for group in report:
            
            group_dic = {}
            term_dic = {}
            
            for a in group.attrib:
                att = re.search(attrib_regex, a)[1]
                data = group.attrib[a]
                group_dic[att] = data

            for term in group:
                term_id = term.attrib[namespace+'id']
                term_dic[term_id] = term.text

            group_id = group_dic['id']
            group_index = group_dic['index']

            if group_id not in report_dic.keys():
                report_dic[group_id] = {}
            
            if group_index not in report_dic[group_id].keys():
                report_dic[group_id][group_index] = {}

            report_dic[group_id][group_index] = term_dic

        xmlReplays.append(report_dic)
    return xmlReplays


def get_xmlReplays2(ucReport):
    # used for report, group and term with name spaces
    attrib_regex = r'{.*}(.*)' 
    xmlReplays = []

    for xmlReply in ucReport:
        if 'xmlReply' not in xmlReply.tag:
            continue

        for reports in xmlReply:
            if 'reports' not in reports.tag:
                continue

        for report in reports:
            if 'report' not in report.tag:
                continue
        
        report_dic = {}
        for name in report.attrib:
            value = report.attrib[name]
            att = name
            # in case the att don't have namespace
            result = re.findall(attrib_regex, name)
            if result != []:
                att = result[0]
            report_dic[att] = value

        for group in report:
            if 'group' not in group.tag:
                continue
            group_dic = {}
            term_dic = {}
            
            for name in group.attrib:
                value = group.attrib[name]
                att = name
                # in case the att don't have namespace
                result = re.findall(attrib_regex, name)
                if result != []:
                    att = result[0]
                group_dic[att] = value

            for term in group:
                if 'term' not in term.tag:
                    continue

                for name in term.attrib:
                    value = term.attrib[name]
                    if 'id' in name:
                        term_dic[value] = term.text

            group_id = group_dic['id']
            group_index = group_dic['index']

            if group_id not in report_dic.keys():
                report_dic[group_id] = {}
            
            if group_index not in report_dic[group_id].keys():
                report_dic[group_id][group_index] = {}

            report_dic[group_id][group_index] = term_dic

        xmlReplays.append(report_dic)
    return xmlReplays


for filename in filenames[0:]:
    ucReport, ucReplayStatus = get_ucReport(filename)
    
    if ucReplayStatus:
        xmlReplays = get_xmlReplays2(ucReport)
        pp.pprint(xmlReplays)

   
