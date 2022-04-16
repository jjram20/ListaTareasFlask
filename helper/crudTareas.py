import mysql.connector

class database():
    def __init__(self):
        self.conexion = mysql.connector.connect(host="127.0.0.1", user="jesus", password="password123", database="FastTaskBasico")
        self.cursor = self.conexion.cursor()
    def agregarTarea(self, tarea):
        self.cursor.execute("INSERT INTO Tareas (Tarea) VALUES ('{}');".format(tarea))
        self.conexion.commit()
        print("Registro guardado")
    def leerTareas(self):
        self.cursor.execute("SELECT * FROM Tareas;")
        data = self.cursor.fetchall()
        return data
    def leerTareaId(self, idTarea):
        self.cursor.execute("SELECT * FROM Tareas WHERE Id = {}".format(idTarea))
        data = self.cursor.fetchall()
        return data
    def eliminarTarea(self, idTarea):
        self.cursor.execute("DELETE FROM Tareas WHERE Id = {}".format(idTarea))
        self.conexion.commit()
        print("Registro eliminado")
    def editarTarea(self, idTarea, nuevaTarea):
        self.cursor.execute("UPDATE Tareas SET Tarea = '{}' WHERE Id = {}".format(nuevaTarea, idTarea))
        self.conexion.commit()
        print("Registro actualizado")