import config.constantes

class Pessoa:
  def __init__(self, nome="", idade=0):
    self.nome = nome
    if idade > config.constantes.IDADE_MAXIMA:
      self.idade = config.constantes.IDADE_MAXIMA
    else:
      self.idade = idade
  def __str__(self):
    return f'''
    Nome: {self.nome},
    idade: {self.idade}
    '''


joao = Pessoa("João", 70)
maria = Pessoa("Maria", 130)
print(joao, maria)
