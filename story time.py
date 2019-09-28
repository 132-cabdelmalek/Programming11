from time import sleep
from user import *

print('\n"To Ply the Stars"')
print("Chris Torrence, 2015\n")
sleep(1)

# Let's find out the player's name, so we can be friendly.
# We go into an infinite loop until we get a valid string.
name = ""
while (name.strip() == ""):
  name = input("Hi, what's your name?")

import random
r = random.random()

# Make the player's younger sibling be a random gender.
if r <= 0.5:
  sibling = "brother"
  pronoun = "he"
else:
  sibling = "sister"
  pronoun = "she"

print("\nA loud noise startles you awake. " +
"At first, you can't remember who or where " +
"you are. Then you remember, you're " + name + ", "
"a middle-school student on your way to Saturn.\n")

sleep(2)

print("The noise continues. You can...")
awake = choice(["Push open the lid of my sleeping pod",
  "Call out to my little " + sibling])

# We're going to need these variables later.
siblingLocation = ""
sibName = ""

if awake == "b":
  siblingLocation = "locker"
  sibName = siblingName(sibling)
  print("\n'" + sibName + ", are you awake?' " +
  "you call out softly.\n")
  sleep(3)

  print("You don't hear any answer. Do you:")
  noAnswer = choice(["Call out again, louder",
    "Push open the lid of my sleeping pod"])

  if noAnswer == "a":
    print("\nYou cry out, '" + sibName + ", are you there?!'\n")
    sleep(3)
    print("Suddenly, you hear heavy footsteps. " +
    "The lid to your sleeping pod is thrown open.")
    badEnding(1)
  
print("\nYou quietly push open the lid of the sleeping pod. " +
"You hear a soft hiss as the excess nitrogen gas escapes.\n")
sleep(2)
print("In the corner you see your " + sibling + "'s pod.\n")
sleep(2)

# If we previously called out to our sibling, then we'll
# make their pod be empty - where could they be?
if siblingLocation == "locker":
  print("The pod is empty!\n")
else:
  print("You see your " + sibling + " peering out. " +
  pronoun.capitalize() + " looks scared.")
  # We need to get our sibling's name if we haven't already...
  if sibName == "":
    sibName = siblingName(sibling)
  print("Do you:")
  sibChoice = choice(["motion for " + sibName +
    " to lie there quietly",
    "signal for " + sibName + " to come join you"])
  if sibChoice == "a":
    siblingLocation = "pod"
  else:
    siblingLocation = "me"

# At this point, your sibling's location is either
# in the locker (good), the pod (bad), with you (also bad).
sleep(2)
print("\nSuddenly, you hear heavy footsteps coming towards " +
  "your compartment. Do you:")
hearNoise = choice(["Run and hide in the storage locker",
  "Pick up a hydrospanner and look threatening"])

if hearNoise == "b":
  print("\nA hulking figure strides into the room, " +
  "heavy boots clanging on the deck plates as he strides " +
  "over to you.")
  if siblingLocation == "me":
    print("\nWhen he sees that there are two of you, both " +
      "holding hydrospanners, he shouts in surprise and " +
      "runs back out of the room.")
  else:
    # If your sibling is either in the pod or the locker,
    # you are doomed.
    badEnding(1)
else:
  print("You quickly run over to the storage locker " +
    "and tug on the handle. It doesn't open!\n")
  sleep(3)
  if siblingLocation == "locker":
    print("Suddenly the locker door creaks open. " +
      "A hand reaches out and grabs your wrist.\n")
    sleep(2)
    print("Before you can cry out, " +
      "you are dragged into the locker.")
    sleep(1)
