<<<<<<< HEAD
class Dog:
  species = "Dog"
  def __init__(self, name, age):
    self.name= name
    self.age= age

Nelson = Dog("Nelson", 8)

Bruno = Dog("Bruno", 10)
print("Nelson Is A {} " .format(Nelson.species))
print("Bruno Is Also A {}" .format(Bruno.species))
print("Nelson Is {}" .format(Nelson.age) ,"Years Old" )
=======
class Dog:
  species = "Dog"
  def __init__(self, name, age):
    self.name= name
    self.age= age

Nelson = Dog("Nelson", 8)

Bruno = Dog("Bruno", 10)
print("Nelson Is A {} " .format(Nelson.species))
print("Bruno Is Also A {}" .format(Bruno.species))
print("Nelson Is {}" .format(Nelson.age) ,"Years Old" )
>>>>>>> 3920a7233fe64405a628e1fc7cc9ed6f85077a04
print("{} Is {} Years Old" .format(Bruno.name , Bruno.age))