class Automata:
  def __init__(self,cadena):
    self.cadena=cadena

  def NumeroBinarios(self):
    self.estado="A"
    for i in range(0,len(self.cadena)):
      self.transicion=self.cadena[i]

#Estado inicial
      if self.estado == "A":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="B"
          elif self.transicion == '0':
             self.estado="C"
          else:
            return False
        else:
            return False
#Estado B
      elif self.estado=="B":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="C"
          elif self.transicion == '0':
             self.estado="A"
          else:
            return False
        else:
            return False
#Estado C
      elif self.estado=="C":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="D"
          else:
            return False
        else:
            return False
#Estado D
      elif self.estado=="D":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="F"
          elif self.transicion == '0':
             self.estado="E"
          else:
            return False
        else:
            return False
#Estado E
      elif self.estado=="E":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="D"
          elif self.transicion == '0':
             self.estado="C"
          else:
            return False
        else:
            return False
#Estado F
      elif self.estado=="F":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="G"
          elif self.transicion == '0':
             self.estado="A"
          else:
            return False
        else:
            return False
#Estado G
      elif self.estado=="G":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="H"
          elif self.transicion == '0':
             self.estado="E"
          else:
            return False
        else:
            return False
#Estado H
      elif self.estado=="H":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="I"
          elif self.transicion == '0':
             self.estado="E"
          else:
            return False
        else:
            return False
#Estado I
      elif self.estado=="I":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="J"
          elif self.transicion == '0':
             self.estado="E"
          else:
            return False
        else:
            return False
#Estado J
      elif self.estado=="J":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="I"
          elif self.transicion == '0':
             self.estado="K"
          else:
            return False
        else:
            return False 
#Estado K
      elif self.estado=="K":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="D"
          elif self.transicion == '0':
             self.estado="C"
          else:
            return False
        else:
            return False
#Estado L
      elif self.estado=="L":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="M"
          elif self.transicion == '0':
             self.estado="K"
          else:
            return False
        else:
            return False       
#Estado M
      elif self.estado=="M":
        if str.isdigit( self.transicion):
          if  self.transicion == '1':
             self.estado="H"
          elif self.transicion == '0':
             self.estado="A"
          else:
            return False
        else:
          return False

      else:
            return False

#Estados finales
    if self.estado=="F":
      return True
    elif self.estado=="C":
      return True
    elif self.estado=="E":
      return True
    elif self.estado=="F":
      return True
    elif self.estado=="G":
      return True
    elif self.estado=="H":
      return True
    elif self.estado=="I":
      return True
    elif self.estado=="J":
      return True
    elif self.estado=="K":
      return True
    elif self.estado=="M":
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
        