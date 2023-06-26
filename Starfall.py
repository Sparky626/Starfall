#Created by Geovnanny Ortiz
#With the use of Visual Studio Code
import cmd,textwrap,sys,os,time
import random as rand
from preferredsoundplayer import *
screen_width = 100
#Makes items print slow as if someone was typing
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print(' ')
    print(' ')
#Player
#Sets up Player and Enemy Classes
class player:
  def __init__(self):
    self.name = ''
    self.guardianClass = ''
    self.hp = 0
    self.maxhp = 0
    self.attack = 0
    self.attackname = ''
    self.pots = 6
    self.location = 'Stasis Pod Chamber'
    self.enemiesdefeated = 0
    self.game_over = False
    self.music = ''
myPlayer = player()
class swarmThrall:
  def __init__(self):
    self.name = 'the Swarm Thrall'
    self.hp = 50
    self.maxhp = 50
    self.attack = 10
    self.attackname = 'Arc Claws'
thrallIG = swarmThrall()
class swarmAcolyte:
  def __init__(self):
    self.name = 'the Swarm Acolyte'
    self.hp = 80
    self.maxhp = 80
    self.attack = 20
    self.attackname = 'Soulfire Rifle'
acolyteIG = swarmAcolyte()
class swarmWizard:
  def __init__(self):
    self.name = 'the Swarm Wizard'
    self.hp = 100
    self.maxhp = 100
    self.attack = 30
    self.attackname = 'Darkness Blast'
wizardIG = swarmWizard()
class swarmKnight:
  def __init__(self):
    self.name = 'the Swarm Knight'
    self.hp = 100
    self.maxhp = 100
    self.attack = 30
    self.attackname = 'Swarm Shredder'
knightIG = swarmKnight()
class swarmOgre:
  def __init__(self):
    self.name = 'the Swarm Ogre'
    self.hp = 150
    self.maxhp = 150
    self.attack = 30
    self.attackname = 'Void Eye Blast'
ogreIG = swarmOgre()
class swarmCrota:
  def __init__(self):
    self.name = 'Alak-Hul the Swarm Commander'
    self.hp = 300
    self.maxhp = 300
    self.attack = 40
    self.attackname = 'the Axe of Alak-Hul'
crotaIG = swarmCrota()


def title_screen_selections():
  #Associates commands with actions
  option = input('> ')
  if option.lower() == ('play'):
    setup_game()
  elif option.lower() == ('help'):
    help_menu()
  elif option.lower() == ('quit'):
    sys.exit()
  while option.lower() not in ['play', 'help', 'quit']:
    print('Please enter a valid command.')
    option = input('> ')
    if option.lower() == ('play'):
      setup_game()
    elif option.lower() == ('help'):
      help_menu()
    elif option.lower() == ('quit'):
      sys.exit()

def title_screen():
  #Clears command prompt and creates a title screen for the game.
  os.system('cls')
  print('#######################')
  print('# Welcome to Starfall #')
  print('#######################')
  print('         -Play-        ')
  print('         -Help-        ')
  print('         -Quit-        ')
  print('### Inspired by the ###')
  print('## Destiny Franchise ##')
  title_screen_selections()

def help_menu():
#Creates a help menu when the help command is inputted into the title screen.
  print('   #################################  ')
  print('   #      Welcome to Starfall      #  ')
  print('   #################################  ')
  print('    -Use Up Down Left Right to Move-  ')
  print('       -Type to execute commands-     ')
  print('     -Use look command to inspect-    ')
  print('     -Use switch to change attack-    ')
  print('       -Use move command to move-     ')
  print('-Defeat one enemy in each room to win-')
  title_screen_selections()


