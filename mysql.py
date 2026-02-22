
# under lär jag mig grunder av oop i python
class Hund:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def skäll(self):
        return f"{self.namn} säger Voff!"
# Skapa en instans av klassen Hund
min_hund = Hund("Fido", 3)
print(min_hund.skäll())  # Output: Fido säger Voff!
print(f'Min hunds namn är {min_hund.namn} och den är {min_hund.ålder} år gammal.')

#så medans ja följer va som kommer lär jag mig oop i python
#och sen kan ja göra ett spel med oop i python
class Bil:
    def __init__(self, märke, modell, år):
        self.märke = märke
        self.modell = modell
        self.år = år

    def starta(self):
        return f"{self.märke} {self.modell} från {self.år} startar."
# Skapa en instans av klassen Bil
min_bil = Bil("Volvo", "XC90", 2020)
print(min_bil.starta())  # Output: Volvo XC90 från 2020 start
print(f'Min bil är en {min_bil.märke} {min_bil.modell} från {min_bil.år}.')
#och sen kan ja göra ett spel med oop i python
class Spelare:
    def __init__(self, namn, hälsa):
        self.namn = namn
        self.hälsa = hälsa

    def ta_skada(self, skada):
        self.hälsa -= skada
        return f"{self.namn} tog {skada} skada och har nu {self.hälsa} hälsa kvar."
    # Skapa en instans av klassen Spelare
spelare1 = Spelare("Hero", 100)
print(spelare1.ta_skada(20))  # Output: Hero tog 20
print(f'Spelarens namn är {spelare1.namn} och hälsan är {spelare1.hälsa}.')
#under så ska de va en övning där ja lär mig grund en bra första övning i oop i python
class Cirkle:
    def __init__(self, radie):
        self.radie = radie

    def area(self):
        return 3.14 * (self.radie ** 2)

    def omkrets(self):
        return 2 * 3.14 * self.radie
# Skapa en instans av klassen Cirkle
min_cirkle = Cirkle(5)
print(f'Area: {min_cirkle.area()}')      # Output: Area:
print(f'Omkrets: {min_cirkle.omkrets()}')  # Output: Omkrets:
print(f'Cirkeln har radie {min_cirkle.radie}.')








class myball:
    x = 4
print(myball)

p1 = myball()
print(p1.x)

del p1
print(p1.x)




class Person:
   def__init__(self, name, age)
   self.name = name
   self.age = age
   
  def myfunc(self):
    print('hello my name is ' + self.name)

p1 = Person('John', 36)

del p1

print(p1)


class myball:
    x = 4
p1 = myball()
p2 = myball()
p3 = myball()
print(p1.x)
print(p2.x)
print(p3.x)
