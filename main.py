import xml.etree.ElementTree as ET
mytree = ET.parse('model.sdf')
myroot = mytree.getroot()

print(myroot)
walls =[]
for x in myroot[0]:
     print(x.tag, x.attrib)
     geometry = x.getElementsByTagName("geometry")
     print(geometry)
     if "Wall" in x.attrib:
         walls.append((x.attrib,""))

for x in myroot.findall('link'):
    if "Wall" in x.attrib:
        item =x.find('geometry').text
        print(item)
        #price = x.find('price').text
        print(item)
