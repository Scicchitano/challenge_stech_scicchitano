#importaciones
import mysql.connector


class BBDD(object):
    def inicializacion(self):
        #conexion al servidor
        self.conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Jphlions135",
            database = "cm_models_test"
        )

        self.cursor = self.conexion.cursor()

    def createTable(self):
        """Se crea la tabla"""
        self.cursor.execute("CREATE TABLE cm_models_test" 
        "(id INT NOT NULL AUTO_INCREMENT,"
        "vendor VARCHAR (64) NOT NULL,"
        "model VARCHAR (64) NOT NULL," 
        "softversion VARCHAR (64) NOT NULL,"
        "PRIMARY KEY (id));")

    def checkRepeticion(self,vendor,model,softversion):
        query = self.cursor.execute("SELECT vendor, model, softversion FROM cm_models_test.cm_models_test;")
        rows=self.cursor.fetchall()
        new_row = (str(vendor), str(model), str(softversion))
        for row in rows:
            if new_row == row:
                print("La IP ya fue ingresada")
                return True
        
        return False

    def add(self,vendor,model,softversion):
        if self.checkRepeticion(vendor,model,softversion):
            return False
        """Se hace la query con los parametros recibidos"""
        query = """INSERT INTO cm_models_test ( vendor, model, softversion) VALUES ('""" + vendor + """', '""" + model + """', '""" + softversion + """')"""
        self.cursor.execute(query)
        self.conexion.commit()
        self.cursor.close()
        return True



