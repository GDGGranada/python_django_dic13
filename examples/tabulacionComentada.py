def malTabulado():
	#Todo lo que tenga una tabulacion pertenece a esta funcion
	print "Yo estoy bien tabulado"

	
print "Yo la estoy liando parda"
	print"Yo estoy bien tabulado"
	
	
malTabulado()

''' ¿Por qué este programa no funciona?, veamoslo tranquilamente
En primer logar tenemos la definicion de una funcion, entonces, todo lo que 
este tabulado por debajo pertenecera a esa funcion

En la línea 6 aparece un print sin tabulacion, cosa que no seria mala si la funcion terminara
en el primer print.

Sin embargo en la linea 7 tenemos otro print con tabulacion. Python no sabe interpretar a que
bloque pertenece y nos lanza un error de indentacion'''

