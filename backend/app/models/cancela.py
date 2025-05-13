from backend.app.database import Database

class Cancela:
    def __init__(self, id_semaforo, status, id=None):
        self.id = id
        self.id_semaforo = id_semaforo
        self.status = status # 'ativa' ou 'recolhida'
    
    def save(self):
        db = Database()
        if self.id:
           db.execute(""" UPDATE Cancela SET id_semaforo=%s, status=%s WHERE id=%s """, (self.id_semaforo, self.status, self.id))
        else:
            db.execute(""" INSERT INTO Cancela (id_semaforo, status) VALUES (%s, %s) """, (self.id_semaforo, self.status))
            self.id = db.cursor.lastrowid
        db.close()
    
    def delete(self):
        if self.id:
            db = Database()
            db.execute("DELETE FROM Cancela WHERE id=%s", (self.id,))
            db.close()
    
    @staticmethod
    def selectAll():
        db = Database()
        db.query("SELECT * FROM Cancela")
        results = db.fetchall()
        db.close()
        return [Cancela(**c) for c in results]
