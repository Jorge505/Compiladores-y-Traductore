class Automata:
  def __init__(self,cadena):
    self.cadena=cadena

  def NumeroBinarios(self):
    self.estado=0
    for i in range(0,len(self.cadena)):
      self.transicion=self.cadena[i]
#Estado inicial
      if self.estado == 0:
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado=2
          elif self.transicion == '0':
             self.estado=1
          else:
            return False
        else:
            return False
#Estado 1
      elif self.estado==1:
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado=0
          elif self.transicion == '0':
             self.estado=3
          else:
            return False
        else:
            return False
#Estado 2
      elif self.estado==2:
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado=0
          elif self.transicion == '0':
             self.estado=3
          else:
            return False
        else:
            return False
#Estado 3
      elif self.estado==3:
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado=4
          else:
            return False
        else:
            return False
#Estado 4
      elif self.estado==4:
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado=5
          else:
            return False
        else:
            return False

      else:
            return False

#Estado final
    if self.estado==5:
      return True
    else:
      return False

def main():
  cadena=input("Introduce numero de automata binarios pares: ")

  AFD=Automata(cadena)

  if AFD.NumeroBinarios() == True:
    print("Es correcto el automata")
  else:
    print("No es correcto el automata")

if __name__ == "__main__":
  main()
        
