import time
class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño = daño
        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {self.daño}")
        jugador.recibir_daño(self.daño)


jugador = Jugador("Juan", 100, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raul", 50, 10, 70)

while jugador.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(2)

print(f"El jugador {jugador.nombre} ha muerto")

# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
# 1. Agregar logica de daño aleatorio al enemigo.
# 2. Agregar lógica de contraataque del jugador.
# 3. Agregar posibilidad de daño crítico en contra ataque del jugador.

