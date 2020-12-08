from persona import Persona
from distrito import Distrito
from cargo import Cargo
from lista import Lista


class Candidato(Persona):
  def __init__(self, nombre, apellido, duracion, cargo, lista, partidoPolitico, departamento, provincia):
    Persona.__init__(self, nombre, apellido, dni = None, fechaNac = None, direccion= None)
    self.cargo = Cargo (duracion,cargo)
    self.lista = Lista (lista, partidoPolitico)
    self.distrito = Distrito (departamento, provincia)

  def __str__(self):
    return ('NOMBRE: {}\n APELLIDO: {}\n CARGO:  {}\n LISTA: {}\n DISTRITO: {}\n PROVINCIA {}\n' .format(
      self.nombre, 
      self.apellido, 
      self.cargo.cargo,
      self.lista.lista,
      self.distrito.departamento,
      self.distrito.provincia
    )
  )


norma = Candidato (
 nombre = 'Norma ',
 apellido = 'Trigo ',
 duracion = 4 ,
 cargo = 'Intendente ',
 lista = 300,
 partidoPolitico = 'Frente Cambia Mendoza ',
 departamento = 'Santa Rosa',
 provincia = 'Mendoza')

celso = Candidato (
  nombre = 'Celso ', 
  apellido = 'Reta ',
  duracion = 4 ,
  cargo = 'Intendente ',
  lista = 302 ,
  partidoPolitico = 'Frente Elegí Mendoza ',
  departamento = 'Santa Rosa',
  provincia = 'Mendoza')


marcelo = Candidato (
  nombre = 'Marcelo ',
  apellido = 'Gómez ',
  duracion = 4 ,
  cargo = 'Intendente ',
  lista = 222 ,
  partidoPolitico = 'Protectora Fuerza Politica ',
  departamento = 'Santa Rosa',
  provincia = 'Mendoza')


juan = Candidato (
  nombre = 'Juan carlos Antonio ',
  apellido = 'Vegas ',
  duracion = 4,
  cargo = 'Intendente ',
  lista =6 ,
  partidoPolitico = 'Partido intransigente ',
  departamento = 'Santa Rosa',
  provincia = 'Mendoza')
