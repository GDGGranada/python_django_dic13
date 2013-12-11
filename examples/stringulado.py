cadena="Hola amiwitos, gracias por venir"
print cadena

print cadena.upper() # Pasa el string a mayusculas
print len(cadena) # Imprime la longitud de la cadena

print cadena[1] # Imprime el caracter en la posicion 2
print cadena[:-8] # Imprime todos los caracteres excepto los 8 ultimos
print cadena[8:-3] # Imprime desde el noveno hasta los 3 ultimos
cadena = cadena + " Que bien lo vamos a pasar" # Concatena dos cadenas 
print cadena

cadena = cadena + 8  #Concatena cadena y numero (nocivo)
#cadena = cadena + str(8.23)  #Concatena cadena y numero (bueno)
print cadena