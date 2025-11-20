import sys
import check
import time
from arrays import optionList
from arrays import weapons
from arrays import inventory
import main

def introScene():
  options = 4

  print("Choices:")
  if "introOne" in optionList:
      print("  1. [Interact] - Head through the door leading deeper into the facility")
  if "introTwo" in optionList:
      print("  2. [Interact] - Search the front desk")
  if "introThree" in optionList:
      print("  3. [Interact] - Investigate the fountain")
  ##---## Checks if "ID Card" is in inventory ##---##
  if "ID Card" in inventory:
    print("  4. [Item] Use the ID Card on the door scanner")
    
  entry = input("Enter the number corresponding to your choice: ")
  entryCheck = check.validEntry(entry, options)
  if entryCheck:
    match entry:
     case "1":
       if "introOne" in optionList:
         print("\n")
         print("You chose 1")
         time.sleep(main.shortTime)
         print("\n")
         print("""You walk up to the door hoping it’s unlocked…it’s not. You try to pry it open with your sword.
It’s sturdier than anticipated. Seems the only way through is to find an ID for the scanner. Hopefully it still functions.""")
         print("\n")
         ##---## Hides the option ##---##
         optionList.remove("introOne")
         introScene()
         
       else:
         print("\n")
         print("Invalid option")
         introScene()
         
     case "2":
       if "introTwo" in optionList:
          print("\n")
          print("You chose 2")
          time.sleep(main.shortTime)
          print("\n")
          print("""It's been picked clean.""")
          print("\n")
          ##---## Hides the first option ##---##
          optionList.remove("introTwo")
          introScene()
        
       else:
          print("\n")
          print("Invalid option")
          introScene()
       
     case "3":
       if "introThree" in optionList:
          print("\n")
          print("You chose 3")
          time.sleep(main.shortTime)
          print("\n")
          print("""You walk up to the stone fountain. It’s fine stonework seems to be what’s keeping it from crumbling after all these years. You notice something in the water.""")
          print("\n")
          time.sleep(main.longTime)
          print("[You’ve collected an ID Card]")
          print("\n")
          ##---## Adds "ID Card" to inventory ##---##
          inventory.append("ID Card")
          ##---## Hides the first option ##---##
          optionList.remove("introThree")
          introScene()

       else:
          print("\n")
          print("Invalid option")
          introScene()
       
     case "4":
       ##---## Checks if "ID Card" is in inventory ##---##
        if "ID Card" in inventory:
         print("\n")
         print("You chose 4")
         time.sleep(main.shortTime)
         print("\n")
       ##---## If not, the choice is invalid ##---##
        else:
           print("\n")
           print("Invalid option")
           introScene()

  else:
     print("\n")
     print("Invalid option")
     introScene()

##-------------## Scene One ##-------------##

def  sceneOne():
   options = 3
  
   print("""Choices:
  1. [Gesture] Give a thumbs up
  2. [Interact] Head towards the next door
  3. [Attack] Destroy the speaker and camera""")
  
   entry = input("Enter the number corresponding to your choice: ")
   entryCheck = check.validEntry(entry, options)
   if entryCheck:
      match entry:
         case "1":
            print("\n")
            print("You chose 1")
            time.sleep(main.shortTime)
            print("\n")
            print("""You don’t have a voicebox you can use to communicate, so you simply give a thumbs up to the camera. That should be enough to show that you are here to help.""")
            print("\n")
            time.sleep(main.longTime)
            print("""“Great! I’ll open the door leading into the facility and guide you to the nearest place in need of repair.”""")
            print("\n")
            time.sleep(main.longTime)
            print("""The door at the other end of the room opens up.""")
            print("\n")
            time.sleep(main.shortTime)
            print("""“I’ve never seen how you Fixers work before, so I’m excited!”""")
            print("\n")
            time.sleep(main.shortTime)
            print("""You step through the door.""")
            print("\n")
            
            return main.breakerTracker, main.suspicionTracker
           
         case "2":
            print("\n")
            print("You chose 2")
            time.sleep(main.shortTime)
            print("\n")
            print("""You don’t have a voicebox you can use to communicate, so you won’t bother trying. You head towards the door at the other end of the room.""")
            print("\n")
            time.sleep(main.longTime)
            print("""“I guess you’re in a hurry. I’ll open the door leading into the facility and guide you to the nearest place in need of repair.”""")
            print("\n")
            time.sleep(main.longTime)
            print("""The door at the other end of the room opens up.""")
            print("\n")
            time.sleep(main.shortTime)
            print("""“I’ve never seen how you Fixers work before, so I’m excited!”""")
            print("\n")
            time.sleep(main.shortTime)
            print("""You step through the door.""")
            print("\n")
            
            return main.breakerTracker, main.suspicionTracker
           
         case "3":
            print("\n")
            print("You chose 3")
            time.sleep(main.shortTime)
            print("\n")
            print("""You’re not here to help, but to sate your curiosity. Having an AI constantly in your ear (even if you don’t technically have ears) while exploring is going to be annoying, so you plan to shut it up.""")
            print("\n")
            time.sleep(main.longTime)
            print("""You swing your sword at the speaker, smashing it to pieces. Then you do the same with the camera. That should be enough to show that you should be left alone.""")
            print("\n")
            time.sleep(main.longTime)
            print("""You head towards the door at the other end of the room. Just like the last door, it locked. This time by the AI. Luckily it’s not as sturdy, so you pry it open and step through.""")
            print("\n")
            main.breakerTracker += 1
            main.suspicionTracker = 5

            return main.breakerTracker, main.suspicionTracker

   else:
      print("\n")
      print("Invalid option")
      return sceneOne()
   
   return main.breakerTracker, main.suspicionTracker

