#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import codecs

def toHtml(e):
    return ET.tostring(e)
#    minidom.parseString(ET.tostring(

root = ET.parse('faqs.xml').getroot()
with codecs.open("faq.html", "w", "UTF-8") as outF:
    outF.write("<!Doctype html>\n")
    outF.write("    <html>\n")
    outF.write("        <head>\n")
    outF.write("            <meta charset=\"UTF-8\" />\n")
    outF.write("            <title>FAQ</title>\n")
    outF.write("        </head>\n")
    outF.write("    <body>\n")
    for faqSectionNr, faq in enumerate(root):
        faqSectionNr += 1
        outF.write("    <a name=\"%s\"></a>\n" % faq.find('name').attrib['id'])
        outF.write("    <h1>%s</h1>\n" % toHtml(faq.find('name')))
        for nr, entry in enumerate(faq.findall("entry")):
            nr += 1
            outF.write("        <a name=\"%s\"></a>\n" % entry.attrib['id'])
            outF.write("        <h3>Q%s.%s: %s</h3>\n" % (faqSectionNr, nr, toHtml(entry.find("question"))))
            outF.write("        %s\n" % toHtml(entry.find("answer")))
    outF.write("    </body>\n")
    outF.write("</html>")
