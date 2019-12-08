import os
import re

class Archivo():

   def leer(self, path):
      lista = []
      archivo = open(path, "r")
      arch1 = archivo.readlines()
      for numero in arch1:
         numero_tanda=int(numero)  
         lista.append(numero_tanda)
      archivo.close()
      return lista

   def escribir(self, nombre, datos):

      archivo = open(nombre+".txt", "w")
      for linea in datos:
         print(linea)
         archivo.write(linea)
      
      archivo.close()
      pass

if __name__ == "__main__":
   A = Archivo()
   print(A.leer('archivo1'))
   
