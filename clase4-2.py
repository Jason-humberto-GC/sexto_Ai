#expresiones regulares

import re #importar el modulo de expresiones regulares
carpeta="documentos\\"
archivo="hola.txt"

with open (carpeta+archivo,"r") as  archivo:
    texto=archivo.read()
    
expresion_regular=re.compile(r"apellido") #compilar la expresion regular la funcion compile() sirve para compilar la expresion regular
#resultado_busqueda=expresion_regular.search(texto) #buscar la expresion regular en el texto
resultado_busqueda=expresion_regular.finditer(texto) #finditer sirve para buscar todas las coincidencias de la expresion regular en el texto

#print(resultado_busqueda.group(0)) #imprimir el resultado de la busqueda group(0) sirve para imprimir el resultado de la busqueda solo sirve para search

for resultado in resultado_busqueda: # sirve para el finditer
    print(resultado.group(0))