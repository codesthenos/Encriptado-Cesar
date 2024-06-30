from constante_ABC import ABC
from funciones_cesar import *

def test_validador_char():

  assert validador_char('a') == True
  assert validador_char(' ') == True
  assert validador_char('!') == False

def test_validador_clave():

  assert modulador_clave(5) == 5
  assert modulador_clave(-5) == -5
  assert modulador_clave(28) == 0
  assert modulador_clave(33) == 5
  assert modulador_clave(-33) == -5

def test_encriptador_char():

  assert encriptador_char('z', 2) == ('A')
  assert encriptador_char('a', -2) == ('Z')
  assert encriptador_char('h', 56) == ('H')
  assert encriptador_char('h', -56) == ('H')
  assert encriptador_char('h', 0) == ('H')
  assert encriptador_char('h', 57) == ('I')
  assert encriptador_char('h', -57) == ('G')
  assert encriptador_char(' ', -57) == ('Z')
  assert encriptador_char('!', -57) == ('!')
  assert encriptador_char('a', -57) == (' ')
  assert encriptador_char('a', -60) == ('X')

def test_encriptador_cesar():

  assert encriptador_cesar('hola', 56) == 'HOLA'
  assert encriptador_cesar('hola', 0) == 'HOLA'
  assert encriptador_cesar('hola', -33) == 'ESIÑ'
  assert encriptador_cesar('', -56) == ''
  assert encriptador_cesar('', 0) == ''
  assert encriptador_cesar('', 33) == ''
  assert encriptador_cesar('Hola, mundo!', -56) == 'HOLA, MUNDO'
  assert encriptador_cesar('Hola, mundo!', 0) == 'HOLA, MUNDO!'
  assert encriptador_cesar('Hola, mundo!', 30) == 'LSND, ÑYSÑH'