from fecha import Fecha
from candidato import norma,celso,marcelo,juan
from voto import Voto
from votante import Votante
from random import randint, choice
from direccion import DIRECCION


NOMBRES = ['Daiana ', 'Gustavo ', 'Lorena ', 'Alejandro ', 'Mónica ', 'Ramiro ', 'Johanna ', 'Abel ', 'Ivana ', 'Cristian ',
'Rocio ', 'Camilo ', 'Martina ', 'Ignacio ', 'Daniela ', 'Gabriel ', 'Gastón ', 'Ana ', 'Agusto ','Ulises ']

APELLIDOS = ['Chaves ', 'Gatica ', 'Horn ', 'Roby', 'Fernández ', 'Ahumada ', 'Ferrer ', 'Bernal', 'Mendez ','Brondo ', 'Messi ', 'Castro ', 'López ', 'Páez ', 'Cerati ', 'Barbaroja ', 'Anzorena ', 'Álvarez ','Barrera ', 'Delatorre ']

DNI = [34134302, 3245678, 33165487, 30654321, 31687123, 27846123, 25658741, 24465321, 38764132, 20563214, 33851236,28745132, 32658741, 34632187, 25874136, 34125863, 25874163, 36258741, 36251478, 25874236]




def generar_fechaNac():
  return Fecha(
    dia=randint(1, 30),
    mes=randint(1, 12),
    anio=randint(1950, 2002)
  )

DIRECCION = [DIRECCION]



def generadorVotantes (cantidad):
  votantes = []
  for idx in range(cantidad):
    idx_nombres = randint (0,len(NOMBRES)-1)
    idx_apellidos = randint (0,len(APELLIDOS)-1)
    idx_dni = randint (0,len(DNI)-1)
    generar_fechaNac()
    idx_direccion = randint (0,len(DIRECCION)-1)
    voto = generar_voto()
    votante =Votante(NOMBRES [ idx_nombres] , APELLIDOS[ idx_apellidos] ,  DNI [ idx_dni] , generar_fechaNac() , DIRECCION[ idx_direccion] , voto )
    votantes.append (votante)
  return votantes


CANDIDATOS= [norma,celso,marcelo,juan]

def generar_voto():

  tipo_voto = choice([0]*89 + [1]*10 + [2]*1) 
  idx_candidatos = choice ([norma]*45 + [celso]*35 + [marcelo]*20+ [juan]*10)
 
  voto = Voto(None,False,False,False)
  
  if tipo_voto == 0:
    voto.candidato = idx_candidatos
    voto.isValido = True
  elif tipo_voto == 1: 
    voto.isBlanco = True
  else:
    voto.isImpugnado = True
  return voto
