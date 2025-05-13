# from models.semaforo import Semaforo
# from models.sensor import Sensor
# from models.leitura_sensor import LeituraSensor
# from models.evento import EventoSemaforo
# from models.cancela import Cancela
# from datetime import datetime

# # Teste CRUD - Semaforo
# print("\n=== Teste: Semaforo ===")
# s1 = Semaforo("Rua Teste 123", "verde_carros", 80)
# s1.save()
# print(f"Semaforo criado: ID = {s1.id}")

# s1.status_atual = "vermelho_carros"
# s1.save()
# print("Semaforo atualizado.")

# for s in Semaforo.selectAll():
#     print(vars(s))

# # Teste CRUD - Sensor
# print("\n=== Teste: Sensor ===")
# sensor = Sensor("proximidade_carro", s1.id)
# sensor.save()
# print(f"Sensor criado: ID = {sensor.id}")

# sensor.tipo = "luminosidade"
# sensor.save()
# print("Sensor atualizado.")

# for sen in Sensor.selectAll():
#     print(vars(sen))

# # Teste CRUD - LeituraSensor
# print("\n=== Teste: LeituraSensor ===")
# leitura = LeituraSensor(sensor.id, 52.3, datetime.now())
# leitura.save()
# print(f"Leitura criada: ID = {leitura.id}")

# for l in LeituraSensor.selectAll():
#     print(vars(l))

# # Teste CRUD - EventoSemaforo
# print("\n=== Teste: EventoSemaforo ===")
# evento = EventoSemaforo(s1.id, "mudanca_sinal", "Troca de verde para vermelho", datetime.now())
# evento.save()
# print(f"Evento criado: ID = {evento.id}")

# for ev in EventoSemaforo.selectAll():
#     print(vars(ev))

# # Teste CRUD - Cancela
# print("\n=== Teste: Cancela ===")
# cancela = Cancela(s1.id, "ativa")
# cancela.save()
# print(f"Cancela criada: ID = {cancela.id}")

# cancela.status = "recolhida"
# cancela.save()
# print("Cancela atualizada.")

# for c in Cancela.selectAll():
#     print(vars(c))

# # 🧹 Limpeza (caso queira deletar tudo no final do teste)
# # cancela.deletar()
# # evento.deletar()
# # leitura.deletar()
# # sensor.deletar()
# # s1.deletar()
# # print("\nTodos os registros foram deletados.")