##-------------## Scene Two ##-------------##

def sceneTwo():
  mainOptions = 3


  print("""Choices:
  1. [Interact] Head up the stairs""")
  if "sceneTwo_Two" in optionList:
    print("  2. [Interact] Look down from the platform")
  if "sceneTwo_Three" in optionList:
    print("  3. [Interact] Investigate the robot")
    
  entry = input("Enter the number corresponding to your choice: ")
  entryCheck = check.validEntry(entry, mainOptions)
  if entryCheck:
     match entry:
      case "1":
         print("\n")
         print("You chose 1")
         time.sleep(main.shortTime)
         print("\n")
         if main.suspicionTracker == 0:
                print("""“Right this way, my good Fixer!”""")
         else:
                print("""You head up the metal stairs.""")

         return main.warTraker, main.dmgTracker, main.pinkcomKnown, main.suspicionTracker
        
      case "2":
        if "sceneTwo_Two" in optionList:
          print("\n")
          print("You chose 2")
          time.sleep(main.shortTime)
          print("\n")
          print("""You look down from the platform. The floor is pitch black from the lack of light, giving the illusion that the silos are growing from the depths of the earth. There are pipes of varying sizes that uniformly stretch out in multiple directions.""")
          time.sleep(main.longTime)
          print("\n")
          optionList.remove("sceneTwo_Two")
          time.sleep(main.longTime)
          sceneTwo()
          
        else:
          print("\n")
          print("Invalid option")
          sceneTwo()
          
      case "3":
        if "sceneTwo_Three" in optionList:
          print("\n")
          print("You chose 3")
          time.sleep(main.shortTime)
          print("\n")
          print("""They might know something.""")
          time.sleep(main.shortTime)
          print("\n")
          print("""As you walk closer, the robot begins twitching.""")
          time.sleep(main.shortTime)
          print("\n")
          if main.suspicionTracker == 0:
            print("""“Careful with getting too close, it might lounge at you.”""")
            time.sleep(main.shortTime)
            print("\n")
            
          main.warTraker, main.dmgTracker, main.pinkcomKnown, main.suspicionTracker = robotInteraction()
          optionList.remove("sceneTwo_Three")
          sceneTwo()

        else:
          print("\n")
          print("Invalid option")
          sceneTwo()
  
  else:
     print("\n")
     print("Invalid option")
     sceneTwo()

  return main.warTraker, main.dmgTracker, main.pinkcomKnown, main.suspicionTracker

##-------------## Robot Interaction ##-------------##

def  robotInteraction():
    options = 4
  
    print("""Choices:
  1. [Interact] Walk away.""")
    if main.suspicionTracker == 0:
           if "sceneTwo_Sub_One" in optionList:
             print("""  2. [Gesture] Look towards a nearby camera in confusion""")
    if "sceneTwo_Sub_Two" in optionList:
           print("""  3. [Item] Show it the ID Card""")
    print("""  4. [Attack] Attack the robot""")

    subEntry = input("Enter the number corresponding to your choice: ")
    subEntryCheck = check.validEntry(subEntry, options)
    if subEntryCheck:
           match subEntry:
            case "1":
               print("\n")
               print("You chose 1")
               time.sleep(main.shortTime)
               print("\n")
               print("""Best not to get involved with it.""")
               time.sleep(main.shortTime)
               print("\n")
               optionList.remove("sceneTwo_Three")
               return main.warTraker, main.dmgTracker, main.pinkcomKnown, main.suspicionTracker

            case "2":
               if main.suspicionTracker == 0:
                 if "sceneTwo_Sub_One" in optionList:
                    print("\n")
                    print("You chose 2")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""“Why are you looking over here? This isn’t one of my models.”""")
                    print("\n")
                    time.sleep(main.shortTime)
                    print("""“It broke into my facility 156 years ago. Or was it 178? My time management isn’t what it used to be.”
