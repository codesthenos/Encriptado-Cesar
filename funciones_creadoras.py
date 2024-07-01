from funciones_cesar import encriptador_char

def creador_funciones_encriptador_cesar(clave:int):

  def encriptador_cesar_fijo(mensaje:str)-> str:
    mensaje_encriptado: str = ''
    for char in mensaje:
      mensaje_encriptado += encriptador_char(char, clave)

    return mensaje_encriptado
  return encriptador_cesar_fijo

def creador_par_cesar(clave: int)->tuple:

  def encriptador_cesar(mensaje:str)-> str:
    mensaje_encriptado: str = ''
    for char in mensaje:
      mensaje_encriptado += encriptador_char(char, clave)

    return mensaje_encriptado

  def desencriptador_cesar(mensaje:str)-> str:
    mensaje_encriptado: str = encriptador_cesar(mensaje)
    mensaje_desencriptado: str = ''
    for char in mensaje_encriptado:
      mensaje_desencriptado += encriptador_char(char, -clave)

    return mensaje_desencriptado 

  return (encriptador_cesar, desencriptador_cesar)