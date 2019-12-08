from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

from algoritmos import Algoritmo
from archivo import Archivo
from disco import Disco


window = Tk() 
# mainFrame = Frame(master=window)
window.title("Integrador de discos")
window.geometry('800x300')
window.filename =  filedialog.askopenfilename(initialdir = "/",title = "SELECCIONAR TANDA",filetypes = (("Txt files","*.txt"),("all files","*.*")))
window.after(1, lambda: window.focus_force())
frameCrl = Frame(window)
frameCrl.pack( side = TOP )

lblTiempos = Label(frameCrl, text=" DISCO", justify=LEFT)
lblTiempos.grid(column=0, row=0) 

lblSeekTime = Label(frameCrl, text=" SeekTime:") 
lblSeekTime.grid(column=0, row=1) 
txtSeekTime = Entry(frameCrl, width=10)
txtSeekTime.grid(column=1, row=1) 

lblVelocidadRotacion = Label(frameCrl, text=" Velocidad Rotacion:") 
lblVelocidadRotacion.grid(column=0, row=2) 
txtVelocidadRotacion = Entry(frameCrl, width=10)
txtVelocidadRotacion.grid(column=1, row=2)

lblTiempoTransferencia = Label(frameCrl, text=" Tiempo Transferencia:") 
lblTiempoTransferencia.grid(column=0, row=3) 
txtTiempoTransferencia = Entry(frameCrl, width=10)
txtTiempoTransferencia.grid(column=1, row=3)

lblTamañoBloque = Label(frameCrl, text=" Tamaño 1 bloque:") 
lblTamañoBloque.grid(column=0, row=4) 
txtTamañoBloque = Entry(frameCrl, width=10)
txtTamañoBloque.grid(column=1, row=4)

lblTotalPistas = Label(frameCrl, text=" Total de pistas:") 
lblTotalPistas.grid(column=0, row=5) 
txtTotalPistas = Entry(frameCrl, width=10)
txtTotalPistas.grid(column=1, row=5)   

lblPosicionCabeza = Label(frameCrl, text=" Posicion cabeza:") 
lblPosicionCabeza.grid(column=0, row=6) 
txtPosicionCabeza  = Entry(frameCrl, width=10)
txtPosicionCabeza.grid(column=1, row=6)

lblSentido = Label(frameCrl, text=" Creciente: C  Decreciente: D:") 
lblSentido.grid(column=0, row=7) 
txtSentido = Entry(frameCrl, width=10)
txtSentido.grid(column=1, row=7) 

lblPrimerosRequerimientos = Label(frameCrl, text="Primeros requerimientos en ser atendido (SOLO PARA FSCAN)") 
lblPrimerosRequerimientos.grid(column=0, row=8) 
txtPrimerosRequerimientos = Entry(frameCrl, width=10)
txtPrimerosRequerimientos.grid(column=1, row=8)

lblCantN = Label(frameCrl, text=" Ingrese N para N-STEP-SCAN ") 
lblCantN.grid(column=0, row=9) 
txtCantN = Entry(frameCrl, width=10)
txtCantN.grid(column=1, row=9) 

lblTliberacion = Label(frameCrl, text="ALGORITMO:", justify=LEFT)
lblTliberacion.grid(column=8, row=0) 

selected = StringVar()
selected.set('fifo')
rad1 = Radiobutton(frameCrl,text='scan', value='scan', variable=selected, width=10) 
rad1.grid(column=8, row=1)
rad2 = Radiobutton(frameCrl,text='c-scan', value='cscan', variable=selected, width=10) 
rad2.grid(column=8, row=2)
rad3 = Radiobutton(frameCrl,text='look', value='look', variable=selected, width=10)
rad3.grid(column=8, row=3)
rad4 = Radiobutton(frameCrl,text='clook', value='clook', variable=selected, width=10)
rad4.grid(column=8, row=4)
rad5 = Radiobutton(frameCrl,text='fifo', value='fifo', variable=selected, width=10)
rad5.grid(column=8, row=5)
rad6 = Radiobutton(frameCrl,text='sstf', value='sstf', variable=selected, width=10)
rad6.grid(column=8, row=6)
rad7 = Radiobutton(frameCrl,text='fscan', value='fscan', variable=selected, width=10)
rad7.grid(column=8, row=7)
rad8 = Radiobutton(frameCrl,text='nsteepscan', value='nsteepscan', variable=selected, width=10)
rad8.grid(column=8, row=8)

def clicked(): 
    # Obtengo el archivo con la lista de procesos
    lista = Archivo().leer(window.filename)
    #Obtengo el SeekTime
    seekTime = txtSeekTime.get()
    #Algoritmo a utilizar
    algoritmo = selected.get()
    # Velocidad de rotacion
    velocidadRotacion = txtVelocidadRotacion.get()
    # Tiempo de transferencia
    tiempoTransferencia = txtTiempoTransferencia.get()
    # Tamaño de 1 bloque
    tamañoBloque = txtTamañoBloque.get()
    # Total pistas
    totalPistas = txtTotalPistas.get()
    # Posicion de la cabeza en un principio
    posicionCabeza = txtPosicionCabeza.get()
    # Sentido en el que va el disco
    sentido = txtSentido.get()
    #Obtengo la cant de los primeros en atenderse para FSCAN
    primerosRequerimientos = txtPrimerosRequerimientos.get()
    #Obtengo el n de N-STEEP-SCAN
    n = txtCantN.get()
    #Creo un disco
    disco = Disco(int(seekTime),
                int(velocidadRotacion),
                int(tiempoTransferencia),
                int(tamañoBloque),
                int(totalPistas),
                int(posicionCabeza),
                sentido)
    
    # Simulacion de algoritmo 
    alg = Algoritmo()
    if algoritmo == 'fifo':
       datosAlgoritmo = alg.fifo(disco, lista)
    if algoritmo == 'sstf':
       datosAlgoritmo = alg.sstf(disco, lista)
    if algoritmo == 'scan':
        datosAlgoritmo = alg.scan(disco, lista)
    if algoritmo == 'cscan':
        datosAlgoritmo = alg.cscan(disco, lista)
    if algoritmo == 'look':
        datosAlgoritmo = alg.look(disco, lista)
    if algoritmo == 'clook':
        datosAlgoritmo = alg.clook(disco, lista)
    if algoritmo == 'fscan':
        datosAlgoritmo = alg.fscan(disco, lista, int(primerosRequerimientos))
    if algoritmo == 'nsteepscan':
        datosAlgoritmo = alg.nsteepscan(disco, lista, int(n))

    Archivo().escribir('datosAlgoritmo', datosAlgoritmo)


Label(frameCrl, text="", justify=CENTER, width=10).grid(column=11, row=0)   
   
btn = Button(frameCrl, text="Comenzar simulacion", command=clicked)
btn.grid(column=12, row=2)



window.mainloop()
###   Fin Grafica    ###