import threading
import random
import time

class Auto(threading.Thread):
    def __init__(self, piloto, pos):
        threading.Thread.__init__(self)
        self.estado = ''
        self.vuelta = 0
        self.piloto = piloto
        self.pos = pos
    
    def vueltas(self, band):

        aleatorioContador = 0    
        aleatorioVuelta = random.choice([5,10,15,20])
        aleatorioTiempo = random.choice([0.02,0.01,0.03])

        while aleatorioContador <=  aleatorioVuelta:
            print("Estado = ", self.estado,"Piloto: ", self.piloto,"Vuelta: ",self.vuelta)
            aleatorioContador += 1
            time.sleep(aleatorioTiempo)
            if (aleatorioVuelta == aleatorioContador and band == False):
                self.vuelta = self.vuelta + 1
                self.estado = 'En pista'
              
        if band == True:
            self.pits()      
            self.band = False
                
                
    def pits(self):  
        aleatorioTiempo = random.choice([1.8,2,2.5,3])
        time.sleep(aleatorioTiempo)
        self.estado = 'En pits'

    def run(self):
        global win
        win = False
        pilotos = [['Checo', False], ['Mazepin', False], ['Shumager', False]]
        aleatorio = []
        while self.vuelta <= 5 and win == False:
            aleatorio = random.choice(pilotos)
            for j in range(len(pilotos)):
                if aleatorio == pilotos[j]:
                    pilotos[j][1] = True          
            self.vueltas(pilotos[self.pos][1])
            
            if self.vuelta == 5:
                win = True
                print('El ganador es: ', self.piloto)

            pilotos = [['Checo', False], ['Mazepin', False], ['Shumager', False]]

        

if __name__ == '__main__':
    pilotos = [['Checo', False], ['Mazepin', False], ['Shumager', False]]
    
    carro1 = Auto(pilotos[0][0], 0)
    carro2 = Auto(pilotos[1][0], 1)
    carro3 = Auto(pilotos[2][0], 2)
    print(carro1.is_alive())
    carro1.start()
    carro2.start()
    carro3.start() 
    
    print(carro1.is_alive())
    
    carro1.join()
    carro2.join()
    carro3.join()
        
