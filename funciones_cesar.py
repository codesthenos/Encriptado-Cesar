from constante_ABC import ABC

def encriptardor_char(char: str, clave: int)-> str:
  char_encriptado: str = ''
  if char.upper() in ABC and char != ' ':
      indice_char: int = ABC.index(char.upper())
      char_encriptado = ABC[indice_char+clave]
  else:
    char_encriptado = char
  return char_encriptado

def encriptador_cesar(mensaje: str, clave: int)-> str:
  mensaje_encriptado: str = ''
  for char in mensaje:
    if char in ABC and char != ' ':
      mensaje_encriptado += encriptardor_char(char, clave)
    else:
      mensaje_encriptado += char
  return mensaje_encriptado.upper()
print(encriptador_cesar('Hola', 0))
print(len(ABC))