import xml.etree.cElementTree as ET
import os

class XML(object):
    def inicializacion(self):
        """Se checkea si el archivo xml ya esta creado"""
        is_file_created = os.path.exists("cm_models.xml")
        
        """Si el archivo no esta creado, se crea y se escribe la estructura"""
        if(not(is_file_created)):
            root = ET.Element("cm_models")
            arbol = ET.ElementTree(root)
            arbol.write("cm_models.xml")

        """Se inicializa el xml"""
        self.tree = ET.parse("cm_models.xml")

    def add(self,vendor,model,softversion):
        """Se agrega el set de parametros al xml"""
        self.xmlRoot = self.tree.getroot()
        doc = ET.SubElement(self.xmlRoot, "cm_model")
        ET.SubElement(doc, "vendor").text = vendor
        ET.SubElement(doc, "model").text = model
        ET.SubElement(doc, "softversion").text = softversion

        #self.xmlRoot.append(doc)
        self.tree.write("cm_models.xml")