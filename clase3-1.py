#programar en python q  utizan listas 

semana_laboral=["lunes","martes","miercoles","jueves","viernes"]
print("semana laboral ",semana_laboral)

print("Dia 1: ", semana_laboral[4]) #   imprime la posisio 4 que es el viernes recuerda que se inicia en 0

semana_laboral[4]="sabado " # se remplazo la posicion 4 que viene siendo viernes y se cambio por sabado 
print("semana laboral=", semana_laboral)

semana_laboral[4]="viernes " 
print("semana laboral=", semana_laboral)

longitud_lista=len(semana_laboral)  ## sirve para ver la longitud de  la lista 
print("la longitud de la lista es de: ", longitud_lista)  

pocision=semana_laboral.index("miercoles") ##.index sirve parqa ver la posicion de la lista de un elemto
print("la posision de la semana es :", pocision)

semana_laboral.append("sabado")  ## append sirve para agreegar un elemto a lista
print("semana laborarl: ", semana_laboral)

del semana_laboral[4]  ## elimina "del" el elemto en la posicion 4
print("semana laboral: ", semana_laboral)
