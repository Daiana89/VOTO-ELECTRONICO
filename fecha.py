class Fecha:

  def __init__(self, dia, mes, anio):
    self.dia = dia
    self.mes = mes
    self.anio = anio

  def __str__(self):
    return '{}/{}/{}'.format(
      self.dia, 
      self.mes,       
      self.anio,
    )