from backend.app.database import Database

class Sensor:
    def __init__(self, tipo, id_semaforo, status=True, id=None):
        self.id = id
        self.tipo = tipo
        self.id_semaforo = id_semaforo
        self.status = status

    def save(self):
        db = Database()
        if self.id:
            db.execute(""" UPDATE Sensor SET tipo=%s, id_semaforo=%s, status=%s WHERE id=%s """, (self.tipo, self.id_semaforo, self.status, self.id))
        else:
            db.execute(""" INSERT INTO Sensor (tipo, id_semaforo, status) VALUES (%s, %s, %s) """, (self.tipo, self.id_semaforo, self.status))
            self.id = db.cursor.lastrowid
        db.close()
    
    def delete(self):
        if self.id:
            db = Database()
            db.execute("DELETE FROM SENSOR WHERE id=%s", (self.id))
            db.close()

    @staticmethod
    def selectAll():
        db = Database()
        db.query("SELECT * FROM Sensor")
        results = db.fetchall()
        db.close()
        return [Sensor(**s) for s in results]
