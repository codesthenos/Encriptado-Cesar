from constante_ABC import ABC

def validador_char(char: str)-> str:
  is_valid_char:bool = False

  if char.upper() in ABC:
      is_valid_char = True

  return is_valid_char

def modulador_clave(clave: int)-> int:
  clave_modulada: int = clave
  clave_absoluta: int = abs(clave)

  if clave_absoluta >= len(ABC):
    clave_modulada = clave_absoluta % len(ABC)
    if clave < 0:
      clave_modulada = -clave_modulada

  return clave_modulada

def encriptador_char(char: str, clave: int)-> str:
  char_encriptado: str = char

  if validador_char(char):
      indice_char: int = ABC.index(char.upper())
      clave_modulada = modulador_clave(clave)
      nuevo_indice: int = indice_char + clave_modulada
      
      if nuevo_indice >= len(ABC):
        nuevo_indice = nuevo_indice - len(ABC)
      elif nuevo_indice < 0:
        nuevo_indice = nuevo_indice + len(ABC)
      
      char_encriptado = ABC[nuevo_indice]

  return char_encriptado