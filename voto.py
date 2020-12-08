class Voto:
  def __init__(self, candidato, isBlanco, isImpugnado,isValido):
    self.candidato = candidato
    self.isBlanco = isBlanco
    self.isImpugnado =isImpugnado
    self.isValido = isValido

  def __str__(self):
      return str('CANDIDATO: {} \n ES BLANCO: {}\n ES IMPUGANDO : {} \n ES VALIDO: {}\n '.format(
         self.candidato, 
         self.isBlanco, 
         self.isImpugnado ,
         self.isValido ,
         )
      )

