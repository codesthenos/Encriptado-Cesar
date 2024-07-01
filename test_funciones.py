from constante_ABC import ABC
from funciones_cesar import *
from funcion_encriptador_cesar import encriptador_cesar
from funciones_creadoras import creador_funciones_encriptador_cesar, creador_par_cesar

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
  assert encriptador_cesar('hola', -33) == 'CKGW'
  assert encriptador_cesar('', -56) == ''
  assert encriptador_cesar('', 0) == ''
  assert encriptador_cesar('', 33) == ''
  assert encriptador_cesar('Hola, mundo!', -56) == 'HOLA, MUNDO!'
  assert encriptador_cesar('Hola, mundo!', 0) == 'HOLA, MUNDO!'
  assert encriptador_cesar('Hola, mundo!', -30) == 'FNJZ,YKSLBN!'
  assert encriptador_cesar('Hola, mundo!', 30) == 'JQNC,BÑWOFQ!'
  assert encriptador_cesar('Hola, mundo!', 5) == 'MTPF,EQZRIT!'

def test_creador_funciones_cesar():

  assert creador_funciones_encriptador_cesar(5)('hola, mundo!') == 'MTPF,EQZRIT!'

def test_creador_de_pares():

  clave = 5
  mensaje = 'hola, mundo!'
  encriptador_5 = creador_par_cesar(clave)[0]
  desencriptador_5 = creador_par_cesar(clave)[1]

  assert encriptador_5(mensaje) == 'MTPF,EQZRIT!'
  assert desencriptador_5(mensaje) == 'HOLA, MUNDO!'