#### DEPICTION OF THE MAP ####
#'''
#Bridge  Bridge Entrance... # Player Starts at Stasis Pod Chamber
#---------
#| | | | | Bridge Communications
#--------- 
#| | | | | Research Lab ...
#---------
#| | | | |
#---------
#| | | | |
#---------
#'''
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
DEFEATED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
#Determines whether or not the locations have been clsed.
defeated_places = {'Bridge Weapons Storage': False, 'Bridge Entrance': False, 'Bridge Command Deck': False, 'Bridge Communications': False,
                'Cafeteria': False, 'Stasis Pod Chamber': False, 'Lounging Area': False, 'Research Lab': False,
                'Engine Room Left Maintenance Panel': False, 'Engine Room Entrance': False, 'Engine Room Main Maintenance Panel': False, 'Engine Room Right Maintenance Panel': False, 
                'Storage Left Wing': False, 'Storage Entrance': False, 'Storage Loading Bay': False, 'Storage Right Wing': False
                }
#Creates a dictionary as the map for the game
zonemap = {
     'Bridge Weapons Storage':{
    ZONENAME:"Bridge Weapons Storage",
    DESCRIPTION :'Weapons storage incase of intruders on the Bridge',
    EXAMINATION : 'The weapons storage is empty and is covered in a mysterious goo.',
    DEFEATED : False,
    UP : '',
    DOWN : 'Cafeteria',
    LEFT : '',
    RIGHT : 'Bridge Entrance',
  },
  'Bridge Entrance':{
    ZONENAME: 'Bridge Entrance',
    DESCRIPTION : 'Where the ship is controlled, piloted, and jumped to hyperspace.',
    EXAMINATION : 'The bridge is deserted and there are no signs of life anywhere... What happened here?',
    DEFEATED : False,
    UP : '',
    DOWN : 'Stasis Pod Chamber',
    LEFT : 'Bridge Weapons Storage',
    RIGHT : 'Bridge Command Deck',
  },
  'Bridge Command Deck':{
    ZONENAME: 'Bridge Command Deck',
    DESCRIPTION : 'Where the ships commander is station and gives the other officers orders',
    EXAMINATION: 'The command deck has been trashed, the commanders chair is destroyed, aswell as any electronics.',
    DEFEATED : False,
    UP : '',
    DOWN : 'Lounging Area',
    LEFT : 'Bridge Entrance',
    RIGHT : 'Bridge Communications',
  },
  'Bridge Communications':{
    ZONENAME: 'Bridge Communications',
    DESCRIPTION : 'Where the tech officers would communicate to earth and send out distress signals.',
    EXAMINATION: 'The comms station has been smashed by something with an alarming amouunt of strength.',
    DEFEATED : False,
    UP : '',
    DOWN : 'Research Lab',
    LEFT : 'Bridge Command Deck',
    RIGHT : '',
  },
  'Cafeteria':{
    ZONENAME: 'Cafeteria',
    DESCRIPTION : 'You used to snack here with your fellow crew members, now there is no one to be found.',
    EXAMINATION: 'You notice egg like objects sitting where the food once was.',
    DEFEATED : False,
    UP : 'Bridge Weapons Storage',
    DOWN : 'Engine Room Left Maintenance Panel',
    LEFT : '',
    RIGHT : 'Stasis Pod Chamber',
  },
  'Stasis Pod Chamber':{
    ZONENAME: 'Stasis Pod',
    DESCRIPTION : 'This is where you woke up.',
    EXAMINATION: 'The stasis pods around you are all empty.',
    DEFEATED : False,
    UP : 'Bridge Entrance',
    DOWN : 'Engine Room Entrance',
    LEFT : 'Cafeteria',
    RIGHT : 'Lounging Area',
  },
  'Lounging Area':{
    ZONENAME: 'Lounging Area',
    DESCRIPTION : 'Crew members used to come here on their off time to play games or watch tv.',
    EXAMINATION: 'All the entertaiment electronics that used to line the walls have been destroyed.',
    DEFEATED : False,
    UP : 'Bridge Command Deck',
    DOWN : 'Engine Room Main Maintenance Panel',
    LEFT : 'Stasis Pod Chamber',
    RIGHT : 'Research Lab',
  },
  'Research Lab':{
    ZONENAME: 'Research Lab',
    DESCRIPTION : 'Crew scientists came up with new weapons and technological aids for the other crew members in this lab.',
    EXAMINATION: 'The tech here is covered in tons of goo, but some of it still functions displaying a blueprint for a high tech pulse rifle.',
    DEFEATED : False,
    UP : 'Bridge Communications',
    DOWN : 'Engine Room Right Maintenance Panel',
    LEFT : 'Lounging Area',
    RIGHT : '',
  },
  'Engine Room Left Maintenance Panel':{
    ZONENAME: '',
    DESCRIPTION : 'This panel controls engine cooling.',
    EXAMINATION: 'This panel has been covered with goo, but it seems like the engines cooling systems are operating correctly',
    DEFEATED : False,
    UP : 'Cafeteria',
    DOWN : 'Storage Left Wing',
    LEFT : '',
    RIGHT : 'Engine Room Entrance',
  },
  'Engine Room Entrance':{
    ZONENAME: '',
    DESCRIPTION : 'The engine room is where you can monitor the engine in case it needs repairs.',
    EXAMINATION: 'The engine room is dark with sparks flying across the floor, you can see green eyes staring at you from the back of the room.',
    DEFEATED : False,
    UP : 'Stasis Pod Chamber',
    DOWN : 'Storage Entrance',
    LEFT : 'Engine Room Left Maintenance Panel',
    RIGHT : 'Engine Room Main Maintenance Panel',
  },
  'Engine Room Main Maintenance Panel':{
    ZONENAME: '',
    DESCRIPTION : 'This panel measures velocity, pressure, and flow rate.',
    EXAMINATION: 'This panel is govered in Hive overgrowth better stay sharp.',
    DEFEATED : False,
    UP : 'Lounging Area',
    DOWN : 'Storage Loading Bay',
    LEFT : 'Engine Room Entrance',
    RIGHT : 'Engine Room Right Maintenance Panel',
  },
  'Engine Room Right Maintenance Panel':{
    ZONENAME: '',
    DESCRIPTION : 'This panel monitors fuel levels.',
    EXAMINATION: 'This panel has been smashed to pieces, how are we supposed to escape now?',
    DEFEATED : False,
    UP : 'Research Lab',
    DOWN : 'Storage Right Wing',
    LEFT : 'Engine Room Main Maintenance Panel',
    RIGHT : '',
  },
  'Storage Left Wing':{
    ZONENAME: '',
    DESCRIPTION : 'Stored in the left wing are medical supplies.',
    EXAMINATION: 'The crates that used to house the medical supplies have been destroyed and are empty.',
    DEFEATED : False,
    UP : 'Engine Room Left Maintenance Panel',
    DOWN : '',
    LEFT : '',
    RIGHT : 'Storage Entrance',
  },
  'Storage Entrance':{
    ZONENAME: 'Storage Entrance',
    DESCRIPTION : 'Where food, weapons, and medical supplies are stored.',
    EXAMINATION: 'Crates are destroyed all across the room, no crates remain intact.',
    DEFEATED : False,
    UP : 'Engine Room Entrance',
    DOWN : '',
    LEFT : 'Storage Left Wing',
    RIGHT : 'Storage Loading Bay',
  },
  'Storage Loading Bay':{
    ZONENAME: '',
    DESCRIPTION : 'A large crane was stored here used to load cargo into the bay.',
    EXAMINATION: 'The crane is ripped in half and there are exposed wires and sparks everywhere.',
    DEFEATED : False,
    UP : 'Engine Room Main Maintenance Panel',
    DOWN : '',
    LEFT : 'Storage Entrance',
    RIGHT : 'Storage Right Wing',
  },
  'Storage Right Wing':{
    ZONENAME: '',
    DESCRIPTION : 'Stored in the right wing are high tech firearms.',
    EXAMINATION: 'The crates that used to house the firearms have been destroyed and are empty.',
    DEFEATED : False,
    UP : 'Engine Room Right Maintenance Panel',
    DOWN : '',
    LEFT : 'Storage Loading Bay',
    RIGHT : '',
  },
}

