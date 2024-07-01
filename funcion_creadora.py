from funciones_cesar import encriptador_char

def creador_funciones_encriptador_cesar(clave:int):

  def encriptador_cesar_fijo(mensaje:str)-> str:
    mensaje_encriptado: str = ''
    for char in mensaje:
      mensaje_encriptado += encriptador_char(char, clave)

    return mensaje_encriptado
  return encriptador_cesar_fijo