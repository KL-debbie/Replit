from random import randint

print('Welcome')
pc_choice = randint(1, 100)

playing = True

while playing:
  choice = int(input("Choose Number(1-100): "))
  if choice == pc_choice:
    print('You Won!!')
    playing = False
  elif choice > pc_choice:
    print('Select Lower')
  elif choice < pc_choice:
    print('Select Higher')
