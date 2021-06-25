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
             self.estado="A"
          elif self.transicion == '0':
             self.estado="B"
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
             self.estado="B"
          else:
            return False
        else:
            return False

#Estado final
    if self.estado=="C":
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
        
