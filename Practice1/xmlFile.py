import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import product as p


file = 'allFiles/myXmlFile.xml'

stock = [ p.Product("Milk", 100, 58), p.Product("Juice", 77, 82), p.Product("Eggs", 261, 110), p.Product("Fish", 73, 118), p.Product("Bread", 112, 25) ]

data = ET.Element('stock')
for item in stock:
    product = ET.SubElement(data, 'product')
    name = ET.SubElement(product, 'name')
    name.text = item.name
    price = ET.SubElement(product, 'price')
    price.text = str(item.price)
    amount = ET.SubElement(product, 'amount')
    amount.text = str(item.amount)


xmlstr = minidom.parseString(ET.tostring(data)).toprettyxml(indent="   ")
with open(file, 'w') as file_handler:
    file_handler.write(xmlstr)


with open(file, 'r') as file_handler:
    xml = file_handler.read()
    print(xml)


answer = input("Do you want to delete the file? [y/n]: ")
if answer == 'y':
    if os.path.isfile(file):
        os.remove(file)
    else:
        print(f"Error: {file} file not found" )