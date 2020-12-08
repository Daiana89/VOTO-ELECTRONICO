
class Persona:

  def __init__(self, nombre, apellido, dni, fechaNac, direccion):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.fechaNac = fechaNac
    self.direccion = direccion 
    

  def __str__(self):
      return ('nombre: {}' 'apellido: {}' 'dni: {}' 'fechaNac: {}' 'numero: {}' 'calle: {} ' 'barrio: {}' ' distrito: {}'.format(
         self.nombre, 
         self.apellido, 
         self.dni ,
         self.fechaNac,
         self.direccion.numero,
         self.direccion.calle,
         self.direccion.barrio,
         self.direccion.distrito,


         )
      )