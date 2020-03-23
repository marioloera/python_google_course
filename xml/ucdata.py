import xml.etree.ElementTree as ET
import pandas as pd
import re
import copy

class UCData:

    def __init__(self):
        # self.lendifyUserId = 'LendifyUserId' # 0
        # self.scoreId = 'ScoreId' # 1
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
        self.__init_data_dic()
    
    def __init_headers__(self):
        self.headers = [
                    # self.lendifyUserId, # 0 
                    # self.scoreId, # 1
                    self.reportId, # 2 
                    self.reportIndex, # 3
                    self.reportName, # 4 
                    self.reportStyp, # 5
                    self.groupId, # 6
                    self.groupIndex, # 7
                    self.groupKey, # 8
                    self.groupName, # 9
                    self.termId, # 10 
                    self.termData,
                    ] # 11
        return

    def __init_data_dic(self):
        self.__init_headers__()
        dic = {}
        for i, header in enumerate(self.headers):
            if header in dic.keys():
                error = 'DUPLICATE HEADER ({h}): IN dic at poss({p})'.format(
                        h=header, p=i)
                raise ValueError(error)
            dic[header] = []
        self.template_dic = dic
        return

    def __get_ucReport__(self, root):
        for child in root:
            if 'Body' in child.tag:
                body = child

        for child in body:
            if 'ucReply' in child.tag:
                ucReplay = child

        for child in ucReplay:
            if 'ucReport' in child.tag:
                ucReport = child
            elif 'status' in child.tag:
                for att in child.attrib:
                    if 'result' in att:
                        ucReplayStatus = child.attrib[att]
            
        return ucReport, ucReplayStatus

    def get_dic_xml(self, xml_string):
        root = ET.fromstring(xml_string)
        ucReport, ucReplayStatus = self.__get_ucReport__(root)
        xmlReplays = self.__get_xmlReplays__(ucReport)
        return xmlReplays

    def get_df_xml(self, xml_string):
        root = ET.fromstring(xml_string)
        ucReport, ucReplayStatus = self.__get_ucReport__(root)

        data_dic = self.__get_df_xmlReplays__(ucReport)
        #rows = str(len(data_dic[self.termId]))
        #print('rows in data_dic:' + rows)
        df = pd.DataFrame(data_dic)
        return df

    def __get_xmlReplays__(self, ucReport):
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

    def __get_df_xmlReplays__(self, ucReport):
        # used for report, group and term with name spaces
        attrib_regex = r'{.*}(.*)' 
        df_dic = copy.deepcopy(self.template_dic)

        #df_dic = self.__init_data_dic()      
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
                        term_id = None
                        term_text = None
                        if 'id' in name:
                            term_dic[value] = term.text
                            term_id = value
                            term_text = term.text


                    # df_dic[self.lendifyUserId].append(dbdfLendifyUserId) # 0
                    # df_dic[self.scoreId].append(dbScoreID) # 1

                    df_dic[self.reportId].append(report_dic['id']) # 2
                    df_dic[self.reportIndex].append(report_dic['index']) # 3
                    df_dic[self.reportName].append(report_dic['name']) # 4
                    df_dic[self.reportStyp].append(report_dic['styp']) # 5
                    df_dic[self.groupId].append(group_dic['id']) # 6
                    df_dic[self.groupIndex].append(group_dic['index']) # 7
                    df_dic[self.groupName].append(group_dic['name']) # 8
                    df_dic[self.groupKey].append(group_dic['key']) # 9
                    df_dic[self.termId].append(term_id) # 10
                    df_dic[self.termData].append(term_text) # 11

                group_id = group_dic['id']
                group_index = group_dic['index']

                if group_id not in report_dic.keys():
                    report_dic[group_id] = {}
                
                if group_index not in report_dic[group_id].keys():
                    report_dic[group_id][group_index] = {}

                report_dic[group_id][group_index] = term_dic

        return df_dic
   