def print_location():
  #Prints players location
  print('\n' + ('#' * (4 + len(myPlayer.location))))
  print('# ' + myPlayer.location.upper() + ' #')
  print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
  print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
  #Prompts the player to enter a command
  global mysong
  stopsound(mysong)
  mysong = soundplay('Prompt.wav')
  print('\n' + '====================================')
  print('What would you like to do?')
  action = input('> ')
  acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'switch', 'attackchange']
  while action.lower() not in acceptable_actions:
    print("Unknown action, try again.\n")
    action = input("> ")
  if action.lower() == 'quit':
    sys.exit()
  elif action.lower() in ['move', 'go', 'travel', 'walk']:
    player_move(action.lower())
  elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
    player_examine(action.lower())
  elif action.lower() in ['switch', 'attackchange']:
    player_switch()

def player_switch():
  #Allows the player to switch the name of their attacks depending on the element they choose
  os.system('cls')
  print_slow('Hello ' + myPlayer.name + ' !' )
  print_slow('What subclass would you like to switch to? (Void/Arc/Solar/Stasis)')
  selection = input('> ')
  if myPlayer.guardianClass.lower() == 'warlock':
    if selection.lower() == 'void':
      myPlayer.attackname = 'Nova Bomb'
    elif selection.lower() == 'arc':
      myPlayer.attackname = 'Chaos Reach'
    elif selection.lower() == 'solar':
      myPlayer.attackname = 'Daybreak'
    elif selection.lower() == 'stasis':
      myPlayer.attackname = 'Winters Wrath'
    else:
      player_switch()
  elif myPlayer.guardianClass.lower() == 'hunter':
    if selection.lower() == 'void':
      myPlayer.attackname = 'Shadowshot'
    elif selection.lower() == 'arc':
      myPlayer.attackname = 'Arc Staff'
    elif selection.lower() == 'solar':
      myPlayer.attackname = 'Golden Gun'
    elif selection.lower() == 'stasis':
      myPlayer.attackname = 'Silence and Squall'
    else:
      player_switch()
  else:
    if selection.lower() == 'void':
      myPlayer.attackname = 'Sentinel Shield'
    elif selection.lower() == 'arc':
      myPlayer.attackname = 'Fist of Havoc'
    elif selection.lower() == 'solar':
      myPlayer.attackname = 'Hammer of Sol'
    elif selection.lower() == 'stasis':
      myPlayer.attackname = 'Glacial Quake'
    else:
      player_switch()