“I do know it came from Pinkcom, though. I would have thought that a Fixer like you would know the difference between models.”""")
                    print("\n")
                    time.sleep(main.longTime)
                    main.pinkcomKnown = True
                    main.suspicionTracker += 1
                    optionList.remove("sceneTwo_Sub_One")
                    robotInteraction()

               else:
                  print("\n")
                  print("Invalid option")
                  robotInteraction()

            case "3":
               if "sceneTwo_Sub_Two" in optionList:
                  print("\n")
                  print("You chose 3")
                  time.sleep(main.shortTime)
                  print("\n")
                  print("""Maybe it will do something if you show the ID.""")
                  print("\n")
                  time.sleep(main.shortTime)
                  print("""Its head twists and looks in your direction. It pauses for a moment, before slashing at you.""")
                  print("\n")
                  time.sleep(main.shortTime)
                  print("[You’ve taken Damage]")
                  main.dmgTracker += 1
                  print("\n")
                  time.sleep(main.shortTime)
                  print("""Luckily the assault is halted by its lack of energy. It stays in place, staring at you, hoping you come closer. Sadly you lost the ID Card in the process.""")
                  print("\n")
                  time.sleep(main.longTime)
                  print("""[You’ve lost the ID Card]""")
                  print("\n")
                  time.sleep(main.shortTime)
                  inventory.remove("ID Card")
                  optionList.remove("sceneTwo_Sub_Two")
                  robotInteraction()

               else:
                  print("\n")
                  print("Invalid option")
                  robotInteraction()

            case "4":
               print("\n")
               print("You chose 4")
               time.sleep(main.shortTime)
               print("\n")
               if main.dmgTracker == 0:
                  print("""You since something is off with it. Before it has the chance to do anything, you quickly slash at it with your sword, slicing it in two.""")
                  

               else:
                  print("""Now knowing it’s a threat, you dispatch it swiftly with your sword. Its slow movements make this easy.""")
                  

               time.sleep(main.shortTime)
               print("\n")
               main.warTraker += 1
               return main.warTraker, main.dmgTracker, main.pinkcomKnown, main.suspicionTracker

    else:
            print("\n")
            print("Invalid option")
            robotInteraction()

    return main.warTraker, main.dmgTracker, main.pinkcomKnown, main.suspicionTracker

##-------------## Scene Three ##-------------##

def sceneThree():
   options = 3

   print("""Choices:
  1. [Interact] Head left
  2. [Interact] Head right""")
   if main.suspicionTracker == 0:
      if "sceneThree_One" in optionList:
        print("  3. [Gesture] Look towards a nearby camera in confusion")

   entry = input("Enter the number corresponding to your choice: ")
   entryCheck = check.validEntry(entry, options)
   if entryCheck:
      match entry:
        case "1":
         print("\n")
         print("You chose 1")
         time.sleep(main.shortTime)
         print("\n")
         print("""You head left.""")
         main.path = "Left"
         time.sleep(main.shortTime)
         print("\n")
         return main.path

        case "2":
         print("\n")
         print("You chose 2")
         time.sleep(main.shortTime)
         print("\n")
         print("""You head right.""")
         main.path = "Right"
         time.sleep(main.shortTime)
         print("\n")
         return main.path

        case "3":
         if main.suspicionTracker == 0:
            if "sceneThree_One" in optionList:
              print("\n")
              print("You chose 3")
              time.sleep(main.shortTime)
              print("\n")
              print("""“Stop looking over here, I don’t have an answer for you! Ignore Right and go Left!”""")
              time.sleep(main.shortTime)
              optionList.remove("sceneThree_One")
              sceneThree()

            else:
               print("\n")
               print("Invalid option")
               sceneThree()

         else:
            print("\n")
            print("Invalid option")
            sceneThree()

   else:
      print("\n")
      print("Invalid option")
      sceneThree()

   return main.path

##-------------## Scene Four ##-------------##

def sceneFour():
    options = 3

    print("""Choices:
  1. [Attack] Charge at the nearest one
  2. [Attack] Deal with the ones that haven’t noticed you""")
    if main.dmgTracker == 0:
        print("  3. [Attack] Attack the strongest looking one first")

    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options)

    if entryCheck:
        match entry:
            case "1":
                print("\n")
                print("You chose 1")
                time.sleep(main.shortTime)
                print("\n")
                print("""You start off simple by taking out the closest one. Due to the element of surprise, it is destroyed with no effort. The three nearby charge at you. You take some damage but are able to destroy them, too.""")
                print("\n")
                time.sleep(main.longTime)
                print("[You’ve taken Damage]")
                main.dmgTracker += 1
                print("\n")
                time.sleep(main.shortTime)
                main.warTraker, main.dmgTracker = aggressiveFight()
                return main.warTraker, main.dmgTracker

            case "2":
                print("\n")
                print("You chose 2")
                time.sleep(main.shortTime)
                print("\n")
                print("""You use the element of surprise to your advantage, taking out five with quick ease.""")
                print("\n")
                time.sleep(main.shortTime)
                if main.dmgTracker > 0:
                    print("""However, the damage from earlier has had some effect on your movement, causing you to slip and fall.""")
                    print("\n")
                    time.sleep(main.shortTime)
                main.warTraker, main.dmgTracker = sneakyFight()
                return main.warTraker, main.dmgTracker

            case "3":
                if main.dmgTracker == 0:
                   print("\n")
                   print("You chose 3")
                   time.sleep(main.shortTime)
                   print("\n")
                   print("""You waste no time focusing on the one that looks the toughest. It was hard having to deal with them and the four others that joined in mid-fight. You end up taking a heavy hit, but you were able to finish them all off. Luckily for you, the majority of the robots seem to have been under the big ones' control. 4 of them stop moving.""")
                   print("\n")
                   time.sleep(main.longTime)
                   print("[You’ve taken Heavy Damage]")
                   main.dmgTracker += 2
                   print("\n")
                   time.sleep(main.shortTime)
                   print("There are 3 robots left.")
                   print("\n")
                   time.sleep(main.shortTime)
                   main.warTraker, main.dmgTracker = leaveFight()
                   return main.warTraker, main.dmgTracker

                else:
                    print("\n")
                    print("Invalid option")
                    sceneFour()

    else:
        print("\n")
        print("Invalid option")
        sceneFour()
    return main.warTraker, main.dmgTracker


##-------------## Aggressive Fight ##-------------##

