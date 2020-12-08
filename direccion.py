class Direccion:
  def __init__(self, numero, calle, barrio, distrito):
    self.numero = numero
    self.calle = calle
    self.barrio = barrio
    self.distrito = distrito

  def __str__(self):
      return str('NUMERO: {} \n' 'CALLE: {}\n' 'BARRIO: {}\n' 'DISTRITO: {} \n'.format(
         self.numero, 
         self.calle, 
         self.barrio ,
         self.distrito ,
         )
      )


DIRECCION = Direccion (
  numero=666, 
  calle='Hipolito Yrigoyen ', 
  barrio='La dormida ', 
  distrito='Santa Rosa')

Direccion (
  numero=661, 
  calle='Fray Luis Beltrán ', 
  barrio=' La Josefa ', 
  distrito='Santa Rosa ')

Direccion (
  numero=1012, 
  calle='Ruta Provincial 50 Km ', 
  barrio=' Barrio 12 De Octubre', 
  distrito='Santa Rosa ')

Direccion (
  numero=662, 
  calle='Molina Cabrera ', 
  barrio='Barrio Molina Cabrera',
  distrito='Santa Rosa ')

Direccion (
  numero=985, 
  calle='Los Lotes Ruta Prov. 50- Km ', 
  barrio='Los Lotes', 
  distrito='Santa Rosa')


Direccion (
  numero=659, 
  calle='El Sosnead ', 
  barrio=' ', 
  distrito='Santa Rosa')
