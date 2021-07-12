import random
import json

def leerlista(texto):
  return input(texto).split()

def muestralista(lista):
  p = ''
  c = ''
  for elemento in lista:
    p += c + str(elemento)
    c = ' '
  return p

def solucion(lista, diccionario):
  puntos = 0
  sirven = []
  for i in range(len(lista)):
    if(lista[i] in diccionario):
      sirven.append(lista[i])
      puntos += diccionario[lista[i]]
  return puntos, sirven

def main():
  json_string = input()
  diccionario = json.loads(json_string)
  lista = leerlista('')
  puntos,sirven = solucion(lista, diccionario)
  print(puntos)
  print(muestralista(sirven))

# Para ver como funciona el reto
main()
