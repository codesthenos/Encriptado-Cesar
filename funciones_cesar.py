ABC = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")

def encriptador_cesar(mensaje: str, clave: int)-> str:
  mensaje_encriptado: str = ''
  for char in mensaje:
    mensaje_encriptado += char
  return mensaje_encriptado.upper()
print(encriptador_cesar('Hola', 0))
print(len(ABC))