#importaciones
import mysql.connector


class BBDD(object):
    def inicializacion(self):
        try:
            #Trato de crear la base de datos por si aun no esta creada
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Jphlions135",
            )
            self.cursor = self.conexion.cursor()
            self.cursor.execute("CREATE DATABASE cm_models")
        except:
            print("La DB ya esta creada")
        #Si la base de datos ya esta creada, me conecto a la misma
        self.conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Jphlions135",
            database = "cm_models"
        )

        self.cursor = self.conexion.cursor()

    def createTable(self):
        """Se crea la tabla"""
        self.cursor.execute("CREATE TABLE cm_models" 
        "(id INT NOT NULL AUTO_INCREMENT,"
        "vendor VARCHAR (64) NOT NULL,"
        "model VARCHAR (64) NOT NULL," 
        "softversion VARCHAR (64) NOT NULL,"
        "PRIMARY KEY (id));")

    def checkRepeticion(self,vendor,model,softversion):
        try:
            self.cursor.execute("SELECT vendor, model, softversion FROM cm_models.cm_models;")
            rows=self.cursor.fetchall()
            new_row = (str(vendor), str(model), str(softversion))
            for row in rows:
                if new_row == row:
                    print("BBDD REPETIDA")
                    return True
            
            return False
        except:
            return False

    def add(self,vendor,model,softversion):
        if self.checkRepeticion(vendor,model,softversion):
            return False
        """Se hace la query con los parametros recibidos"""
        query = """INSERT INTO cm_models ( vendor, model, softversion) VALUES ('""" + vendor + """', '""" + model + """', '""" + softversion + """')"""
        self.cursor.execute(query)
        self.conexion.commit()
        self.cursor.close()
        return True



