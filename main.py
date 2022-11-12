import random

recordsW =random.randint(0,100)

class player:
  def __init__(self, name):
    self.name = name
    self.age = random.randint(18,60)
    self.recordsW = random.randint(0,100)
    self.recordsL = 100-self.recordsW
  def printAtr(self):
    print(f"Name: {self.name} Age: {self.age} Win Records:{self.recordsW} Loss Records:{self.recordsL}")

players = []

print("Tennis Simulation Generation Version 1.0")
print("\n")

for i in range(8):
  x = str(input("Enter your player name here: "))
  players.append(player(x))



for i in players:
  i.printAtr()
  print("")

print("------------------------------------------------------------")
print("")
winners=[]

for i in range(4):
  random_item_1=random.choice(players)
  random_item_2=random.choice(players)

  while random_item_1==random_item_2:
    random_item_2=random.choice(players)

  #battle code

  player_1_W=random_item_1.recordsW
  player_2_W=random_item_2.recordsW
  W_sum=player_1_W+player_2_W

  quarter_battle=random.randint(0,W_sum)
  winner = ""
  loser = ""
  if(quarter_battle<player_1_W):
    winner=random_item_1
    loser=random_item_2.name
    
  
  if(player_1_W+1<W_sum):
    winner=random_item_2
    loser=random_item_1.name

  winners.append(winner)
    

  players.remove(random_item_1)
  players.remove(random_item_2)
  
  print(f"{random_item_1.name} vs {random_item_2.name} winner is {winner.name} and the loser is {loser}")

  print("")


print("----------------------------")

for i in winners:
  print(i.name)

print("-----------------------------")

winners2=[]

for i in range(2):
  random_item1=random.choice(winners)
  random_item2=random.choice(winners)
  
  while random_item1==random_item2:
    random_item2=random.choice(winners)
    
  player_1W=random_item1.recordsW
  player_2W=random_item2.recordsW
  Wsum=player_1W+player_2W


  winner1 = ""
  loser1 = ""
  if(0<player_1W):
    winner1=random_item1
    loser1=random_item2
    
  
  if(player_1W+1<Wsum):
    winner1=random_item2
    loser1=random_item1

  winners2.append(winner1)
    

  winners.remove(random_item1)
  winners.remove(random_item2)
  
  print(f"{random_item1.name} vs {random_item2.name} winner is {winner1.name} and the loser is {loser1.name}")

  print("")

print("----------------------------")

for i in winners2:
  print(i.name)

print("-----------------------------")


winners3=[]

for i in range(1):
  random_item1=random.choice(winners2)
  random_item2=random.choice(winners2)
  
  while random_item1==random_item2:
    random_item2=random.choice(winners2)
    
  player_1W=random_item1.recordsW
  player_2W=random_item2.recordsW
  Wsum=player_1W+player_2W


  winner1 = ""
  loser1 = ""
  if(0<player_1W):
    winner1=random_item1
    loser1=random_item2
    
  
  if(player_1W+1<Wsum):
    winner1=random_item2
    loser1=random_item1

  winners3.append(winner1)
    

  winners2.remove(random_item1)
  winners2.remove(random_item2)
  
  print(f"{random_item1.name} vs {random_item2.name} winner is {winner1.name} and the loser is {loser1.name}")

  print("")

print("----------------------------")

for i in winners3:
  print(i.name)
