#!/usr/bin/env python3
import unittest
from extract_uc_data import UCData as UC

def get_xml():
    xml_string = '<?xml version="1.1" encoding="UTF-8" ?>\
        <soapenv:Envelope xmlns:soapenv="https://schemas.xmlsoap.org/soap/envelope/" \
            xmlns:soapenc="https://schemas.xmlsoap.org/soap/encoding/" \
            xmlns:xsd="https://www.w3.org/2001/XMLSchema" \
            xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance">\
            <soapenv:Body>\
                <ucReply xmlns="https://www.uc.se.schemas/ucOrderReply/">\
                    <ns2:status ns2:result="ok" \
                        xmlns:ns2="https://www.uc.se.schemas/ucOrderReply/" />\
                    <ucReport>\
                        <xmlReply>\
                            <ns2:reports ns2:lang="swe" \
                                xmlns:ns2="https://www.uc.se.schemas/ucOrderReply/">\
                                <ns2:report ns2:id="4801093750" ns2:index="0" ns2:name="Peter Peltonen" ns2:styp="3">\
                                    <ns2:group ns2:id="W080" ns2:index="0" ns2:key="" ns2:name="IDuppgifter, fysiker">\
                                        <ns2:term ns2:id="W08001">9480109375</ns2:term>\
                                        <ns2:term ns2:id="W08006">Tygelsjö</ns2:term>\
                                        <ns2:term ns2:id="W08007">5905104948</ns2:term>\
                                        <ns2:term ns2:id="W08027" />\
                                        <ns2:term ns2:id="W08030">2</ns2:term>\
                                        <ns2:term ns2:id="W08043">Gift sedan 1995-08 med Helga Peltonen (590510-4948)</ns2:term>\
                                        <ns2:term ns2:id="W08031">199508</ns2:term>\
                                        <ns2:term ns2:id="W08035">Peltonen, Peter Ernst </ns2:term>\
                                    </ns2:group>\
                                    </ns2:report>\
                            </ns2:reports>\
                        </xmlReply>\
                    </ucReport>\
                </ucReply>\
            </soapenv:Body>\
        </soapenv:Envelope>'
    return xml_string

class UCDataTest(unittest.TestCase):
    
    def test_empty_string(self):
        uc = UC()
        df, status = uc.get_dataframe('', 1, 'a')
        self.assertEqual((df, status), (None, uc.resultEmptyString))
    
    def test_null(self):
        uc = UC()
        df, status = uc.get_dataframe(None, 1, 'a')
        self.assertEqual((df, status), (None, uc.resultNull))

    def test_replay_status(self):
        uc = UC()
        _, status = uc.get_dataframe(get_xml(), 1, 'a')
        self.assertEqual(status, uc.resultOk)

    def test_score_and_user(self):
        uc = UC()
        expected = [219328372, '13ldkf0239']
        df, _ = uc.get_dataframe(get_xml(), expected[0], expected[1])    
        for _, row in df.iterrows():
            result = []
            result.append(int(row[uc.scoreId]))
            result.append(row[uc.lendifyUserId])
            self.assertEqual(result, expected)

    def test_report_data(self):
        uc = UC()
        expected = ['4801093750','0','Peter Peltonen','3']
        # <ns2:report ns2:id="4801093750" ns2:index="0" ns2:name="Peter Peltonen" ns2:styp="3">\
        df, _ = uc.get_dataframe(get_xml(), 1, 'a')    
        for _, row in df.iterrows():
            result = []
            result.append(row[uc.reportId])
            result.append(row[uc.reportIndex])
            result.append(row[uc.reportName])
            result.append(row[uc.reportStyp])
            self.assertEqual(result, expected)

    def test_group_data(self):
        uc = UC()
        expected = ['W080', '0', '', 'IDuppgifter, fysiker']
        # <ns2:group ns2:id="W080" ns2:index="0" ns2:key="" ns2:name="IDuppgifter, fysiker">\
        df, _ = uc.get_dataframe(get_xml(), 1, 'a') 
        for _, row in df.iterrows():
            result = []
            result.append(row[uc.groupId])
            result.append(row[uc.groupIndex])
            result.append(row[uc.groupKey])
            result.append(row[uc.groupName])
            self.assertEqual(result, expected)

    def test_term_data(self):
        uc = UC()        
        expected = {'W08006': 'Tygelsjö',
                    'W08007': '5905104948',
                    'W08043': 'Gift sedan 1995-08 med Helga Peltonen (590510-4948)',
                    'W08027': None,
                    'W08031': '199508',
                    }       
        # <ns2:term ns2:id="W08006">Tygelsjö</ns2:term>
        # <ns2:term ns2:id="W08007">5905104948</ns2:term>
        # <ns2:term ns2:id="W08027" />
        # <ns2:term ns2:id="W08030">2</ns2:term>
        # <ns2:term ns2:id="W08043">Gift sedan 1995-08 med Helga Peltonen (590510-4948)</ns2:term>
        # <ns2:term ns2:id="W08031">199508</ns2:term>
        df, _ = uc.get_dataframe(get_xml(), 1, 'a')
        result = {}
        for _, row in df.iterrows():
            termId = row[uc.termId]
            if termId not in expected.keys():
                continue
            result[termId] = row[uc.termData]
        self.assertEqual(result, expected)

    def test_file(self):
        filename = 'xmldata/uc_xml_example1.xml'
        uc = UC()
        df, _ = uc.get_df_from_file(filename, 1, 'a')
        expected = {
                    'group_count': 39,
                    'W450-2-W45024': '9473',
                    'W450-4-W45024': '9604',
                    'W46B-0-key':'196409071492',
                    }
        result = {}
        groups = {}
        for _, row in df.iterrows():
            groupId = row[uc.groupId]
            groupIndex = row[uc.groupIndex]
            groupKey = row[uc.groupKey]
            termId = row[uc.termId]
            termData = row[uc.termData]
            gId_gIndex = '-'.join([groupId, groupIndex])
            if gId_gIndex not in groups.keys():
                groups[gId_gIndex] = 1

            if groupId == 'W450' and termId == 'W45024':
                if groupIndex == '2' or groupIndex == '4':
                   result['-'.join([groupId , groupIndex, termId])] = termData
            
            elif groupId == 'W46B' and groupIndex == '0':
                result['-'.join([groupId , groupIndex, 'key'])] = groupKey


        result['group_count'] = len(groups)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
