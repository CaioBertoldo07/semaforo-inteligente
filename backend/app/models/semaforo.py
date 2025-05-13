from app.database import Database

class Semaforo:
    def __init__(self, localizacao, status_atual, nivel_luminosidade, id=None):
        self.id = id
        self.localizacao = localizacao
        self.status_atual = status_atual
        self.nivel_luminosidade = nivel_luminosidade
        
    def save(self):
        db = Database()
        if self.id:
           db.execute(""" UPDATE Semaforo SET localizacao=%s, status_atual=%s, nivel_luminosidade=%s WHERE id=%s """, (self.localizacao, self.status_atual, self.nivel_luminosidade, self.id))
        else:
            db.execute(""" INSERT INTO Semaforo (localizacao, status_atual, nivel_luminosidade) VALUES (%s, %s, %s) """, (self.localizacao, self.status_atual, self.nivel_luminosidade))       
            self.id = db.cursor.lastrowid
        db.close()
    
    def delete(self):
        if self.id:
            db = Database()
            db.execute("DELETE FROM Semaforo WHERE id=%s", self.id)
            db.close()
    
    @staticmethod
    def selectAll():
        db = Database()
        db.query("SELECT * FROM semaforo")
        results = db.fetchall()
        db.close()
        return [Semaforo(**s) for s in results]
        