def player_move(myAction):
  #Asks the player where they would like to move if they type in the move command when they are prompted to.
  ask = "Where would you like to move to?\n"
  dest = input(ask)
  if dest.lower() in ['up', 'north']:
    destination = zonemap[myPlayer.location][UP]
    if destination == '':
      print('You cannot move UP from this location.')
      prompt()
    else:
      movement_handler(destination)
  elif dest.lower() in ['left', 'west']:
   destination = zonemap[myPlayer.location][LEFT]
   if destination == '':
      print('You cannot move LEFT from this location.')
      prompt()
   else:
      movement_handler(destination)
  elif dest.lower() in ['right', 'east']:
    destination = zonemap[myPlayer.location][RIGHT]
    if destination == '':
      print('You cannot move RIGHT from this location.')
      prompt()
    else:
      movement_handler(destination)
  elif dest.lower() in ['down', 'south']:
   destination = zonemap[myPlayer.location][DOWN]
   if destination == '':
      print('You cannot move DOWN from this location.')
      prompt()
   else:
      movement_handler(destination)
    
  
  
def movement_handler(destination):
  #Prints the destination the player has moved to.
  print("\n" + "You have moved to the " + destination + ".")
  myPlayer.location = destination
  os.system('cls')
  print_location()
  

def player_examine(action):
  #Prints dialogue of the area if the enemy has not been defeated yet,
  if zonemap[myPlayer.location][DEFEATED] == True:
    print('')
    print_slow("You have already defeated the enemy in this zone.")
  else:
    print('')
    print_slow(zonemap[myPlayer.location][EXAMINATION])
    prefight()

def main_game_loop():
  #Begins the main game loop
  while myPlayer.game_over == False:
    prompt()

