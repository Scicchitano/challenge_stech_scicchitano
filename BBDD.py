#importaciones
import mysql.connector


class BBDD(object):
    def inicializacion(self):
        #conexion con el servidor
        self.conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Jphlions135",
            database = "cm_models_test"
        )

        #creación del cursor
        self.cursor = self.conexion.cursor()

    def createTable(self):
        self.cursor.execute("CREATE TABLE cm_models_test" 
        "(id INT NOT NULL AUTO_INCREMENT,"
        "vendor VARCHAR (64) NOT NULL,"
        "model VARCHAR (64) NOT NULL," 
        "softversion VARCHAR (64) NOT NULL,"
        "PRIMARY KEY (id));")

    def add(self,vendor,model,softversion):
        query = """INSERT INTO cm_models_test ( vendor, model, softversion) VALUES ('""" + vendor + """', '""" + model + """', '""" + softversion + """')"""
        print(query)
        self.cursor.execute(query)
        self.conexion.commit()
        print(self.cursor.rowcount, "Record inserted successfully into Laptop table")
        self.cursor.close()



