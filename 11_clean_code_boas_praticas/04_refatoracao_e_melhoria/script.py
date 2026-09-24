def calc(a,b):
  return a+b


def calcular_soma(numero1, numero2):
  return numero1+numero2


def processar(lista):
  resultado = []
  for i in lista:
    if i > 10:
      resultado.append(i*2)
    return resultado


def processar_numeros(lista):
  return [numero * 2 for numero in lista if numero > 10]



# código complexo

def processar(lista):
  return [x*2 for x in lista if x > 10]



