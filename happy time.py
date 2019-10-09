import random
choices = ["A","B"]
choice2a = random.choice(choices)
print(choice2a)

from time import sleep 
name= input("what is your name")
print ("Hi" + name + " welcome to my story")
sleep(3)
print ("You are watching TV when an asteroid with a door falls through your roof")
sleep(2)
print ("You can:")
print ("Choice A: Call 911")
print ("Choice B: Hide behind the TV")
choice1 = input("what do you do")#choice
if choice1 == "a" or choice1 == "A": 
  print ("You call and hear fuzz: The phone has been blocked")
  print ("You can:")
  print ("Choice A: Try your cell phone")
  print ("Choice B: Throw the phone into the ground")
  choice2a=input("What do you do?")#choice
  if choice2a == "a" or choice2a == "A":
    print ("Your cell phone will not turn on; the batterie has been removed")
    sleep(2)
    print ("You stomp on the ground and it breaks the floor and you fall in a hole and die")#die
  elif choice2a == "b" or choice2a == "B":
    print ("You get shocked and die")#die
elif choice1 == "b" or choice1 == "B":
  print ("Your TV falls over and you get stuck under it")
  print ("You can:")
  
  print ("Choice A: Pick the TV back up and hide behind it")
  print ("Choice B: Hide behind your couch instead")
  choice2b = input("What do you do?")#choice
  if choice2b == "A" or choice2b == "a":
    print ("The door opens and you hear somthing stepping out")
    print ("You get hit in the head by a flying spear and die")#die
  elif choice2b == "B" or choice2b == "b":
    print ("The TV falls over and makes a loud noise")
    print ("You can:")
    print ("Choice A: Sceam because the loud noise startled you")
    print ("Choice B: tiptoe over to see of it broke")
    choice2bb = input("What do you do?")#choice
    if choice2bb == "a" or choice2bb == "A":
      print ("You quickly cover your mouth hoping noone or nothing heard you")
      print ("To bad something did and a 20 foot speargun pops out of the astaroid and shoots you and you die ")#die
    elif choice2bb == "b" or choice2bb == "B":
      print ("desktop.inie door slowly creaks open")
      print ("You can")
      print ("Choice A: Run like a crazy person and charge strait at the door yelling YAAAAA!")
      print ("Choice B: Go pick up a kitchen knife and crouch behint the counter")
      choice2bbb = input("What do you do?")#choice
      choice2bbb = choice2bbb.lower()
      if choice2bbb == "a":
        print ("You see a face and you look into the eyes and vaporate")#die
      elif choice2bbb == "b":
        print ("The door finishes opening and you here footsteps. You peek out and see a creature")
        print ("You can")
        print ("Choice A:  Hold the knife and take a closer look")
        print ("Choice B: Throw the knife at the creature")
        choicebbbb = input ("What do you do?")#choice
        choicebbbb = choicebbbb.lower()
        if choicebbbb == "a":
          print ("You get shot by a speargun and die. THE END YOU FAILED")#die
        elif choicebbbb == "b":
          print ("You here a groan and you see the creature lying on the floor with the knife in it's chest")
          print ("There are 2 knives")
          print ("You can")
          print ("Choice A: Grab one knife")
          print ("Choice B: Grab both")
          choicebbbbb = input ("What do you do?")#choice
          choicebbbbb = choicebbbbb.lower()
          if choicebbbbb == "a":
            print ("two creatures pop out and you throw the knife and kill one but the other one wacks you over the head with the tip of the spear and you die")#die
          else:
              print ("Two more creatures with large spearguns pop out of the door")
              print ("You can...")
              print ("Choice A: Throw one knife at one and charge the other.")
              print ("Choice B: Throw both knives at the creatures")
              choicebbbbb= input("What do you do?")#choice
              choicebbbbb = choicebbbbb.lower ()
              if choicebbbbb == "a":
                print ("You miss the throw and get shot and die")#die
              else:
                print ("You hit both of them and they both die, but one of them fires the shot of and just misses you")
                print ("You can...")
                print ("Choice A: Turn and run")
                print ("choice B: Charge the door")
                choicebbbbbb = input("What do you do?")#choice
                choicebbbbbb = choicebbbbbb.lower()
                if choicebbbbbb == "a":
                  print ("You hit the spear in the ground which was a double sided spear and die")#die
                else:
                  print ("You go in and find 20,000 pounds of pure diamond inside. YOU WON")#winning
          
else:
  print ("You must answer A or B: The world explodes and you die")#die
