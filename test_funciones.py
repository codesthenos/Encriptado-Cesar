from funciones_cesar import *

def test_encriptador_char():

  assert encriptardor_char('h', 56) == ('H')
  assert encriptardor_char('h', -56) == ('H')
  assert encriptardor_char('h', 0) == ('H')
  assert encriptardor_char('h', 57) == ('I')
  assert encriptardor_char('h', -57) == ('G')
  assert encriptardor_char(' ', -57) == (' ')
  assert encriptardor_char('!', -57) == ('!')

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