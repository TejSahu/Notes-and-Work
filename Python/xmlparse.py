import xml.etree.ElementTree as ET

file = ET.parse("Baseline FKM.xml")
root = file.getroot()

print(root)
print(root.tag)
print(root.attrib['name'])
# print(root.value)

for child in root.iter('ignoreKey'):
    for subchild in child.iter('data'):
        print(root.attrib['name'], child.tag, subchild.text)
