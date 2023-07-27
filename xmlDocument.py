import xml.etree.cElementTree as ET
import os

class XML(object):
    def inicializacion(self):
        is_file_created = os.path.exists("cm_models.xml")
           
        if(not(is_file_created)):
            root = ET.Element("cm_models")
            arbol = ET.ElementTree(root)
            arbol.write("cm_models.xml")

        self.tree = ET.parse("cm_models.xml")

    def add(self,vendor,model,softversion):
        self.xmlRoot = self.tree.getroot()
        doc = ET.SubElement(self.xmlRoot, "cm_model")
        ET.SubElement(doc, "vendor").text = vendor
        ET.SubElement(doc, "model").text = model
        ET.SubElement(doc, "softversion").text = softversion

        #self.xmlRoot.append(doc)
        self.tree.write("cm_models.xml")