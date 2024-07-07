age = int(input('How old are u? '))

if age < 18:
  print('Not allow')
elif age > 18 and age < 36:
  print('Drink')
elif age == 40 or age == 60:
  print('Party')
elif age > 60 and age < 85:
  print('beer!')
else:
  print('good bye')


def make_juice(fruit):
  return f"{fruit} + 🍉"

def add_ice(juice):
  return f"{juice} +"🧊"

def add_suger(ice):
  return f"{ice} + 🍬"

juice = make_juice("�")
cold_juice = add_ice(juice)
perfect_juice = add_suger(cold_juice)

print(perfect_juice)