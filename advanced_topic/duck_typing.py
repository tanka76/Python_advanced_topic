# Define the three classes
 
class Duck:
  def quack(self):
    print("I am a duck and I quack.")
 
class Goose:
  def quack(self):
    print("I am a goose and I quack.")
 
class Cat:
  def meow(self):
    print("I am a dog and I meow.")
 
# Define the method
def quack(animal):
  animal.quack()

quack(Duck())
quack(Goose())
quack(Cat())