def aggressiveFight():
    options = 2

    print("""Choices:
  1. [Attack] Keep the pressure on and attack the next cluster of robots.
  2. [Attack] Wait for them to come to you.""")

    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options) 
    if entryCheck:
        match entry:
           case "1":
               print("\n")
               print("You chose 1")
               time.sleep(main.shortTime)
               print("\n")
               print("""Keep it coming. You’re not scared! You take out another four at the cost of taking more damage.""")
               print("\n")
               time.sleep(main.shortTime)
               print("[You’ve taken Damage]")
               main.dmgTracker += 1
               print("\n")
               time.sleep(main.shortTime)
               print("There are 4 robots left.")
               print("\n")
               time.sleep(main.shortTime)
               main.warTraker, main.dmgTracker = leaveFight()
               return main.warTraker, main.dmgTracker
   
           case "2":
               print("\n")
               print("You chose 2")
               time.sleep(main.shortTime)
               print("\n")
               print("""You patently wait for them to attack. Your calm approach lets you take out four without putting yourself in danger.""")
               print("\n")
               time.sleep(main.longTime)
               print("There are 4 robots left.")
               print("\n")
               time.sleep(main.shortTime)
               main.warTraker, main.dmgTracker = leaveFight()
               return main.warTraker, main.dmgTracker

    else:
       print("\n")
       print("Invalid option")
       aggressiveFight()

    return main.warTraker, main.dmgTracker

##-------------## Sneaky Fight ##-------------##

def sneakyFight():
    options = 3
    proneCheck = False
    defendCheck = False
   ##---## Checks if you've taken damage and sets you prone if so ##---##
    if main.dmgTracker > 0:
        proneCheck = True

    print("""Choices:
  1. [Attack] Attack the ones coming""")
    if proneCheck:
        print("  2. [Interact] Get up")
        if "sneakyFight_Three" in optionList:
            print("  3. [Interact] Defend against the ones coming")

    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options) 
    if entryCheck:
        match entry:
           case "1":
            print("\n")
            print("You chose 1")
            time.sleep(main.shortTime)
            if proneCheck:
               print("\n")
               print("""The four of them beat you while you’re done. You struggled to fight back, and were able to destroy them in the end and get up from the floor.""")
               print("\n")
               time.sleep(main.longTime)
               print("[You’ve taken Heavy Damage]")
               print("\n")
               time.sleep(main.longTime)
               main.dmgTracker += 2

            else:
               print("\n")
               print("""You destroy the four with no issue.""")
               print("\n")
               time.sleep(main.shortTime)
               
            print("There are 4 robots left.")
            print("\n")
            time.sleep(main.shortTime)
            main.warTraker, main.dmgTracker = leaveFight()
            return main.warTraker, main.dmgTracker

           case "2":
               if proneCheck:
                  print("\n")
                  print("You chose 2")
                  time.sleep(main.shortTime)
                  if not defendCheck:
                     print("\n")
                     print("""You pull yourself up, but are attacked while doing so.""")
                     print("\n")
                     time.sleep(main.shortTime)
                     print("[You’ve taken Damage]")
                     main.dmgTracker += 1

                  else:
                     print("\n")
                     print("""You pull yourself up.""")
                     proneCheck = False

               else:
                  print("\n")
                  print("Invalid option")
                  sneakyFight()

           case "3":
               if proneCheck:
                 if "sneakyFight_Three" in optionList:
                     print("\n")
                     print("You chose 3")
                     time.sleep(main.shortTime)
                     print("\n")
                     print("""You swiftly roll out of the way of the incoming attacks.""")
                     defendCheck = True
                     optionList.remove("sneakyFight_Three")
                     sneakyFight()

                 else:
                     print("\n")
                     print("Invalid option")
                     sneakyFight()

               else:
                  print("\n")
                  print("Invalid option")
                  sneakyFight()
                  

    else:
       print("\n")
       print("Invalid option")
       sneakyFight()
       
    return main.warTraker, main.dmgTracker

##-------------## Leave Fight ##-------------##

