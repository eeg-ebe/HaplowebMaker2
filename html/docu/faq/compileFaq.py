#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import codecs

def toHtml(e):
    return ET.tostring(e)
#    minidom.parseString(ET.tostring(

root = ET.parse('faqs.xml').getroot()
with codecs.open("faq.html", "w", "UTF-8") as outF:
    outF.write("<!Doctype html>")
    outF.write("<html>")
    outF.write("<head>")
    outF.write("<meta charset=\"UTF-8\" />")
    outF.write("<title>FAQ</title>")
    outF.write("</head>")
    outF.write("<body>")
    for faq in root:
        outF.write("<a name=\"%s\"></a>" % faq.find('name').attrib['id'])
        outF.write("<h1>%s</h1>" % toHtml(faq.find('name')))
        for entry in faq.findall("entry"):
            outF.write("<a name=\"%s\"></a>" % entry.attrib['id'])
            outF.write("<h3>%s</h3>" % toHtml(entry.find("question")))
            outF.write("%s" % toHtml(entry.find("answer")))
    outF.write("</body>")
    outF.write("</html>")