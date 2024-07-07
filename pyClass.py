class Dog:

  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("zzzzzzz....")


class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(
        name,
        breed,
        5,
    )
    self.aggresive = True

  def rrrr(self):
    print("stay away!")


class puppy(Dog):

  def __init__(self, name, breed):
    super().__init__(
        name,
        breed,
        0.1,
    )
    self.spoiled = True

  def __str__(self):
    return f"{self.breed} name {self.name}"

  def woof(self):
    print('Woof_Woof')

  def introduce(self):
    self.woof()
    print(f"Hello My name is {self.name} and I am a baby {self.breed}")
    self.woof()


ruffus = puppy(name='ruffus', breed='beagle')

bibi = GuardDog(
    name='bibi',
    breed='dalmatian',
)

ruffus.woof()
bibi.rrrr()
