from backend.app.database import Database

class EventoSemaforo:
    def __init__(self, id_semaforo, tipo_evento, descricao, data_hora, id=None):
        self.id = id
        self.id_semaforo = id_semaforo
        self.tipo_evento = tipo_evento
        self.descricao = descricao
        self.data_hora = data_hora
    
    def save(self):
        db = Database()
        if self.id:
            db.execute(""" UPDATE EventoSemaforo SET id_semaforo=%s, tipo_evento=%s, descricao=%s, data_hora=%s WHERE id=%s """, (self.id_semaforo, self.tipo_evento, self.descricao, self.data_hora, self.id))
        else:
            db.execute(""" INSERT INTO EventoSemaforo (id_semaforo, tipo_evento, descricao, data_hora) VALUES (%s, %s, %s, %s) """, (self.id_semaforo, self.tipo_evento, self.descricao, self.data_hora))
            self.id = db.cursor.lastrowid
        db.close()
    
    def delete(self):
        if self.id:
            db = Database()
            db.execute("DELETE FROM EventoSemaforo WHERE id=%s", (self.id,))
            db.close()
    
    @staticmethod
    def selectAll():
        db = Database()
        db.query("SELECT * FROM EventoSemaforo")
        results = db.fetchall()
        db.close()
        return [EventoSemaforo(**e) for e in results]
    