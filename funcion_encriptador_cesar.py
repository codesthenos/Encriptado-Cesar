from funciones_cesar import encriptador_char

def encriptador_cesar(mensaje:str, clave:int)-> str:
  mensaje_encriptado: str = ''
  for char in mensaje:
    mensaje_encriptado += encriptador_char(char, clave)

  return mensaje_encriptado