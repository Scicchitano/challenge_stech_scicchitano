import BBDD
import xmlDocument
import snmp_mock
import sys

CANTIDAD_PUNTOS_IPV4 = 3

def checkIPV4(ip):
    return ip.count('.') == CANTIDAD_PUNTOS_IPV4

print("Lista de argumentos: " , sys.argv)

if not(checkIPV4(str(sys.argv[1]))):
    print("ERROR: BAD IP")
    exit(1)




"""Se ejecuta el mock para simular los parametros de vendor, model y softversion"""
snmp_mock_obj = snmp_mock.snmp_mock()

snmp_mock_obj.inicializacion()

snmp_mock_obj.run(OID=sys.argv[1])


if sys.argv[2] == 'db' or sys.argv[2] == 'both':
    """Se escribe en la BBDD los parametros obtenidos"""
    BBDD_obj = BBDD.BBDD()

    BBDD_obj.inicializacion()
    try:
        BBDD_obj.createTable()
    except:
        print("La tabla ya esta creada")

    if BBDD_obj.add(snmp_mock_obj.vendor, snmp_mock_obj.model, snmp_mock_obj.softversion):
        print("Se actualizo la BBDD")


if sys.argv[2] == 'file' or sys.argv[2] == 'both':
    """Se escribe en el archivo XML los parametros obtenidos"""
    XML_obj = xmlDocument.XML()

    XML_obj.inicializacion()

    XML_obj.add(snmp_mock_obj.vendor, snmp_mock_obj.model, snmp_mock_obj.softversion)
    print("Se actualizo el XML")