def leaveFight():
    options = 2

    print("""Choices:
  1. [Attack] Remove the last ones
  2. [Interact] Leave through the exit""")
   
    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options)
    if entryCheck:
       match entry:
          case "1":
             print("\n")
             print("You chose 1")
             time.sleep(main.shortTime)
             print("\n")
             if main.dmgTracker > 2:
                print("""Your injuries are catching up to you. You struggle to take out the last of them, but take on more damage in the process.""")
                print("\n")
                time.sleep(main.longTime)
                print("""[You’ve taken Damage]""")
                main.dmgTracker += 1
                print("\n")
                time.sleep(main.shortTime)
                if main.dmgTracker >= 4:
                   print("""As you leave, you begin to notice your vision fading. Seems like you’ve taken too much damage to continue on. You collapse to the floor.""")
                   print("\n")
                   time.sleep(main.longTime)
                   print("[You’ve been Destroyed]")
                   print("\n")
                   time.sleep(main.longTime)
                   ##---## Ending Scene Here ##---##
                   deathScene()
                   return main.warTraker, main.dmgTracker

                else:
                   print("""There are no more left.""")
                   main.warTraker += 1
                   print("\n")
                   time.sleep(main.longTime)
                   ##---## Ending Scene Here ##---##
                   return main.warTraker, main.dmgTracker

             else:
                print("""They pose little challenge to you. You destroy them with ease.""")
                print("\n")
                time.sleep(main.shortTime)
                main.warTraker += 1
                ##---## Ending Scene Here ##---##
                return main.warTraker, main.dmgTracker
                   

          case "2":
             print("\n")
             print("You chose 2")
             time.sleep(main.shortTime)
             print("\n")
             if main.dmgTracker > 2:
               print("""You decide to run past them now that there aren’t that many left, but your injuries have caught up to you. Your leg haywires, causing you to trip. The last four beat you while you’re down.""")
               print("\n")
               time.sleep(main.longTime)
               if main.dmgTracker >= 4:
                  print("""You were too weak to fight back…""")
                  print("\n")
                  time.sleep(main.longTime)
                  print("[You’ve been Destroyed]")
                  print("\n")
                  time.sleep(main.longTime)
                  ##---## Ending Scene Here ##---##
                  deathScene()
                  return main.warTraker, main.dmgTracker

               else:
                  print("""You struggled to fight back, but you were able to destroy them in the end.""")
                  print("\n")
                  time.sleep(main.shortTime)
                  print("""[You’ve taken Heavy Damage]""")
                  main.dmgTracker += 2
                  if main.dmgTracker >= 4:
                     print("\n")
                     time.sleep(main.shortTime)
                     print("""As you leave, you begin to notice your vision fading. Seems like you’ve taken too much damage to continue on. You collapse to the floor.""")
                     print("\n")
                     time.sleep(main.longTime)
                     print("[You’ve been Destroyed]")
                     print("\n")
                     time.sleep(main.longTime)
                     ##---## Ending Scene Here ##---##
                     deathScene()
                     return main.warTraker, main.dmgTracker
   
                  else:
                     print("\n")
                     time.sleep(main.shortTime)
                     main.warTraker += 1
                     ##---## Ending Scene Here ##---##
                     return main.warTraker, main.dmgTracker
             else:
                print("You decide to run past them now that there aren’t that many left. You have no trouble doing so.")
                print("\n")
                time.sleep(main.longTime)
                ##---## Ending Scene Here ##---##
                return main.warTraker, main.dmgTracker
   
    else:
      print("\n")
      print("Invalid option")
      leaveFight()

    return main.warTraker, main.dmgTracker

##-------------## Scene Five ##-------------##

def sceneFive():
    options = 5

    print("""Choices:
  1. [Gesture] Indicate you’re just passing through
  2. [Gesture] Give a thumbs up
  3. [Gesture] Point to your sword
  4. [Attack] Destroy them""")
    if "sceneFive_ID" in optionList:
        print("  5. [Item] Show them the ID Card")

    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options)
    if entryCheck:
        match entry:
            case "1":
                print("\n")
                print("You chose 1")
                time.sleep(main.shortTime)
                print("\n")
                print("""You make a walking motion with your fingers.""")
                time.sleep(main.shortTime)
                print("\n")
                print("""“I s-see… no voice box or is-s-s it broken-n? What-t-tever the matter is it is sham-me you are just pas-s-ssing through.”""")
                time.sleep(main.longTime)
                print("\n")
                print("""“I wis-s-sh you luck on your t-t-travels.”""")
                ##---## Ending Scene Here ##---##
                return main.heroTracker, main.breakerTracker

            case "2":
                print("\n")
                print("You chose 2")
                time.sleep(main.shortTime)
                print("\n")
                print("""You do just that, giving the old bot a well mannered thumbs up.""")
                time.sleep(main.shortTime)
                print("\n")
                print("""“...r-right…”""")
                time.sleep(main.shortTime)
                print("\n")
                print("""“Well, en-njoy your t-t-time in town.”""")
                time.sleep(main.shortTime)
                print("\n")
                print("""The old bot awkwardly bows before turning around and leaving. Kind of quick to give up there, pal…""")
                time.sleep(main.longTime)
                print("\n")
                main.heroTracker = townScene()
                return main.heroTracker, main.breakerTracker

            case "3":
                print("\n")
                print("You chose 3")
                time.sleep(main.shortTime)
                print("\n")
                print("""“Hm? A Flathead S-sword? Having a Fixer w-w-weapon with you should-d mean you’re a F-f-fixer, right?”""")
                time.sleep(main.longTime)
                print("\n")
                print("""You nod your head.""")
                time.sleep(main.shortTime)
                print("\n")
                print("""“Won-nderful n-n-news! F-father brought-t-t us a Fixer. I s-s-shall take my l-leave, but please s-stay as long as-s you need-d-d. Do vis-sit the shrine whil-l-le you’re here.”""")
                time.sleep(main.longTime)
                print("\n")
                print("""The old bot bows before heading off.""")
                time.sleep(main.shortTime)
                print("\n")
                main.heroTracker = townScene()
                return main.heroTracker, main.breakerTracker

            case "4":
                print("\n")
                print("You chose 4")
                time.sleep(main.shortTime)
                print("\n")
                print("""An easy target. Friendly or not, a robot that isn’t you is a threat.""")
                time.sleep(main.shortTime)
                print("\n")
                print("""You quickly slash them with your sword, destroying it in one fell swoop. The other residents begin to panic. No matter, they’re next.""")
                time.sleep(main.longTime)
                print("\n")
                print("""The town had no defenses, so it took little time to deal with the rest. You leave a destroyed town behind as you exit.""")
                time.sleep(main.longTime)
                print("\n")
                main.breakerTracker += 1
                main.heroTracker = townScene()
                return main.heroTracker, main.breakerTracker

            case "5":
                if "ID Card" in inventory:
                   if "sceneFive_ID" in optionList:
                       print("\n")
                       print("You chose 5")
                       time.sleep(main.shortTime)
                       print("\n")
                       print("You take out the ID Card and hold it out towards them.")
                       time.sleep(main.shortTime)
                       print("\n")
                       print("""“Oh? D-didn’t think I’d see one of thos-se again-n-n. I’m sorry to s-say, but I don’t think-k it will be much h-help here. Father t-turned off most of the ID locked-d doors. They s-s-saw no need to have t-them using up energy.”""")
                       time.sleep(main.longTime)
                       print("\n")
                       print("""“I c-can take it off-f-f your hands if you w-want. In return I c-can give you a-a-a Fuse. It should help-p you in the fut-ture.”""")
                       time.sleep(main.longTime)
                       print("\n")
                       idTrade()
                       optionList.remove("sceneFive_ID")
                       sceneFive()
   
                   else:
                       print("\n")
                       print("Invalid option")
                       sceneFive()

                else:
                    print("\n")
                    print("Invalid option")
                    sceneFive()

    else:
        print("\n")
        print("Invalid option")
        sceneFive()
       
    return main.heroTracker, main.breakerTracker

