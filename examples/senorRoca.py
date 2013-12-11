
def senorRoca(jugador1, jugador2):

	print "Jugador 1 saco %s Jugador 2 saco %s" % (jugador1,jugador2)
	if (jugador1=='piedra'):
		if (jugador2=='piedra'):
			print "Empatan con piedra"
		elif (jugador2=='papel'):
			print "El jugador 2 hace la envolvente y gana"
		elif (jugador2=='tijera'):
			print "Jugador 1 machaca las tijeras"
		else:
			print "Un helicoptero apache os arrasa a todos por culpa del jug 2"
	
	elif (jugador1=='papel'):
		if (jugador2=='piedra'):
			print "El jugador 1 hace la envolvente y gana"
		elif (jugador2=='papel'):
			print "Tanto papel y aqui sin tabaco . . . "
		elif (jugador2=='tijera'):
			print "Jugador 2 recorta el papel"
		else:
			print "Jugador2 no es dificil, solo piedra papel o tijera"
			
	elif (jugador1=='tijera'):
		if (jugador2=='piedra'):
			print "Jugador 2 baila sobre tus cenizas"
		elif (jugador2=='papel'):
			print "Jugador 1 recorta el papel"
		elif (jugador2=='tijera'):
			print "Choque de tijeras, ni para ti ni para mi"
		else:
			print "ASdfajhalsdgashdglahsf"
	else:
		print 'Parad ya de liarla no?'


		
		
def rocaMalvada(jugador1,jugador2):
	print "Jugador 1 saco %s Jugador 2 saco %s" % (jugador1,jugador2)
	
	if (jugador1!='piedra' and jugador1!='papel' and jugador1!='tijera'):
		return "No hagas caso al 1 que el pobre no da mas"
	if (not jugador2=='piedra' and not jugador2=='papel' and not jugador2=='tijera'):
		return "No hagas caso al 2 que el pobre no da mas"
	
	if (jugador1=='piedra' and (jugador2=='piedra' or jugador2=='tijera')):
		return "El jugador 2 no gana"
	elif (jugador1=='papel' and (jugador2=='papel' or jugador2=='piedra')):
		return "El jugador 2 no gana"
	elif (jugador1=='tijera' and (jugador2=='papel' or jugador2=='tijera')):
		return "El jugador 2 no gana"

		
jugador1="piedra"
jugador2="tijera"		
senorRoca(jugador1,jugador2)

print rocaMalvada(jugador1,jugador2)
