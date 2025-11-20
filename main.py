# By: Marshall D Turner
# In the far future, humanity has gone extinct. The world is now ruled by the robots that were created to serve them. You play as a Fixer, a robot tasked with maintaining and repairing factories. You are sent to the Mason Co Robotic Facility, a factory long thought to be abandoned. You come across the AI running the place and join forces to get the factory back up and running. As you explore the facility, you uncover info about the AI, the factory, and the world itself.

### Fair warning, this game is not long nor is the story finished. I wanted to go further and have a more complete story, but time did not permit it. The origninal idea was going to have a long puzzle room after the split sections after [Crossroads]. The puzzle room would end with a boss fight and have more fleshed out and open ended endings. Sadly that was cut short, so this is more of a demo than anything else, with very little lore. ###

import sys
import time
import scenes

##---## Time Values ##---##
shortTime = 1
longTime = 3

##---## Values ##---##
dmgTracker = 0
suspicionTracker = 0
pinkcomKnown = False
path = "Fill"

##---## Ending Trackers ##---##
breakerTracker = 0
warTraker = 0
heroTracker = 0


def  main():
  ##---## Intro ##---##
  print("""Mason Co Robotic Facility, a factory long thought to be abandoned, towers over you. Easily the size of a city, yet still below average. Intimidating nonetheless. No one would come here without reason and that includes you, a supposed Fixer. Those tasked with maintaining and repairing factories created back when man still roamed the earth. There is no demand for this place to be repaired, nor do you have any ties to it, your only goal is to sate your curiosity. A rare emotion for your kind. Equipped with only a Flathead Sword, you travel closer.""")
  time.sleep(longTime)
  print("\n")
  print("[ ]--------------------[Lobby]--------------------[ ]")
  time.sleep(longTime)
  print("\n")
  print("""You find yourself standing before the rusted and destroyed west entry gate, no longer fulfilling its purpose of protecting the facility. Walking inside reveals what could be assumed to be a lobby similar to that of a hotel. The only life found here are the plants sprouting all around. A stone fountain is located in the center of the lobby. No water currently flows through it, leaving an algae filled pool. There are a few doors on the left and right side of the room, but the door that catches your attention is at the other end of the lobby, right next to the front desk. It’s a metal door locked behind an ID reader. That should lead further into the facility.""")
  time.sleep(longTime)
  print("\n")
  print("""What to do…""")
  print("\n")
  time.sleep(shortTime)
  
  ##---## Intro's Options ##---##
  scenes.introScene()
  
  ##---## Scene One ##---##
  print("[ ]--------------------[The AI]--------------------[ ]")
  time.sleep(longTime)
  print("\n")
  print("""You swipe the ID Card through the scanner hoping it still works and to your surprise, it does. A small jingle plays indicating that the ID Card has been verified. The metal door opens automatically with a loud creak. You step past it into a pitch black room. You’re incapable of making anything out. You instinctively reach for the switch on the side of your head to turn on your lights. Yet before your hand makes it, the lights on the ceiling turn on. You were almost blinded by the sudden contrast of light. The room is small. Housing nothing more than some cushioned chairs. You notice a camera on the wall. You saw some in the lobby, but they didn’t interest you as they were all broken. This one though, is on.""")
  time.sleep(longTime)
  print("\n")
  print("""“Welcome to Mason Co Robotic Facility!”""")
  time.sleep(shortTime)
  print("\n")
  print("""A voice rang out from a speaker on a nearby wall.""")
  print("\n")
  time.sleep(shortTime)
  print("""“It’s been forever since an outside bot visited my facility. Hold on…That sword on your back. Not only are you the first visitor in ages, you’re a Fixer, too!? And here I thought they abandoned me.”""")
  print("\n")
  time.sleep(longTime)
  print("""Looks like the AI running the place is still operational.""")
  print("\n")
  time.sleep(shortTime)
  
  ##---## Scene One's Options ##---##
  breakerTracker, suspicionTracker = scenes.sceneOne()

  ##---## Scene Two ##---##
  print("[ ]--------------------[Welcome]--------------------[ ]")
  time.sleep(longTime)
  print("\n")
  print("""You find yourself on a platform looking out to a vast open area. Gigantic, building-like silos that stretch all the way to the unseeable ceiling above laid out throughout the facility. You notice long platforms attached to them that connect the silos to each other and stairs on their side that lead up and down. Traversing this facility without a guide can be a nightmare. You spot a fellow robot hunched over near the platform railing and stairs that lead up to a nearby silo.""")
  time.sleep(longTime)
  print("\n")
  if suspicionTracker == 0:
    print("""“Again, welcome to Mason Co! This is only a small section of the facility with not much importance, but we will start here first. Just head up the stairs.”""")
  time.sleep(shortTime)
  print("\n")

  ##---## Scene Two's Options ##---##
  warTraker, dmgTracker, pinkcomKnown, suspicionTracker = scenes.sceneTwo()

  ##---## Scene Three ##---##
  time.sleep(longTime)
  print("\n")
  print("[ ]--------------------[Crossroads]--------------------[ ]")
  time.sleep(longTime)
  print("\n")
  print("""After walking up 1,056 steps, you reach a platform connected to two(2) bridges that lead into different directions. Left and Right, a classic choice.""")
  print("\n")
  time.sleep(longTime)
  if suspicionTracker == 0:
    print("""“Left will get you there faster, but there are currently some Pinkcom models in the way.”""")
    print("\n")
    time.sleep(longTime)
    print("“Right is of no importance.”")
    print("\n")
    time.sleep(shortTime)

  ##---## Scene Three's Options ##---##
  path = scenes.sceneThree()

  ##---## Scene Four ##---##
  if path == "Left":
    print("[ ]--------------------[Silo]--------------------[ ]")
    time.sleep(longTime)
    print("\n")
    if suspicionTracker < 5:
      print("They said go Left, so you go Left.")

    else:
      print("Guess you’ll go Left.")

    print("""After 1 and 46 minutes of walking, you arrive at one of the silos. There is only a door that leads inside.""")
    time.sleep(longTime)
    print("\n")
    if suspicionTracker < 5:
      print("""“This should be the only bump in the road. It will be dangerous, but I’m sure a Fixer like you should have it covered.”""")
      time.sleep(longTime)
      print("\n")
      print("""“Let me get the door for you.”""")

    time.sleep(shortTime)
    print("\n")

    if pinkcomKnown:
      print("""The door opens automatically, revealing a wide open room with an exit at the other end. Piles of scrap and destroyed machine litter the area. You can not discern what purpose the room had in the past, but now it looks to be occupied by Pinkcom robots. There are 12 of them scattered about.""")

    else:
      print("""The door opens automatically, revealing a wide open room with an exit at the other end. Piles of scrap and destroyed machine litter the area. You can not discern what purpose the room had in the past, but now it looks to be occupied by hostile robots. There are 12 of them scattered about.""")

    time.sleep(longTime)
    print("\n")
    
    ##---## Scene Four's Options ##---##
    
    warTraker, dmgTracker = scenes.sceneFour()

  ##---## Scene Five ##---##
  else:
    print("[ ]--------------------[Town]--------------------[ ]")
    time.sleep(longTime)
    print("\n")
    if suspicionTracker < 5:
      print("They’re clearly hiding something.")
      time.sleep(shortTime)
      print("\n")
      print("""“Wait!”""")

    else:
      print("Guess you’ll go Right.")

    time.sleep(shortTime)
    print("\n")
    print("""After 6 hours and 4 minutes of walking a seemingly straight forward path, you arrive at a massive platform that leads to multiple silos. However, that’s not the important part. Atop this platform rests some sort of small town. The last thing you expected to find here. Unlike the towns found outside, their buildings appear to be made entirely out of scrap metal. Mostly due to the lack of natural resources here.""")
    time.sleep(longTime)
    print("\n")
    if suspicionTracker < 5:
      print("""You take notice that the AI hasn’t spoken to you since you took the Right path. There are cameras and speakers here and there that look to be functional, but they aren't using them. Weird.""")
      time.sleep(longTime)

    else:
      time.sleep(shortTime)

    print("\n")
    print("""With nowhere else to go but forward, you head into the village.""")
    if pinkcomKnown:
      time.sleep(shortTime)
      print("\n")
      print("""The residents simply stare at your arrival. They look to be different models than the Pinkcom robots. Perhaps they were made here.""")

    else:
      time.sleep(shortTime)
      print("\n")
      print("""The residents simply stare at your arrival. They look to be different models than the one earlier. Perhaps they were made here.""")

    time.sleep(longTime)
    print("\n")
    print("""A particularly worn down robot confronts you. Their voice box sounds worn out as well.""")
    time.sleep(shortTime)
    print("\n")
    print("""“S-sorry for-r the awkward town gre-e-eting. Seeing an-n-n-n unkn-n-own model such as you s-show up has put-t-t-t them on edge. What b-brings you here, t-t-traveler?“""")
    time.sleep(longTime)
    print("\n")
    
    ##---## Scene Five's Options ##---##
    heroTracker, breakerTracker = scenes.sceneFive()

  ##---## Endings ##---##
  print("[ ]--------------------[Abrupt]--------------------[ ]")
  time.sleep(longTime)
  print("\n")
  scenes.endingScene()


if __name__ == "__main__":
   main()