def setup_game():
  #Gives the player a class name and shows some intro dialogue
  global mysong
  stopsound(mysong)
  mysong = soundplay('GameSetup.wav')
  os.system('cls')
  print_slow('Eyes up guardian!')
  print_slow('You have been in cryosleep for too long, your ship, the Stronghold, has been overun by the Swarm.')
  print_slow('Who are the Swarm? An elite legion of Hive soldiers who are focused on erradicating everything in the galaxy.')
  print_slow('They arrived in the Sol system in the year 2675 while you were in cryosleep.')
  print_slow('It is the year 2680 and they have been wreaking havoc alongside the Hive for many years.')
  print_slow('Who am I? Oh I am just your Ghost, your personal AI, I woke you from cryosleep! I was sent here by the Traveler to aid in your escape and fight against the Swarm.')
  #Gives the player a name
  question1 = "Now tell me what's your name?"
  print_slow(question1)
  player_name = input("> ")
  print('')
  myPlayer.name = player_name
  #Gives the player their class
  print_slow('Hello! ' + player_name)
  print_slow("You have been chosen by the mysterious entity called the Traveler and it has given you extrodinary abilities that us Ghosts call the light!")
  question2 = "What class of light were you given when I woke you up? (warlock/hunter/titan)"
  print_slow(question2)
  player_class = input("> ")
  print('')
  valid_class = ['warlock', 'hunter', 'titan']
  if player_class.lower() in valid_class:
    myPlayer.guardianClass = player_class
    if player_class.lower() == 'warlock':
      print_slow('Ah a Warlock the wisest and strongest in magic of the classes.')
    elif player_class.lower() == 'hunter':
      print_slow('Ah a Hunter the fastest and most cunning of the classes.')
    else:
      print_slow('Ah a Titan the most brute and strongest of the classes.')
  else:
    while player_class.lower() not in valid_class:
      player_class = input("> ")
    if player_class.lower == 'warlock':
      print('Ah a Warlock the wisest and strongest in magic of the classes.')
    elif player_class.lower == 'hunter':
      print('Ah a Hunter the fastest and most cunning of the classes.')
    else:
      print('Ah a Titan the most brute and strongest of the classes.')
      
  #Gives player Stats
  if player_class.lower() == 'warlock':
    myPlayer.hp = 160
    myPlayer.maxhp = 160
    myPlayer.attack = 40 
    myPlayer.attackname = 'Nova Bomb'
  elif player_class.lower() == 'hunter':
    myPlayer.hp = 200
    myPlayer.maxhp = 200
    myPlayer.attack = 30
    myPlayer.attackname = 'Golden Gun'
  else:
    myPlayer.hp = 240
    myPlayer.maxhp = 240
    myPlayer.attack = 20 
    myPlayer.attackname = 'Hammer of Sol'
  print('')
  print('Commands = move/go/travel/walk/quit/examine/inspect/interact/look/switch/attackchange')
  print('')
  continueSpace = input('Press enter to begin your escape......')
  print("")
  os.system('cls')
  print("########################")
  print("#   Let's start Now!   #")
  print("########################")
  main_game_loop()

#Sets up Enemy to fight
def prefight():
  global enemy
  #Decides whether to give the player a random enemy or the boss enemy depending on how many enemies the player has defeated.
  if myPlayer.enemiesdefeated == 16:
    enemy = crotaIG
    print_slow("The Hive Prince emerges from the shadows.")
    print_slow("You engage him with extreme caution.....")
    continue1 = input('')
    fight()
  else:
    global mysong
    stopsound(mysong)
    mysong = soundplay('Fight.wav')
    #Gives the player a random enemy from the roster.
    enemynum = rand.randint(1,5)
    if enemynum == 1:
      enemy = thrallIG
    elif enemynum == 2:
      enemy = acolyteIG
    elif enemynum == 3:
      enemy = wizardIG
    elif enemynum == 4:
      enemy = knightIG
    elif enemynum == 5:
      enemy = ogreIG
    print_slow("Look out a " + enemy.name + " appeared!")
    print_slow(myPlayer.name + " engages the enemy.")
    continue1 = input(' ')
    fight()
  