##-------------## ID Trade ##-------------##

def idTrade():
    options = 2

    print("""Choices:
  1. [Gesture] Give a thumbs up
  2. [Gesture] Give a thumbs down""")
    
    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options)
    if entryCheck:
        match entry:
            case "1":
                print("\n")
                print("You chose 1")
                time.sleep(main.shortTime)
                print("\n")
                print("""“W-wonderful! Here you g-go.”""")
                time.sleep(main.longTime)
                print("\n")
                print("""[You’ve lost the ID Card]""")
                inventory.remove("ID Card")
                print("\n")
                print("""[You’ve collected a Fuse]""")
                inventory.append("Fuse")
                print("\n")
                time.sleep(main.shortTime)
                print("""“You haven’t-t said why you are h-here yet, t-t-traveler.”""")
                time.sleep(main.shortTime)
                print("\n")

            case "2":
                print("\n")
                print("You chose 2")
                time.sleep(main.shortTime)
                print("\n")
                print("""“A s-s-shame…”""")
                time.sleep(main.shortTime)
                print("\n")
                print("""“You haven’t-t said why you are h-here yet, t-t-traveler.”""")
                time.sleep(main.shortTime)
                print("\n")

    else:
        print("\n")
        print("Invalid option")
        idTrade()


##-------------## Town ##-------------##

def townScene():
    options = 3

    print("""Choices:
  1. [Interact] Leave the town
  2. [Interact] Check out the shops""")
    if "sceneFive_Shrine" in optionList:
        print("  3. [Interact] Head to the shrine")

    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options)
    if entryCheck:
       match entry:
        case "1":
            print("\n")
            print("You chose 1")
            time.sleep(main.shortTime)
            print("\n")
            print("""Welp, you’ve seen enough. Time to move on.""")
            time.sleep(main.shortTime)
            print("\n")
            ##---## Ending Scene Here ##---##
            return main.heroTracker

        case "2":
            print("\n")
            print("You chose 2")
            time.sleep(main.shortTime)
            print("\n")
            print("""You stop by a store selling tech. Their wares look old, but they can still have their uses. A rusted bot from behind the counter calls out to you.""")
            time.sleep(main.shortTime)
            print("\n")
            print("""“Ya here just to window shop, pal?”""")
            time.sleep(main.shortTime)
            print("\n")
            shopScene()
            main.heroTracker = townScene()

        case "3":
            if "sceneFive_Shrine" in optionList:
               print("\n")
               print("You chose 3")
               time.sleep(main.shortTime)
               print("\n")
               print("""There seems to be a shrine somewhere in the center of town. It’s not uncommon for a settlement to worship something. Most times it’s the AI that resides in the area, and due to the lack of much outside influence, that’s probably what’s happening here.""") 
               time.sleep(main.longTime)
               print("\n")
               print("""You arrive at the shrine. It’s about as you expected for a scrap town like this, a simple roof being supported by pillars with an altar in the center. There are bots huddled around, praying towards the altar. None of them pay you any mind.""")
               time.sleep(main.longTime)
               print("\n")
               optionList.remove("sceneFive_Shrine")
               main.heroTracker = shrineScene()
               main.heroTracker = townScene()

            else:
                print("\n")
                print("Invalid option")
                main.heroTracker = townScene()

    else:
        print("\n")
        print("Invalid option")
        main.heroTracker = townScene()
       
       
    return main.heroTracker

##-------------## Shop ##-------------##

