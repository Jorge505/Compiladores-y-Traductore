class Automata:
  def __init__(self,cadena):
    self.cadena=cadena

  def NumeroBinarios(self):
    self.estado="F"
    for i in range(0,len(self.cadena)):
      self.transicion=self.cadena[i]

#Estado inicial
      if self.estado == "F":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="G"
          elif self.transicion == '0':
             self.estado="A"
          else:
            return False
        else:
            return False
#Estado A
      elif self.estado=="A":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="B"
          else:
            return False
        else:
            return False
#Estado B
      elif self.estado=="B":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="D"
          elif self.transicion == '0':
             self.estado="C"
          else:
            return False
        else:
            return False

#Estado C
      elif self.estado=="C":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="B"
          elif self.transicion == '0':
             self.estado="A"
          else:
            return False
        else:
            return False
#Estado D
      elif self.estado=="D":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="E"
          elif self.transicion == '0':
             self.estado="F"
          else:
            return False
        else:
            return False
#Estado G
      elif self.estado=="G":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="A"
          elif self.transicion == '0':
             self.estado="F"
          else:
            return False
        else:
            return False
#Estado E
      elif self.estado=="E":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="E"
          elif self.transicion == '0':
             self.estado="C"
          else:
            return False
        else:
            return False

#Estados finales
    if self.estado=="A":
      return True
    elif self.estado=="C":
      return True
    elif self.estado=="D":
      return True
    elif self.estado=="E":
      return True
    else:
      return False   
      
def main():
  cadena=input("Introduce numero de automata binarios pares: ")

  AFD=Automata(cadena)

  if AFD.NumeroBinarios() == True:
    print("Es correcto el automata ✔️")
  else:
    print("No es correcto el automata ❌")

if __name__ == "__main__":
  main()
    