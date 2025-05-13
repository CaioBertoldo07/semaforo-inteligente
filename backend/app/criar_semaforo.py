from app.models.semaforo import Semaforo

s = Semaforo("Av. Brasil, Centro", "verde_carros", 85)
s.save()
print("Semáforo criado com ID:", s.id)
