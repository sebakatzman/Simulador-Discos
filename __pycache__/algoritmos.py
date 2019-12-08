from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

class Algoritmo:

    def fifo(self, disco, lista):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            distanciaTotal = 0
            cilindro = disco.posicionCabeza
            distanciaRecorrida = 0
            listaAux = lista
            texto = "-----Estrategia utilizada: Fifo-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(listaAux)
            print (listaImpr)
            datos.append(listaImpr)
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            cantMovimientos = 0
            for l in listaAux:
                distanciaRecorrida = cilindro - l
                #Compruebo si se movio para aumentar la cant de movimientos
                if distanciaRecorrida != 0:
                    cantMovimientos = cantMovimientos + 1
                if (distanciaRecorrida < 0):
                    distanciaRecorrida = distanciaRecorrida * -1
                distanciaTotal += distanciaRecorrida
                distanciaImprimir = (str(listaAux.index(l)) + '----' + str(cilindro)+ ' - '+ str(l) + '  =  ' + str(distanciaRecorrida) + '\n')
                print (distanciaImprimir)
                datos.append(distanciaImprimir)
                distanciaRecorrida = 0
                cilindro = l
            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ns' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def verificarListaDeRequerimientos(self, disco, lista):
        esValida = True
        for elemento in lista:
            if elemento > disco.totalPistas:
                esValida = False
        return esValida

    def getRetardoRotacional(self, velocidadRotacion):
        return (self.getVueltaCompleta(velocidadRotacion)) / 2

    def getTiempoTransferencia(self, cantSectorPorPista, velocidadRotacion):
        return (1 * int(self.getVueltaCompleta(velocidadRotacion))) / cantSectorPorPista

    def getVueltaCompleta(self, velocidadRotacion):
        return (1 * 60000) / velocidadRotacion
    
    def getTiempoAccesoTotal(self, cantMovimientos, disco, lista):
        rr = self.getRetardoRotacional(disco.velocidadRotacion)
        tt = self.getTiempoTransferencia(disco.tamañoBloque, disco.velocidadRotacion)
        tat = (cantMovimientos * disco.seekTime) + (rr + tt) * 9
        return tat

    def sstf(self, disco, lista):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            distanciaTotal = 0
            cilindro = disco.posicionCabeza
            distanciaRecorrida = 0
            listaAux = lista
            tamanio = len(lista)
            contador = 0
            cantMovimientos = 0
            texto = "-----Estrategia utilizada: SSTF-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(listaAux)
            print (listaImpr)
            datos.append(listaImpr)
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            while contador != tamanio:
                pos = self.buscarMenorDistancia(listaAux, cilindro)
                distanciaRecorrida = cilindro - listaAux[pos-1]
                if distanciaRecorrida < 0:
                    distanciaRecorrida = distanciaRecorrida * -1
                txt = (str(cilindro) + "  -  " + str(listaAux[pos-1]) + "  =  " + str(distanciaRecorrida)  + '\n')
                datos.append(txt)
                print (txt)
                if distanciaRecorrida != 0:
                    cantMovimientos = cantMovimientos + 1
                cilindro = listaAux[pos-1]
                listaAux.pop(pos-1)
                distanciaTotal = distanciaTotal + distanciaRecorrida
                contador += 1
            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def buscarMenorDistancia(self, listaAux, cilindro):
        resta = 8000
        pos = 0
        posicion = 0
        res = 0
        for l in listaAux:
            pos = pos + 1
            res = cilindro - l
            if res < 0: 
                res = res * -1
            if res < resta:
                resta = res
                posicion = pos
            res = 0  
        return posicion       

    def scan(self, disco, lista):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            listaVuelta = []
            distanciaRecorrida = 0
            distanciaTotal = 0
            listaAux = lista
            cantMovimientos = 0
            cilindro = disco.posicionCabeza
            contador = 0
            tamanio = len(lista)
            cantMovimientos = 0
            listaAux = lista
            texto = "-----Estrategia utilizada: SCAN-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            listaImpr = str(listaAux)
            datos.append(listaImpr)
            datos.append(texto)
            listaImprimir = listaAux
            print (listaImprimir)
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            if (disco.posicionCabeza == 0) or (disco.sentido == 'C'):
                #Comienza algoritmos de scan creciente
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                    distanciaRecorrida = cilindro - candidato
                    if distanciaRecorrida < 0:
                        distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaAux:
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
                #Hice el primer scaneo, ahora veo si no llegue al final para ir hasta el final
                if (cilindro != disco.totalPistas):
                    distanciaRecorrida = cilindro - disco.totalPistas
                    distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = disco.totalPistas
                #Ahora doy la vuelta y vuelvo en sentido contrario
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    distanciaTotal += distanciaRecorrida
                    txt = (str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Compruebo si llega al principio, sino hago que valla.
                if cilindro != 0:
                    distanciaRecorrida = cilindro 
                    txt = (str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                #Fin de algoritmo Creciente...
            else:
                #Comienza algoritmo scan descreciente
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaDecrecienteScanAux(listaAux, cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = (str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    cilindro = candidato
                    if candidato in listaAux:
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
                #Hice el primer scaneo, ahora veo si no llegue al principio  para ir hasta el final
                if (cilindro != 0):
                    distanciaRecorrida = cilindro 
                    txt = (str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = 0
                #Ahora doy la vuelta y vuelvo en sentido contrario
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaCrecienteScanAux(cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    distanciaRecorrida = distanciaRecorrida * -1
                    txt = (str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Compruebo si llega al final, sino hago que valla.
                if cilindro != disco.totalPistas:
                    distanciaRecorrida = cilindro - disco.totalPistas
                    distanciaRecorrida = distanciaRecorrida * -1
                    txt = (str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                #Fin de algoritmo decreciente...

            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def cscan(self, disco, lista):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            listaVuelta = []
            distanciaRecorrida = 0
            distanciaTotal = 0
            listaAux = lista
            cantMovimientos = 0
            contador = 0
            cilindro = disco.posicionCabeza
            tamanio = len(lista)
            cantMovimientos = 0
            texto = "-----Estrategia utilizada: C-SCAN-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(listaAux)
            print (listaImpr)
            datos.append(listaImpr)
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            if (disco.posicionCabeza == 0) or (disco.sentido == 'C'):
                #Comienza algoritmos de cscan creciente
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                    distanciaRecorrida = cilindro - candidato
                    if distanciaRecorrida < 0:
                        distanciaRecorrida = distanciaRecorrida * -1
                    txt = (str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n')
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaAux:
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
                #Hice el primer scaneo, ahora veo si no llegue al final para ir hasta el final
                if (cilindro != disco.totalPistas):
                    distanciaRecorrida = cilindro - disco.totalPistas
                    distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = disco.totalPistas
                #Ahora vuelvo a la pista 0 por que es cscan
                if (len(listaVuelta) != 0):
                    distanciaRecorrida = cilindro - 0
                    txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = 0
                #Recorro nuevamente en creciente
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaCrecienteScan(listaVuelta, cilindro, listaAux, disco)
                    distanciaRecorrida = cilindro - candidato
                    if distanciaRecorrida < 0:
                        distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Compruebo si llega al final, sino hago que valla.
                if (cilindro != 0) and (cilindro != disco.totalPistas):
                    distanciaRecorrida = (cilindro - disco.totalPistas) * -1
                    txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                #Fin de algoritmo Creciente...
            else:
                #Comienza algoritmo scan descreciente
                print("Comienza en decreciente")
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaDecrecienteScanAux(listaAux, cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    cilindro = candidato
                    if candidato in listaAux:
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
                #Hice el primer scaneo, ahora veo si no llegue al principio  para ir hasta el
                if (cilindro != 0):
                    distanciaRecorrida = cilindro 
                    txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = 0
                #Ahora vuelvo a decreciente
                contador = 0
                tamanio = len(listaVuelta)
                if (tamanio != 0):
                        distanciaRecorrida = disco.totalPistas
                        distanciaRecorrida = cilindro 
                        txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                        print (txt)
                        datos.append(txt)
                        if distanciaRecorrida != 0:
                            cantMovimientos += 1
                        distanciaTotal += distanciaRecorrida
                        cilindro = disco.totalPistas
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Compruebo si llega al principio, sino hago q valla
                if cilindro != 0:
                    distanciaRecorrida = cilindro
                    txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                #Fin de algoritmo decreciente...

            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def look(self, disco, lista):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            listaVuelta = []
            distanciaRecorrida = 0
            distanciaTotal = 0
            listaAux = lista
            cantMovimientos = 0
            cilindro = disco.posicionCabeza
            tamanio = len(lista)
            cantMovimientos = 0
            texto = "-----Estrategia utilizada: LOOK-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(listaAux) + '\n'
            print (listaImpr)
            datos.append(listaImpr)
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            if (disco.posicionCabeza == 0) or (disco.sentido == 'C'):
                #Comienza algoritmos de C-Scan creciente
                print("Comienza en creciente")
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                    distanciaRecorrida = cilindro - candidato
                    if distanciaRecorrida < 0:
                        distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    cilindro = candidato
                    if candidato in listaAux:
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
                #Ahora doy la vuelta y vuelvo en sentido contrario
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Fin de algoritmo Creciente...
            else:
                #Comienza algoritmo scan decreciente
                print("Comienza en decreciente")
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaDecrecienteScanAux(listaAux, cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    cilindro = candidato
                    if candidato in listaAux:    
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
            
                #Ahora doy la vuelta y vuelvo en sentido contrario
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaCrecienteScanAux(cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Fin de algoritmo decreciente...

            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def clook(self, disco, lista):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            listaVuelta = []
            distanciaRecorrida = 0
            distanciaTotal = 0
            listaAux = lista
            cantMovimientos = 0
            contador = 0
            cilindro = disco.posicionCabeza
            tamanio = len(lista)
            texto = "-----Estrategia utilizada: C-LOOK-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(listaAux) + '\n'
            print (listaImpr)
            datos.append(listaImpr)
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            if (disco.posicionCabeza == 0) or (disco.sentido == 'C'):
                #Comienza algoritmos de clook creciente
                print("Comienza en creciente")
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                    distanciaRecorrida = cilindro - candidato
                    if distanciaRecorrida < 0:
                        distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaAux:    
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
                #Ahora vuelvo al primer requerimiento mas chico
                if (len(listaVuelta) != 0):
                    numero_menor = 5000
                    for l in listaVuelta:
                        if l < numero_menor:
                            numero_menor = l    
                    distanciaRecorrida = cilindro - numero_menor
                    txt = str(cilindro) + "  -  " + str(numero_menor) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = numero_menor
                    if numero_menor in listaVuelta:
                        listaVuelta.remove(numero_menor)
                #Ahora vuelvo a recorrer en creciente
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaCrecienteScan(listaVuelta, cilindro, listaAux, disco)
                    distanciaRecorrida = cilindro - candidato
                    if distanciaRecorrida < 0:
                        distanciaRecorrida = distanciaRecorrida * -1
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Fin de algoritmo Creciente...
            else:
                #Comienza algoritmo clook decreciente
                print("Comienza en decreciente")
                finPrimerScan = True
                while (finPrimerScan):
                    candidato = self.buscarMenorDistanciaDecrecienteScanAux(listaAux, cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    cilindro = candidato
                    if candidato in listaAux:
                        listaAux.remove(candidato)
                    if (len(listaAux) == 0):
                        finPrimerScan = False
            #Ahora vuelvo al ultimo requerimiento mas grande
                if (len(listaVuelta) != 0):
                    numero_mayor = 0
                    for l in listaVuelta:
                        if l > numero_mayor:
                            numero_mayor = l    
                    distanciaRecorrida = (cilindro - numero_mayor) * -1
                    txt = str(cilindro) + "  -  " + str(numero_mayor) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaTotal += distanciaRecorrida
                    cilindro = numero_mayor
                    if numero_mayor in listaVuelta:
                        listaVuelta.remove(numero_mayor)
                #Ahora vuelvo a recorrer en decreciente
                contador = 0
                tamanio = len(listaVuelta)
                while contador != tamanio:
                    candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                    distanciaRecorrida = cilindro - candidato
                    txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                    print (txt)
                    datos.append(txt)
                    distanciaTotal += distanciaRecorrida
                    #Si se movio entonces sumamos uno a cant movimientos
                    if distanciaRecorrida != 0:
                        cantMovimientos += 1
                    distanciaRecorrida = 0
                    contador += 1
                    cilindro = candidato
                    if candidato in listaVuelta:
                        listaVuelta.remove(candidato)
                #Fin de algoritmo Creciente...

            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def buscarMenorDistanciaCrecienteScan(self, listaAux, cilindro, listaVuelta, disco):
        resta = 8000
        res = 0
        distanciaRecorrida = 0
        listaAuxEliminar = []
        numero_candidato = disco.totalPistas
        for numero in listaAux:
            distanciaRecorrida = cilindro - numero
            if distanciaRecorrida <= 0:
                res = distanciaRecorrida * -1
                if res < resta:
                    resta = res
                    numero_candidato = numero
            else:
                listaAuxEliminar.append(numero)
                listaVuelta.append(numero)
        for lista in listaAuxEliminar:
            listaAux.remove(lista)
        if numero_candidato == disco.totalPistas:
            listaAux.append(numero_candidato)
        return numero_candidato

    def buscarMenorDistanciaDecrecienteScan(self, cilindro, listaVuelta):
        menorDistancia = 8000
        distanciaRecorrida = 0
        candidato = 0
        for numero in listaVuelta:
            distanciaRecorrida = cilindro - numero
            if distanciaRecorrida < menorDistancia:
                menorDistancia = distanciaRecorrida
                candidato = numero
            distanciaRecorrida = 0
        return candidato

    def buscarMenorDistanciaDecrecienteScanAux(self, listaAux, cilindro, listaVuelta):
        resta = 8000
        distanciaRecorrida = 0
        listaAuxEliminar = []
        numero_candidato = 0
        for numero in listaAux:
            distanciaRecorrida = cilindro - numero
            if distanciaRecorrida >= 0:
                if distanciaRecorrida < resta:
                    resta = distanciaRecorrida
                    numero_candidato = numero
            else:
                listaAuxEliminar.append(numero)
                listaVuelta.append(numero)
        for lista in listaAuxEliminar:
            listaAux.remove(lista)
        return numero_candidato

    def buscarMenorDistanciaCrecienteScanAux(self, cilindro, listaVuelta):
        menorDistancia = 8000
        distanciaRecorrida = 0
        for numero in listaVuelta:
            distanciaRecorrida = cilindro - numero
            distanciaRecorrida = distanciaRecorrida * -1
            if distanciaRecorrida < menorDistancia:
                menorDistancia = distanciaRecorrida
                candidato = numero
            distanciaRecorrida = 0
        return candidato
    
    def fscan(self, disco, lista, primeros): #Primeros: primeros en servirse, el resto llega 
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            listaVuelta = []
            distanciaRecorrida = 0
            distanciaTotal = 0
            cantMovimientos = 0
            cilindro = disco.posicionCabeza
            listaAux = []
            contador = 0
            texto = "-----Estrategia utilizada: F-SCAN-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(lista) + '\n'
            print (listaImpr)
            datos.append(listaImpr)
            #Divido las listas en 2 
            #Armo la lista 1
            while contador != primeros:
                elemento = lista[contador]
                listaAux.append(elemento)
                contador += 1
            listaImpr = 'Primera Lista: ' + str(listaAux) + '\n'
            print (listaImpr)
            datos.append(listaImpr)
            rangoLista = len(lista)
            listaAux2 = []
            #Armo la lista 2
            while contador != rangoLista:
                elemento = lista[contador]
                listaAux2.append(elemento)
                contador += 1 
            listaImpr = 'Segunda Lista: ' + str(listaAux2) + '\n'
            print (listaImpr)
            datos.append(listaImpr)
            cantMovimientos = 0
            texto = "Orden en el que se atienden los requerimientos"+'\n'
            datos.append(texto)
            print (texto)
            if (disco.posicionCabeza == 0) or (disco.sentido == 'C'):
                #Comienza algoritmos de scan creciente
                creciente = True
                print("Comienza en creciente")
                finPrimerScan = True
                for i in range(2):
                    if (creciente):
                        while (finPrimerScan):
                            candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                            distanciaRecorrida = cilindro - candidato
                            if distanciaRecorrida < 0:
                                distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            distanciaTotal += distanciaRecorrida
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            contador += 1
                            cilindro = candidato
                            if candidato in listaAux:
                                listaAux.remove(candidato)
                            if (len(listaAux) == 0):
                                finPrimerScan = False
                        #Hice el primer scaneo, ahora veo si no llegue al final para ir hasta el final
                        if (cilindro != disco.totalPistas):
                            distanciaRecorrida = cilindro - disco.totalPistas
                            distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = disco.totalPistas
                        #Ahora doy la vuelta y vuelvo en sentido contrario
                        contador = 0
                        tamanio = len(listaVuelta)
                        while contador != tamanio:
                            candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                            distanciaRecorrida = cilindro - candidato
                            distanciaTotal += distanciaRecorrida
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            contador += 1
                            cilindro = candidato
                            if candidato in listaVuelta:    
                                listaVuelta.remove(candidato)
                        #Compruebo si llega al principio, sino hago que valla.
                        if (cilindro != 0) and (cilindro != disco.totalPistas):
                            distanciaRecorrida = cilindro 
                            txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = 0
                        if (cilindro == disco.totalPistas):
                            creciente = False
                        #Fin de algoritmo Creciente...
                        listaAux = listaAux2
                        finPrimerScan = True
                        listaVuelta = []
                    else:
                        #Comienza a recorrer la segunda lista en decreciente
                        listaVuelta = listaAux2
                        if listaVuelta:
                            while (finPrimerScan):
                                candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                                distanciaRecorrida = cilindro - candidato
                                txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                distanciaTotal += distanciaRecorrida
                                #Si se movio entonces sumamos uno a cant movimientos
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaRecorrida = 0
                                contador += 1
                                cilindro = candidato
                                if candidato in listaVuelta:
                                    listaVuelta.remove(candidato)
                                if (len(listaVuelta) == 0):
                                    finPrimerScan = False
                            #Hice el primer scaneo, ahora veo si no llegue al principio para ir hasta el
                            if (cilindro != 0):
                                distanciaRecorrida = cilindro
                                txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaTotal += distanciaRecorrida
                                cilindro = 0
                                #Fin de algoritmo Decreciente...
            else:
                #Comienza algoritmo scan descreciente
                print("Comienza en decreciente")
                finPrimerScan = True
                decreciente = True
                for i in range(2):
                    if decreciente:
                        while (finPrimerScan):
                            candidato = self.buscarMenorDistanciaDecrecienteScanAux(listaAux, cilindro, listaVuelta)
                            distanciaRecorrida = cilindro - candidato
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            distanciaTotal += distanciaRecorrida
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            cilindro = candidato
                            if candidato in listaAux: 
                                listaAux.remove(candidato)
                            if (len(listaAux) == 0):
                                finPrimerScan = False
                        #Hice el primer scaneo, ahora veo si no llegue al principio  para ir hasta el
                        if (cilindro != 0):
                            distanciaRecorrida = cilindro 
                            txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = 0
                        #Ahora doy la vuelta y vuelvo en sentido contrario
                        contador = 0
                        tamanio = len(listaVuelta)
                        while contador != tamanio:
                            candidato = self.buscarMenorDistanciaCrecienteScanAux(cilindro, listaVuelta)
                            distanciaRecorrida = cilindro - candidato
                            distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            distanciaTotal += distanciaRecorrida
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            contador += 1
                            cilindro = candidato
                            if candidato in listaVuelta: 
                                listaVuelta.remove(candidato)
                        #Compruebo si llega al final, sino hago que valla.
                        if (cilindro != disco.totalPistas) and (cilindro != 0):
                            distanciaRecorrida = cilindro - disco.totalPistas
                            distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = disco.totalPistas
                        if (cilindro == 0):
                            decreciente = False
                        #Fin de algoritmo decreciente...
                        listaAux = listaAux2
                        finPrimerScan = True
                        listaVuelta = []
                    else:
                        #Comienza a recorrer la segunda lista en creciente
                        listaAux = listaAux2
                        if listaAux:
                            while (finPrimerScan):
                                candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                                distanciaRecorrida = (cilindro - candidato) * -1
                                txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                distanciaTotal += distanciaRecorrida
                                #Si se movio entonces sumamos uno a cant movimientos
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaRecorrida = 0
                                contador += 1
                                cilindro = candidato
                                if candidato in listaAux: 
                                    listaAux.remove(candidato)
                                if (len(listaAux) == 0):
                                    finPrimerScan = False
                            #Hice el primer scaneo, ahora veo si no llegue al final para ir hasta el
                            if (cilindro != disco.totalPistas):
                                distanciaRecorrida = (cilindro - disco.totalPistas ) * -1
                                txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaTotal += distanciaRecorrida
                                cilindro = disco.totalPistas
                                #Fin de algoritmo Decreciente...

            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)
        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos

    def nsteepscan(self, disco, lista, n):
        datos = []
        listaValida = self.verificarListaDeRequerimientos(disco, lista)
        if listaValida:
            listaVuelta = []
            distanciaRecorrida = 0
            distanciaTotal = 0
            cantMovimientos = 0
            cilindro = disco.posicionCabeza
            listaAux = []
            contador = 0
            texto = "-----Estrategia utilizada: N-STEP-SCAN-----"+'\n'
            print (texto)
            datos.append(texto)
            texto = "Cadena a de datos a simular"+'\n'
            datos.append(texto)
            print (texto)
            listaImpr = str(lista) + '\n'
            print (listaImpr)
            datos.append(listaImpr)
            #Divido las listas en n 
            cantListas = int(len(lista) / n)
            print ('n q recibo desde afuera: ', n)
            listaAuxiliar = []
            indice = 0
            elementosLeidos = 0
            listaDeListas = []
            cantElementos = len(lista)
            print (cantElementos)
            #Armo las listas segun N
            for z in range(cantListas):
                for x in range(n):
                    elemento = lista[indice]
                    listaAuxiliar.append(elemento)
                    indice += 1
                    elementosLeidos += 1
                    print ('indice: ', indice)
                listaDeListas.append(listaAuxiliar)
                listaAuxiliar = []
            #Por si quedo algun elemento fuera de una lista, lo meto en otra lista
            while elementosLeidos < cantElementos:
                elemento = lista[indice]
                listaAuxiliar.append(elemento)
                indice += 1
                elementosLeidos += 1

            if (listaAuxiliar):
                listaDeListas.append(listaAuxiliar)
            cantListas = len(listaDeListas)
            numero_lista = 1
            print ('cantidad de listas: ', cantListas)
            for lis in listaDeListas:
                txt = 'Lista numero: ' + str(numero_lista) + '---' + str(lis) + '\n'
                datos.append(txt)
                numero_lista += 1
                print(lis)
            indice = 0
            listaAux = listaDeListas[indice] 
            if (disco.posicionCabeza == 0) or (disco.sentido == 'C'):
                #Comienza algoritmos de scan creciente
                creciente = True
                print("Comienza en creciente")
                finPrimerScan = True
                for i in range(cantListas):
                    if (creciente):
                        while (finPrimerScan):
                            candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                            distanciaRecorrida = cilindro - candidato
                            if distanciaRecorrida < 0:
                                distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            distanciaTotal += distanciaRecorrida
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            contador += 1
                            cilindro = candidato
                            if candidato in listaAux:
                                listaAux.remove(candidato)
                            if (len(listaAux) == 0):
                                finPrimerScan = False
                        #Hice el primer scaneo, ahora veo si no llegue al final para ir hasta el final
                        if (cilindro != disco.totalPistas):
                            distanciaRecorrida = cilindro - disco.totalPistas
                            distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = disco.totalPistas
                        #Ahora doy la vuelta y vuelvo en sentido contrario
                        contador = 0
                        tamanio = len(listaVuelta)
                        while contador != tamanio:
                            candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaVuelta)
                            distanciaRecorrida = cilindro - candidato
                            distanciaTotal += distanciaRecorrida
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            contador += 1
                            cilindro = candidato
                            if candidato in listaVuelta:
                                listaVuelta.remove(candidato)
                        #Compruebo si llega al principio, sino hago que valla.
                        if (cilindro != 0) and (cilindro != disco.totalPistas):
                            distanciaRecorrida = cilindro 
                            txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = 0
                        if (cilindro == disco.totalPistas):
                            creciente = False
                        #Fin de algoritmo Creciente...
                        indice += 1
                        if indice < cantListas:
                            listaAux = listaDeListas[indice]
                        finPrimerScan = True
                        listaVuelta = []
                    else:
                        #Comienza a recorrer en decreciente
                        if listaAux:
                            while (finPrimerScan):
                                candidato = self.buscarMenorDistanciaDecrecienteScan(cilindro, listaAux)
                                distanciaRecorrida = cilindro - candidato
                                txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                distanciaTotal += distanciaRecorrida
                                #Si se movio entonces sumamos uno a cant movimientos
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaRecorrida = 0
                                contador += 1
                                cilindro = candidato
                                if candidato in listaAux:
                                    listaAux.remove(candidato)
                                if (len(listaAux) == 0):
                                    finPrimerScan = False
                            #Hice el primer scaneo, ahora veo si no llegue al principio para ir hasta el
                            if (cilindro != 0):
                                distanciaRecorrida = cilindro
                                txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaTotal += distanciaRecorrida
                                cilindro = 0
                            indice += 1
                            print('numero de indice: ', indice)
                            if indice < cantListas:
                                listaAux = listaDeListas[indice]
                            finPrimerScan = True
                            listaVuelta = []
                            creciente = True
                            #Fin de algoritmo Decreciente...
            else:
                #Comienza algoritmo scan descreciente
                print("Comienza en decreciente")
                finPrimerScan = True
                decreciente = True
                for i in range(cantListas):
                    if decreciente:
                        while (finPrimerScan):
                            candidato = self.buscarMenorDistanciaDecrecienteScanAux(listaAux, cilindro, listaVuelta)
                            distanciaRecorrida = cilindro - candidato
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            distanciaTotal += distanciaRecorrida
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            cilindro = candidato
                            if candidato in listaAux:
                                listaAux.remove(candidato)
                            if (len(listaAux) == 0):
                                finPrimerScan = False
                        #Hice el primer scaneo, ahora veo si no llegue al principio  para ir hasta el
                        if (cilindro != 0):
                            distanciaRecorrida = cilindro 
                            txt = str(cilindro) + "  -  " + '0' + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = 0
                        #Ahora doy la vuelta y vuelvo en sentido contrario
                        contador = 0
                        tamanio = len(listaVuelta)
                        while contador != tamanio:
                            candidato = self.buscarMenorDistanciaCrecienteScanAux(cilindro, listaVuelta)
                            distanciaRecorrida = cilindro - candidato
                            distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            distanciaTotal += distanciaRecorrida
                            #Si se movio entonces sumamos uno a cant movimientos
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaRecorrida = 0
                            contador += 1
                            cilindro = candidato
                            if candidato in listaVuelta:
                                listaVuelta.remove(candidato)
                        #Compruebo si llega al final, sino hago que valla.
                        if (cilindro != disco.totalPistas) and (cilindro != 0):
                            distanciaRecorrida = cilindro - disco.totalPistas
                            distanciaRecorrida = distanciaRecorrida * -1
                            txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                            print (txt)
                            datos.append(txt)
                            if distanciaRecorrida != 0:
                                cantMovimientos += 1
                            distanciaTotal += distanciaRecorrida
                            cilindro = disco.totalPistas
                        if (cilindro == 0):
                            decreciente = False
                        #Fin de algoritmo decreciente...
                        indice += 1
                        if indice < cantListas:
                            listaAux = listaDeListas[indice]
                        finPrimerScan = True
                        listaVuelta = []
                    else:
                        #Comienza a recorrer en creciente
                        if listaAux:
                            while (finPrimerScan):
                                candidato = self.buscarMenorDistanciaCrecienteScan(listaAux, cilindro, listaVuelta, disco)
                                distanciaRecorrida = (cilindro - candidato) * -1
                                txt = str(cilindro) + "  -  " + str(candidato) + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                distanciaTotal += distanciaRecorrida
                                #Si se movio entonces sumamos uno a cant movimientos
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaRecorrida = 0
                                contador += 1
                                cilindro = candidato
                                if candidato in listaAux:
                                    listaAux.remove(candidato)
                                if (len(listaAux) == 0):
                                    finPrimerScan = False
                            #Hice el primer scaneo, ahora veo si no llegue al final para ir hasta el
                            if (cilindro != disco.totalPistas):
                                distanciaRecorrida = (cilindro - disco.totalPistas ) * -1
                                txt = str(cilindro) + "  -  " + str(disco.totalPistas) + "  =  " + str(distanciaRecorrida) + '\n'
                                print (txt)
                                datos.append(txt)
                                if distanciaRecorrida != 0:
                                    cantMovimientos += 1
                                distanciaTotal += distanciaRecorrida
                                cilindro = disco.totalPistas
                            indice += 1
                            if indice < cantListas:
                                listaAux = listaDeListas[indice]
                            finPrimerScan = True
                            listaVuelta = []
                            decreciente = True
                            #Fin de algoritmo Decreciente...

            distanciaRec = 'Distancia recorridda total: '+ str(distanciaTotal) + '\n'
            print (distanciaRec)
            datos.append(distanciaRec)
            retardoR = 'Retardo rotacional: '+ str(self.getRetardoRotacional(disco.velocidadRotacion))+ 'ms' + '\n'
            datos.append(retardoR)
            print (retardoR)
            tiempoTra = 'Tiempo de transferencia: '+ str(self.getTiempoTransferencia(disco.tamañoBloque,disco.velocidadRotacion)) + 'ms' + '\n'
            datos.append(tiempoTra)
            print (tiempoTra)
            cantM = 'Cantidad de movimientos: ' + str(cantMovimientos) + '\n'
            datos.append(cantM)
            print (cantM)
            tiempoAT = 'Tiempo acceso total: ' + str(self.getTiempoAccesoTotal(cantMovimientos, disco, listaAux)) + 'ms' + '\n'
            datos.append(tiempoAT)
            print (tiempoAT)

        else:
            txt = ('NO SE PUEDE SIMULAR. HAY UN REQUERIMIENTO EN LA LISTA MAYOR AL TOTAL DE PISTAS ')
            datos.append(txt)
            print (txt)
        return datos
        


    