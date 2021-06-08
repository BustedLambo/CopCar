#Type 'help' for help.

import random as r, sys as s, time as t

player_hit_potential = r.randint(0, 15)
player_dodge_potential = r.randint(0, 10)
player_uppercut_potential = r.randint(0, 10)
player_energygain_potential = r.randint(1, 10)
player_uppercut_damage = r.randint(35, 45)
enemy_hit_potential = r.randint(0, 17)
hp_random = r.randint(2, 10)
ko_energy = 0
player_hp = 75
enemy_hp = 60


#GAME FUNCTION
def game():
    global ko_energy, player_hp, enemy_hp, hp_random
    print("What will you do?")
    print("MOVES:")
    print(">PUNCH (p)")
    print(">HOOK (h)")
    print(">UPPERCUT (u)")
    print(">DODGE (d)")
    if ko_energy == 1:
      print("(You have", ko_energy, "ENERGY POINT.)")
    else:
      print("(You have", ko_energy, "ENERGY POINTS.)")
    print("_______")
    userMove = input()
    print()
    #PUNCH
    if (userMove == "punch" or
        userMove == "p" or
        userMove == "P" or
        userMove == "PUNCH"):
        if player_hit_potential < 9:
            print("You throw a PUNCH...\n")
            t.sleep(2)
            print("   ...and the attack is successful!\n")
            if hp_random == 10:
              print("It's a critical hit!\n")
              print("You have inflicted", hp_random, "points of damage!\n")
              t.sleep(1)
            else:
              print("You have inflicted", hp_random, "points of damage!\n")
            enemy_hp -= hp_random
            ko_energy += 1
        else:
            print("You throw a PUNCH...\n")
            t.sleep(1)
            print("   ...but you miss.\n")
            if enemy_hit_potential > 10:
              t.sleep(0.5)
              print("Your enemy uses the chance to strike, costing you", hp_random, "HP!\n")
              t.sleep(0.25)
              player_hp -= hp_random
              enemy_hp += 2
              ko_energy -= 1
            else:
                print("Your enemy uses the chance to strike, but he misses!\n")
    #HOOK
    elif (userMove == "hook" or
          userMove == "h" or
          userMove == "H" or
          userMove == "HOOK"):
        if player_hit_potential < 7:
            print("You use HOOK...\n")
            print("   ...and the attack is successful!\n")
            if hp_random == 10:
              print("It's a critical hit!\n")
              print("You have inflicted", hp_random, "points of damage!\n")
            else:
              print("You have inflicted", hp_random, "points of damage!\n")
            hp_random *= 2
            enemy_hp -= hp_random
            ko_energy += 1
        else:
            print("You use HOOK...\n")
            print("   ...but you miss.\n")
            if enemy_hit_potential > 10:
                print("Your enemy uses the chance to strike, costing you", hp_random, "HP!\n")
                player_hp -= hp_random
                enemy_hp += 4
                ko_energy -= 1
            else:
                print("Your enemy uses the chance to strike, but he misses!\n")
    #DODGE
    elif (userMove == "dodge" or
          userMove == "d" or
          userMove == "D" or
          userMove == "DODGE"):
        print("You decide to DODGE the next attack...\n")
        if player_dodge_potential < 6 or enemy_hit_potential > 8:
                print("   ...and you dodge successfully!\n")
                if player_energygain_potential <= 5:
                  ko_energy += 1
                else:
                  pass
        else:
                print("   ...but it was unsuccessful.\n")
                print("You lost", hp_random, "HP!")
                player_hp -= hp_random
                enemy_hp += 6
                ko_energy -= 1
    #UPPERCUT
    elif (userMove == "uppercut" or
          userMove == "u" or
          userMove == "U" or
          userMove == "UPPERCUT"):
        if ko_energy >= 5:
            print("You have enough ENERGY POINTS to use an UPPERCUT!")
            print("Are you sure you'd like to use this move? (yes/no)")
            uppercutConfirm = input()
            if (uppercutConfirm == "yes" or
                uppercutConfirm == "y" or
                uppercutConfirm == "Y" or
                uppercutConfirm == "YES"):
                print()
                print("You decide to use an UPPERCUT!\n")
                print("Using all of your strength, you hit your oppenent...!\n")
                if player_uppercut_potential > 1:
                        print("KABOOM!\n")
                        print("Your powerful punch lands.")
                        print("Your opponent has lost", player_uppercut_damage, "HP!")
                        ko_energy -= 5
                        enemy_hp -= player_uppercut_damage
                else:
                        print("   ...Huh?\n")
                        print("Your punch didn't land!\n")
                        print("Your foe uses this chance to attack! You lost", hp_random, "HP!\n")
                        ko_energy -= 5
                        player_hp -= hp_random
            elif (uppercutConfirm == "no" or
                  uppercutConfirm == "n" or
                  uppercutConfirm == "N" or
                  uppercutConfirm == "NO"):
                print("You decided to not use an UPPERCUT.")
        elif ko_energy < 5:
            print("You have", ko_energy, "ENERGY POINTS. You need", 5 - ko_energy, "more to perform an UPPERCUT!")
        else:
            pass
    #HELP
    elif (userMove == "help" or
          userMove == "HELP" or
          userMove == "?"):
        print("How to play:")
        print("- Type in the commands that are by each arrow.")
        print("- Gain 5 ENERGY POINTS to use an uppercut!")
        print("- If your HP drops to zero, you lose!")
    elif userMove == "activate hacks":
      print("H4CK5 H4V3 B33N 4C71V473D")
      print("WH47 D0 Y0U W4N7 70 3D17?")
      print(">HP")
      print(">ENERGY POINTS")
      print(">WIN")
      choice = input()
      if choice == "hp" or choice == "HP":
        print("M4X HP?")
        z = input()
        if z == "yes":
          player_hp = 999
        else:
          pass
      elif choice == "energy points":
        print("M4X 3N3RGY P01N7S?")
        a = input()
        if a == "yes":
          ko_energy = 999
        else:
          pass
      elif choice == "win":
        enemy_hp = -999
      else:
        pass
    #EXIT/QUIT
    elif (userMove == "quit" or
          userMove == "exit" or
          userMove == "q" or
          userMove == "e" or
          userMove == "Q" or
          userMove == "E" or
          userMove == "QUIT" or
          userMove == "EXIT"):
      print("Are you sure you want to quit? (yes/no)")
      quitConfirmation = input()
      if (quitConfirmation == "yes" or
          quitConfirmation == "y" or
          quitConfirmation == "Y" or
          quitConfirmation == "YES"):
        s.exit()
      else:
        pass
    else:
        print("Huh? Try that again.\n")
    
def healthLimits():
  global player_hp, enemy_hp
  if player_hp <= 0:
    print("Oh no! You've run out of HP!")
    print("You lost!")
    print("Better luck next time!")
    s.exit()
  else:
      pass
  if enemy_hp <= 0:
    print("Your opponent is KO'ed!")
    print("Congrats! You won the game!")
    s.exit()
    
def healthLimits_2():
  global player_hp, enemy_hp
  while player_hp > 75:
    player_hp = 75
  while enemy_hp > 60:
    enemy_hp = 60

def energyPointLimiter():
    global ko_energy
    if ko_energy < 0:
        ko_energy = 0

def stats():
    print("YOUR HP:", player_hp)
    print("ENEMY HP:", enemy_hp)
    print("-----------")
      
############################################

print("ROUND START")
print("----------")

while True:
    stats()
    energyPointLimiter()
    healthLimits()
    healthLimits_2()
    game()
    player_hit_potential = r.randint(0, 15)
    player_dodge_potential = r.randint(0, 7)
    player_uppercut_potential = r.randint(0, 10)
    player_energygain_potential = r.randint(1, 10)
    player_uppercut_damage = r.randint(35, 45)
    enemy_hit_potential = r.randint(0, 20)
    hp_random = r.randint(2, 10)