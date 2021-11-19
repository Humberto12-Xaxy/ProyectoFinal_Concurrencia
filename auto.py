import threading
import random
import time

class Auto(threading.Thread):
    def __init__(self, estado, vuelta, piloto, bandera):
        threading.Thread.__init__(self)
        self.estado = estado
        self.vuelta = vuelta
        self.piloto = piloto
        self.band = bandera
    
    def vueltas(self):

        for i in range(5):

            aleatorioContador = 0    
            aleatorioVuelta = random.choice([100,110,120,115])
            aleatorioTiempo = random.choice([0.02,0.01,0.03])

            while aleatorioContador <=  aleatorioVuelta:
                aleatorioContador += 1
                time.sleep(aleatorioTiempo)
                if (aleatorioVuelta == aleatorioContador and self.band == False):
                    self.estado = 'En pista'
                    self.vuelta = self.vuelta + 1
                elif self.band == True:
                    self.pits()
            if(self.vuelta == 5):
                print('El ganador es ' + self.piloto)
    
    def pits(self):
        aleatorioTiempo = random.choice([1.8,2,2.5,3])
        time.sleep(aleatorioTiempo)
        self.estado = 'En pits'
        print(aleatorioTiempo)


    def run(self):
            self.vueltas()

carro1 = Auto('En pista', 0, 'checo', True)
carro1.start()

                
             
              

        
