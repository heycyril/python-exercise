# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.yaml.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式
'''
<?xml version='1.0' encoding='utf-8'?>
<namelist>
    <name enrolled="yes">
        <age checked="no"/>
        <sex>33</sex>
    </name>
    <name enrolled="no">
        <age>19</age>
    </name>
</namelist>
'''