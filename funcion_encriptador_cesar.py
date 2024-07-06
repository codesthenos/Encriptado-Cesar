from funciones_cesar import encriptador_char

def encriptador_cesar(mensaje:str, clave:int)-> str:
  mensaje_encriptado: str = ''
  for char in mensaje:
    mensaje_encriptado += encriptador_char(char, clave)

  return mensaje_encriptado

def encriptador_cesar_map(mensaje, clave):
  return ''.join(list(map(lambda x: encriptador_char(x, clave), mensaje)))
