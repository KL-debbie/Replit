# 일반 유닛
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# marine1 = Unit("marine", 40, 6)
# marine2 = Unit("marine", 40, 6)
# tank = Unit('tank', 150, 34)

# 공격 유닛
class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군에게 공격. [공격력 {2}]".format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    self.hp -= damage
    print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴".format(self.name))

# 메딕
# 공격 유닛
'''
firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack('5시')
# 공격 2번
firebat1.damaged(25)
firebat1.damaged(25)
'''

class Flyable:
  def __init__(self, speed):
    self.speed = speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.speed))

# 공중 공격 유닛 
class FlyAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, speed):
    AttackUnit.__init__(self, name, hp, 0, damage)    # 지상 스피드 0
    Flyable.__init__(self, speed)

# 공중 공격 유닛, 한번에 14발의 미사일
valkyrie = FlyAttackUnit('valkyrie', 200, 60, 50)
valkyrie.fly(valkyrie.name, '3시')

vultue = AttackUnit("vul", 80, 10, 20)
bc = FlyAttackUnit('BattleCruiser', 500, 25, 3)

vultue.move('11시')
bc.fly(bc.name, '9시')