def shopScene():
    options = 5

    print("""Choices:
  1. [Interact] Leave the shop""")
    if "ID Card" in inventory:
        print("""  2. [Item] Trade the ID Card for a Fuse
    3. [Item] Trade the ID Card for Chains""")
    if "Fuse" in inventory:
        print("""  4. [Item] Trade the Fuse for a Cluster Bomb
    5. [Item] Trade the Fuse for a Repair Kit""")

    entry = input("Enter the number corresponding to your choice: ")
    entryCheck = check.validEntry(entry, options)
    if entryCheck:
        match entry:
            case "1":
                print("\n")
                print("You chose 1")
                time.sleep(main.shortTime)
                print("\n")
                print("""You leave the shop.""")
                time.sleep(main.shortTime)
                print("\n")

            case "2":
                if "ID Card" in inventory:
                    print("\n")
                    print("You chose 2")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""“Aye. That works for me, pal.”""")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""[You’ve lost the ID Card]""")
                    inventory.remove("ID Card")
                    print("\n")
                    print("""[You’ve collected a Fuse]""")
                    inventory.append("Fuse")
                    print("\n")
                    time.sleep(main.shortTime)
                    shopScene()

                else:
                    print("\n")
                    print("Invalid option")
                    shopScene()

            case "3":
                if "ID Card" in inventory:
                    print("\n")
                    print("You chose 3")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""“Aye. That works for me, pal.”""")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""[You’ve lost the ID Card]""")
                    inventory.remove("ID Card")
                    print("\n")
                    print("""[You’ve collected some Chains]""")
                    inventory.append("Chains")
                    print("\n")
                    time.sleep(main.shortTime)
                    shopScene()

                else:
                    print("\n")
                    print("Invalid option")
                    shopScene()

            case "4":
                if "Fuse" in inventory:
                    print("\n")
                    print("You chose 4")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""“Aye. That works for me, pal.”""")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""[You’ve lost the Fuse]""")
                    inventory.remove("Fuse")
                    print("\n")
                    print("""[You’ve collected a Cluster Bomb]""")
                    weapons.append("Cluster Bomb")
                    print("\n")
                    time.sleep(main.shortTime)
                    shopScene()

                else:
                    print("\n")
                    print("Invalid option")
                    shopScene()

            case "5":
                if "Fuse" in inventory:
                    print("\n")
                    print("You chose 5")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""“Aye. That works for me, pal.”""")
                    time.sleep(main.shortTime)
                    print("\n")
                    print("""[You’ve lost the Fuse]""")
                    inventory.remove("Fuse")
                    print("\n")
                    print("""[You’ve collected a Repair Kit]""")
                    inventory.append("Repair Kit")
                    print("\n")
                    time.sleep(main.shortTime)
                    shopScene()

                else:
                    print("\n")
                    print("Invalid option")
                    shopScene()

    else:
        print("\n")
        print("Invalid option")
        shopScene()


##-------------## Shrine ##-------------##

def shrineScene():
     options = 4

     print("""Choices:
  1. [Interact] Leave""")
     if "shrine_Two" in optionList:
        print("  2. [Interact] Investigate the altar")
     if "shrine_Three" in optionList:
         print("  3. [Interact] Eavesdrop on their prayers")
     if "spearSeen" in optionList:
        if "shrine_Four" in optionList:
            print("  4. [Interact] Take the Philipsear")

     entry = input("Enter the number corresponding to your choice: ")
     entryCheck = check.validEntry(entry, options)
     if entryCheck:
          match entry:
            case "1":
                 print("\n")
                 print("You chose 1")
                 time.sleep(main.shortTime)
                 print("\n")
                 print("""Welp, you’ve seen enough.""")
                 time.sleep(main.shortTime)
                 print("\n")
                 return main.heroTracker

            case "2":
                 if "shrine_Two" in optionList:
                     print("\n")
                     print("You chose 2")
                     time.sleep(main.shortTime)
                     print("\n")
                     print("""You notice something sitting atop the altar. You begin making out its form as you get close. It’s a Philipspear, a Fixer weapon. Hanging off of it are red ropes with bells attached at the end. They’re treating it like a holy relic.""")
                     time.sleep(main.longTime)
                     print("\n")
                     print("""To think you would find a Fixer weapon here. This factory is full of surprises.""")
                     time.sleep(main.shortTime)
                     print("\n")
                     optionList.append("spearSeen")
                     optionList.remove("shrine_Two")
                     main.heroTracker = shrineScene()

                 else:
                     print("\n")
                     print("Invalid option")
                     main.heroTracker = shrineScene()

            case "3":
                 if "shrine_Three" in optionList:
                     print("\n")
                     print("You chose 3")
                     time.sleep(main.shortTime)
                     print("\n")
                     print("""You listen in on what they are praying for and to whom.""")
                     time.sleep(main.shortTime)
                     print("\n")
                     print("""They are praying to a figure they call ‘Father’. You might know who this Father is.""")
                     time.sleep(main.shortTime)
                     print("\n")
                     print("""Their prayers are almost all about helping their town survive and thrive, as well as eliminating the Pinkcom robots. Seems they are left unanswered.""")
                     time.sleep(main.longTime)
                     print("\n")
                     optionList.remove("shrine_Three")
                     main.heroTracker = shrineScene()

                 else:
                     print("\n")
                     print("Invalid option")
                     main.heroTracker = shrineScene()

            case "4":
                 if "spearSeen" in optionList:
                     if "shrine_Four" in optionList:
                          print("\n")
                          print("You chose 4")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""You get closer to the Philipspear.""")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""One of the worshipers takes notice of the Flathead sword on your back. They stop praying and gather the attention of the others. You enter high alert thinking you just upset them. They all begin speaking in unison.""")
                          time.sleep(main.longTime)
                          print("\n")
                          print("""“Father has gifted us a Fixer. Our prayers have been answered.”""")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""One of them walks up to the altar, grabbing the Philipspear.""")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""“Our prayers have been answered.”""")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""They turn to you and kneel, offering you the Philipspear.""")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""“Our prayers have been answered.”""")
                          time.sleep(main.shortTime)
                          print("\n")
                          print("""It would be rude to refuse, so you take the Philipspear. The worshippers return to what they were doing, as if what just conspired never happened.""")
                          time.sleep(main.longTime)
                          print("\n")
                          print("""[You’ve obtained the Philipspear]""")
                          time.sleep(main.longTime)
                          print("\n")
                          weapons.append("Philipsear")
                          main.heroTracker += 1
                          optionList.remove("shrine_Four")
                          main.heroTracker = shrineScene()

                     else:
                        print("\n")
                        print("Invalid option")
                        main.heroTracker = shrineScene()

                 else:
                     print("\n")
                     print("Invalid option")
                     main.heroTracker = shrineScene()

     else:
        print("\n")
        print("Invalid option")
        main.heroTracker = shrineScene()

     return main.heroTracker

##-------------## Death Scene ##-------------##
def deathScene():
    print("""You've become another footnote on the history of the Mason Co Robotic Facility. You are eventually forgotten…""")
    time.sleep(main.longTime)
    print("\n")
    print("""[The End]""")
    sys.exit()

