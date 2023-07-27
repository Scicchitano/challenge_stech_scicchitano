import BBDD
import xmlDocument
import snmp_mock

snmp_mock_obj = snmp_mock.snmp_mock()

snmp_mock_obj.inicializacion()

snmp_mock_obj.run(OID="1.3.6.1.2.1.1.1.0")


BBDD_obj = BBDD.BBDD()

BBDD_obj.inicializacion()
try:
    BBDD_obj.createTable()
except:
    print("La tabla ya esta creada")

BBDD_obj.add(snmp_mock_obj.vendor, snmp_mock_obj.model, snmp_mock_obj.softversion)


XML_obj = xmlDocument.XML()

XML_obj.inicializacion()

XML_obj.add(snmp_mock_obj.vendor, snmp_mock_obj.model, snmp_mock_obj.softversion)

