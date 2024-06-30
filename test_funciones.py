from funciones_cesar import *

def test_suma():

  assert suma(5, 7) == 25
  assert suma(-5, 8) == 25
  assert suma(0, 0) == 25
  assert suma(4, -5) == -1 # suma(4, -5) es 25 por lo que el test aqui casca