##-------------## Endings ##-------------##

def endingScene():
      if main.path == "Left":
       if main.suspicionTracker ==5:
          print("""You’ve left the silo. The fight was hard, but you’ve never left more alive. Well as much as a robot can be. It’s nice not having a care in the world. You’ve made a decision. This place will become your playground! Who cares if you’ve pissed off the AI running the place? You’re free to do what you want!""")
          time.sleep(main.longTime)
          print("\n")
          print("""You march forward deeper into the factory, enjoying yourself every step of the way.""")
          time.sleep(main.longTime)
          print("\n")
          print("""[Ending 1: Renegade]""")

       elif main.warTraker == 2:
         print("""You’ve left the silo.""")
         time.sleep(main.shortTime)
         print("\n")
         print("""“Great job! You had me worried there for a second. Let’s continue on, we should be there soon.”""")
         time.sleep(main.longTime)
         print("\n")
         print("""It’s talking again, whatever. As long as you get to fight more, that’s all that matters. If you help out along the way, great. If not, well, you’re still here to fight.""")
         time.sleep(main.longTime)
         print("\n")
         print("""You continue following the AI’s path, destroying anything that gets in your way.""")
         time.sleep(main.longTime)
         print("\n")
         print("""[Ending 2: War]""")

       else:
          print("""You’ve left the silo.""")
          time.sleep(main.shortTime)
          print("\n")
          print("""“Great job! You had me worried there for a second. Let’s continue on, we should be there soon.”""")
          time.sleep(main.longTime)
          print("\n")
          print("""You give a thumbs up and follow the path ahead.""")
          time.sleep(main.longTime)
          print("\n")
          print("""[Ending 5a: Fixer]""")

      else:
        if main.breakerTracker == 2:
          print("""Nothing feels better than snuffing the life out of a fellow robot. You wonder if there are any more towns in this factory. It is massive afterall.""")
          time.sleep(main.longTime)
          print("\n")
          print("""You imagine how the AI must be feeling seeing you slaughter one of their towns. The anger, the helplessness. It fills you with joy.""")
          time.sleep(main.longTime)
          print("\n")
          print("""[Ending 3: Breaker]""")

        elif main.heroTracker == 1:
          print("""After traveling a mile out from the town, the AI comes back.""")
          time.sleep(main.shortTime)
          print("\n")
          print("""“Sorry. I didn’t want you to see that.”""")
          time.sleep(main.shortTime)
          print("\n")
          print("""You look towards the nearest camera and tilt your head.""")
          time.sleep(main.shortTime)
          print("\n")
          print("""“I felt ashamed about not being able to help them, so I just ignored it. Hoping they can survive on their own. They did for a while, but…”""")
          time.sleep(main.longTime)
          print("\n")
          print("""“Their town was bigger and had more residents. However, due to the poor condition of my facility, they had to deal with many hardships. I’m hoping that you can be my… no… our solution. That is if you’re okay with that.”""")
          time.sleep(main.longTime)
          print("\n")
          print("You give a thumbs up.")
          time.sleep(main.shortTime)
          print("\n")
          print("""“Thank you.”""")
          time.sleep(main.shortTime)
          print("\n")
          print("You continue forward filled with a new found determination.")
          time.sleep(main.shortTime)
          print("\n")
          print("""[Ending 4: Hero]""")

        else:
          print("""After traveling a mile out from the town, the AI comes back.""")
          time.sleep(main.shortTime)
          print("\n")
          print("""“Sorry. I didn’t want you to see that.”""")
          time.sleep(main.shortTime)
          print("\n")
          print("""You look towards the nearest camera and tilt your head.""")
          time.sleep(main.shortTime)
          print("\n")
          print("""“It’s nothing.”""")
          time.sleep(main.shortTime)
          print("\n")
          print("You give a thumbs up and follow the path ahead. The factory ain’t gonna fix itself after all.")
          time.sleep(main.longTime)
          print("\n")
          print("""[Ending 5b: Fixer]""")

      time.sleep(main.longTime)
      print("\n")
      print("""[To Be Continued]""")
      time.sleep(main.longTime)
      sys.exit()