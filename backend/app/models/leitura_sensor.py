from backend.app.database import Database

class LeituraSensor:
    def __init__(self, id_sensor, valor, data_hora, id=None):
        self.id = id
        self.id_sensor = id_sensor
        self.valor = valor
        self.data_hora = data_hora
    
    def save(self):
        db = Database()
        if self.id:
            db.execute(""" UPDATE LeituraSensor SET id_sensor=%s, valor=%s, data_hora=%s WHERE id=%s """, (self.id_sensor, self.valor, self.data_hora, self.id))
        else:
            db.execute(""" INSERT INTO LeituraSensor (id_sensor, valor, data_hora) VALUES (%s, %s, %s) """, (self.id_sensor, self.valor, self.data_hora))
            self.id = db.cursor.lastrowid
        db.close()
    
    def delete(self):
        db = Database()
        db.execute("DELETE FROM LeituraSensor WHERE id=%s", (self.id,))
        db.close()
    
    @staticmethod
    def selectAll():
        db = Database()
        db.query("SELECT * FROM LeituraSensor")
        results = db.fetchall()
        db.close()
        return [LeituraSensor(**r) for r in results]
        