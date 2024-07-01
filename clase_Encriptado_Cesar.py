from funcion_encriptador_cesar import encriptador_cesar

class Encriptado_Cesar():

  def __init__(self, mensaje:str='hola, mundo!', clave:int=77):
    self.mensaje = mensaje
    self.clave = clave
    self.mensaje_encriptado = self.encriptar_mensaje()
    self.mensaje_desencriptado = self.desencriptar_mensaje()

  def __str__(self):
    return f'El mensaje a encriptar es "{self.mensaje}"\nLa clave Cesar es "{self.clave}"\nEl mensaje encriptado es "{self.mensaje_encriptado}"\nEl mensaje desencriptado es "{self.mensaje_desencriptado}"'

  def __repr__(self):
    return self.__str__()

  def encriptar_mensaje(self):
    return encriptador_cesar(self.mensaje, self.clave)
  
  def desencriptar_mensaje(self):
    return encriptador_cesar(self.mensaje_encriptado, -self.clave)
  
print(Encriptado_Cesar())