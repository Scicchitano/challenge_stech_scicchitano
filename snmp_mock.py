class snmp_mock(object):
    def inicializacion(self):
        self.vendor = ""
        self.model = ""
        self.softversion = ""
    def run(self,OID):
        answer = "iso.3.6.1.2.1.1.1.0 = STRING: 'Cisco DPC2325 DOCSIS 2.0 2-PORT Gateway <<HW_REV: 1.0; VENDOR: Cisco - " + OID[0] + "; BOOTR: 2.1.7lR3; SW_REV: dpc2325-v202r12811-110715as - " + OID[2] +"; MODEL: DPC2325 - " + OID[4] + ">>'"
        print(answer)

        vendorIndex_start = answer.index("VENDOR:")
        vendorIndex_end = answer.index("; BOOTR")
        self.vendor = answer[vendorIndex_start+8:vendorIndex_end]

        softversionIndex_start = answer.index("SW_REV:")
        softversionIndex_end = answer.index("; MODEL")
        self.softversion = answer[softversionIndex_start+8:softversionIndex_end]

        modelIndex_start = answer.index("MODEL:")
        modelIndex_end = answer.index(">>")
        self.model = answer[modelIndex_start+7:modelIndex_end]

        print("VENDOR: " + self.vendor)
        print("SW_REV: " + self.softversion)
        print("MODEL: " + self.model)
        return 