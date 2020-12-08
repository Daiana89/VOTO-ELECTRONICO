from generadorvotantes import generadorVotantes
from candidato import norma, celso, marcelo,juan


def main():

	resultados = generadorVotantes(500)
	contBlancos = 0
	contValidos = 0
	contImpugnado = 0
	contNorma = 0
	contCelso = 0
	contMarcelo = 0
	contJuan = 0


	for item in resultados:
		print('VOTANTE: {}'.format(item))
	for i in resultados:
		if i.voto.isBlanco == True:
			contBlancos += 1
		if i.voto.isValido == True:
			contValidos += 1
		if i.voto.isImpugnado == True:
			contImpugnado += 1
		if i.voto.candidato == norma:
			contNorma += 1
		if i.voto.candidato == celso:
			contCelso += 1
		if i.voto.candidato == marcelo:
			contMarcelo += 1
		if i.voto.candidato == juan:
			contJuan += 1


	contValidos = contValidos * 100 / 500
	contBlancos = contBlancos * 100 / 500
	contImpugnado = contImpugnado * 100 / 500
	contNorma = contNorma * 100 / 500
	contCelso = contCelso * 100 / 500
	contMarcelo = contMarcelo * 100 / 500
	contJuan = contJuan * 100 / 500

	

	print('LOS RESULTADOS DE LOS VOTOS SON:  \n*Blancos {}%  \n*Válidos {}%  \n*Impugnados {}%'.format(
	   contBlancos, contValidos, contImpugnado, end=" "))

	print('RESULTADO DE LOS CANDIDATOS:\n'	

 '* Candidato Trigo Norma tiene {}%\n'
	
	'* Candidato Reta Celso tiene {}%\n'
  
	'* Candidato Gómez Marcelo Fernando tiene {}%\n'
  
	'* Candidato Vegas Juan Carlos Antonio tiene {}%'.format(contNorma, contCelso, contMarcelo, contJuan))

  



	if contNorma > 40:
		print('EL CANDIDATO GANADOR ES:\n*** Trigo Norma*** \n CON UN: ' + str(contNorma) + '%')

	else:
		print(
		    'SEGUNDA VUELTA,entre: \n* Trigo Norma  \n* Reta Celso  \n CON UN:  {}%  y   {}% '
		    .format(contNorma, contCelso))


if __name__ == '__main__':
	main()
