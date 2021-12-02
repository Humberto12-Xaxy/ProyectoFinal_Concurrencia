import threading
import random
import time
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Auto(threading.Thread):
    def __init__(self, piloto, pos, vueltas,label, ganador):
        threading.Thread.__init__(self)
        self.estado = ''
        self.vuelta = 1
        self.piloto = piloto
        self.pos = pos
        self.label = label
        self.ganador = ganador
        self.vuelt = vueltas
    
    def vueltas(self, band):

        aleatorioContador = 1    
        aleatorioVuelta = random.choice([10,20,30,50])
        aleatorioTiempo = random.choice([0.02,0.01,0.03])

        while aleatorioContador <=  aleatorioVuelta:
            print("Estado = ", self.estado,"Piloto: ", self.piloto,"Vuelta: ",self.vuelta)
            aleatorioContador += 1
            time.sleep(aleatorioTiempo)
            if (aleatorioVuelta == aleatorioContador and band == False):
                self.vuelta = self.vuelta + 1
                self.estado = 'En pista'
                self.label.setText(f'Estado: {self.estado}')

              
        if band == True:
            
            self.pits()      
            self.band = False
                
                
    def pits(self):  
        aleatorioTiempo = random.choice([1.8,2,2.5,3])
        time.sleep(aleatorioTiempo)
        self.estado = 'En pits'
        self.label.setText(f'Estado: {self.estado}')

    def run(self):
        global win
        win = False
        pilotos = [['Checo', False], ['Mazepin', False], ['Shumager', False]]
        aleatorio = []
        while True:

            if win == True:
                print('entre')
                break

            aleatorio = random.choice(pilotos)
            for j in range(len(pilotos)):
                if aleatorio == pilotos[j]:
                    pilotos[j][1] = True          
            self.vueltas(pilotos[self.pos][1])
            
            self.vuelt.setText(f'Vueltas: {self.vuelta}')

            if self.vuelta == 15:
                win = True
                self.ganador.setText(f'El ganador es {self.piloto}')
                print('El ganador es: ', self.piloto)
                break
            
            pilotos = [['Checo', False], ['Mazepin', False], ['Shumager', False]]
