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

    
    def checkRepetido(self,vendor,model,softversion):
        self.new_element = [vendor,model,softversion]
        """Se agrega el set de parametros al xml"""
        self.xmlRoot = self.tree.getroot()
        for page in self.xmlRoot:
            i=0
            element = ["","",""]
            for elem in page:
                element[i] = elem.text
                i = i + 1
                if i==3:
                    #print(element)
                    #print("----------------------------------------------------------------------------")
                    i=0
                    if element == self.new_element:
                        print("XML REPETIDO")
                        return True
        return False

    def add(self,vendor,model,softversion):

        if self.checkRepetido(vendor,model,softversion):
            return False

        doc = ET.SubElement(self.xmlRoot, "cm_model")
        ET.SubElement(doc, "vendor").text = vendor
        ET.SubElement(doc, "model").text = model
        ET.SubElement(doc, "softversion").text = softversion

        #self.xmlRoot.append(doc)
        self.tree.write("cm_models.xml")
        print("Se actualizo el XML")
        return True