import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')

root = tree.getroot()

for unit in root.iter('unit'):

    print(unit.attrib)