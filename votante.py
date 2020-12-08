from persona import Persona

class Votante(Persona):
  def __init__(self,nombre, apellido, dni, fechaNac, direccion, voto):
    Persona.__init__(self, nombre, apellido, dni, fechaNac, direccion)
    self.voto = voto 

  def __str__(self):
      return ('NOMBRE: {} \n' 'APELLIDO: {} \n' 'DNI: {} \n' 'FECHANAC: {} \n' 'DIRECCION: {} ' 'VOTO {} ' '\n'.format(
         self.nombre, 
         self.apellido, 
         self.dni ,
         self.fechaNac,
         self.direccion,
         self.voto
         )
      )