def fight():
  os.system('cls')
  #Creates fight sequence against the enemy
  print_slow(myPlayer.name + " vs. " + enemy.name)
  playerHealth = str(myPlayer.hp)
  print('You have ' + playerHealth + ' health.')
  print("")
  enemyHealth = str(enemy.hp)
  print('The ' + enemy.name + ' has ' + enemyHealth + ' health.' )
  print("")
  print('What shall you do?')
  print("1.) Attack")
  print("2.) Use Healing Orb")
  print("3.) Run")
  option = input('')
  if option == '1':
    attack()
  elif option == '2':
    heal()
  elif option == '3':
    os.system('cls')
    print_slow('You escaped the ' + enemy.name + '.')
    prompt()
  else:
    fight()

def attack():
  print('')
  #Makes player and enemy do random damage in a range
  PAttack = rand.randint(myPlayer.attack / 2, myPlayer.attack)
  EAttack = rand.randint(enemy.attack / 2, enemy.attack)
  enemy.hp -= PAttack
  playerAttack = str(PAttack)
  enemyAttack = str(EAttack)
  print_slow('You attack the ' + enemy.name + ' with your ' + myPlayer.attackname + '!')
  print_slow('The attack does ' + playerAttack + ' damage!')
  if enemy.hp <= 0:
    win()
  else:
    myPlayer.hp -= EAttack
    print_slow('The ' + enemy.name + ' attacks you with ' + enemy.attackname + '!')
    print_slow('The attack does ' + enemyAttack + ' damage!')
    continue1 = input('')
    if myPlayer.hp <= 0:
      print_slow('You were consumed by the darkness......')
      print_slow('Game Over.....')
      sys.exit()
    else:
      fight()
def win():
  #Plays the win scenario after the enemy is defeated
  enemy.hp = enemy.maxhp
  print_slow(myPlayer.name + ' defeated ' + enemy.name)
  defeated_places[myPlayer.location] = True
  zonemap[myPlayer.location][DEFEATED] = True
  myPlayer.enemiesdefeated += 1
  myPlayer.attack += 2
  if myPlayer.enemiesdefeated == 16:
    continue1 = input('Press enter to Continue')
    boss()
  elif myPlayer.enemiesdefeated == 17:
    continue1 = input('Press enter to Continue')
    gamewin()
  else:    
    continue1 = input('Press enter to Continue')
    prompt()

  
def heal():
  print('')
  #Creates an option for the player to heal
  os.system('cls')
  if myPlayer.pots == 0:
      #Does not allow the player to heal if they do not have healing orbs.
      print_slow("You don't have any healing orbs!")
  else:
    if myPlayer.maxhp > myPlayer.hp:
      print_slow("You used a healing orb!")
      myPlayer.hp = myPlayer.maxhp
      myPlayer.pots -= 1
    else:
      #Does not allow the player to heal if they already are at max health
      print_slow("Using this orb will not restore your health.")
  fight()

def boss():
  #Sets up boss dialogue and music
  myPlayer.pots += 3
  global mysong
  stopsound(mysong)
  mysong = soundplay('FinalBoss.wav')
  os.system('cls')
  print_slow('The air turns cold........')
  print_slow('Alak-Hul: So you have defeated my entire army and you now challenge me?')
  print_slow('Alak-Hul: Pathetic, prepare to face my wrath....')
  print_slow('Ghost: On your 6 here he comes!!!!')
  prefight()


def gamewin():
  os.system('cls')
  global mysong
  stopsound(mysong)
  mysong = soundplay('GameEnd.wav')
  print_slow('You defeated any enemy that dared cross your path, and slayed the swarm commander.')
  print_slow('You repair the once infested Stonghold and pilot it to Earth to the Lost City where you are greeted with congratulations of your victory.')
  if myPlayer.guardianClass.lower() == 'warlock':
    print_slow('The Warlock Vanguard Ikora Rey greets you and hopes to work with you in the future to defeat other Hive Commanders.')
  elif myPlayer.guardianClass.lower() == 'hunter':
    print_slow('The Hunter Vanguard Cayde-6 greets you and states that he hopes to kick ass and take names with you in the future.')
  else:
    print_slow('The Titan Vanguard Zavala greets you and asks for your aid in defending the city from the coming enemies.')
  print_slow('A lot has changed since you were last on earth, it might take a bit to get used to it.')
  print_slow('Game Over!')
  continue1 = input('Thanks for Playing!')
mysong = soundplay('Title.wav')  
title_screen()
