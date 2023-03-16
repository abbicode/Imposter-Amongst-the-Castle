import tkinter as tk
from time import sleep
from sys import stdout, exit
import random
import sys
import time

def typewriter(message):
  for char in message: 
      sys.stdout.write(char)
      sys.stdout.flush()
      if char=="\n":
        time.sleep(0.12)
      elif char==".":
        time.sleep(0.12)
      elif char=="!":
        time.sleep(0.12)
      elif char=="?":
        time.sleep(0.12)
      elif char==",":
        time.sleep(0.07)
      else:
        time.sleep(0.025)

def answer(message): 
  while message not in "abAB" :
    message=str(input("Error, answer is not valid. Please enter 'a' or 'b'\n"))

def urmom(message): 
  while message!="1": 
    message=str(input("Error. Enter '1' to continue"))
  

message="WELCOME TO IMPOSTER AMONGST THE CASTLE"
typewriter(message)
#make all it print looks like print(work) put into typewriter, if it looks like print("a lot of words in quotes") don't 

print("""
      """)

players=[]
names=[]
mdec=[]
count=12

castlem=['King: EDMUND','Seamstress: WINIFRED','Maid1: MIRABEL ','Maid2: CELESTE','Cook: NEVILLE','Butler: BARTHOLOMEW','Doctor: AUGUST','Priest: IRVING','Knight1: MAXIM','Knight2: BARNABAS','Gardener: FERDINAND','Page: CHRYSANTHA']
castle2=[1,2,3,4,5,6,7,8,9,10,11,12]
beans=1
players=int(input("  Enter number of players (1-4): "))
while players<1 or players>4:
  players=int(input("  Error. Enter number of player (1-4): "))

for x in range(players):
  names.append(1+x)


print("""
      """)
if players==1: 
  mdec.append("Anabel")
  print("  Player 1: ",mdec[0])
  
elif players==2:
  mdec.append("Anabel")
  mdec.append("Juliette")
  print("  Player 1: ",mdec[0],"\n")
  print("  Player 2: ",mdec[1],"\n")
  
elif players==3: 
  mdec.append("Anabel")
  mdec.append("Juliette")
  mdec.append("Cassian")
  print("  Player 1: ",mdec[0],"\n")
  print("  Player 2: ",mdec[1],"\n")
  print("  Player 3: ",mdec[2],"\n")
  
elif players==4:
  mdec.append("Anabel")
  mdec.append("Juliette")
  mdec.append("Cassian")
  mdec.append("Sebastian")
  print("  Player 1: ",mdec[0],"\n")
  print("  Player 2: ",mdec[1],"\n")
  print("  Player 3: ",mdec[2],"\n")
  print("  Player 4: ",mdec[3],"\n")
  

loading="\n ...LOADING... \n"
typewriter(loading)

#add instructions on how to play the game and a description of the game

introduction=("Hello player/s, welcome to the game 'Imposter Amongst the Castle'. You will be detectives, if there are less than 4 players, than you will be playing with NPCs. In total, there are 4 main detectives, Anabel, Juliet, Cassian, and Sebastian. Once you enter the castle, you will interview 12 different castle members. After all the interviews are over, the voting process begins. After the first 2 voting processes *assuming you haven't gotten the killer yet*, you will be introduced to a game center and a store where you can purchase useful items. This game and store center will happen every intermission between the voting processes. There are riddles, questions and games. Please follow the directions later to play these. Although for the most part, all you need to enter is (a), (b), (c), (d), or a number. The goal of the game is to catch the killer as quick as you can, the longer it takes to find the killer, the more of a chance the killer finds you. Good luck in catching the killer!")

typewriter(introduction)

message=("\n\n\n...LOADING...\n\nYou and your friends are starving, but you have no money. You go to the local baker, Gisele, to steal some of her bread. She catches you in the act, but instead of yelling, she pulls you aside.\n\nGisele: You thieves have been stealing for years! It is a miracle I caught you all. You owe me 50,000 shillings for all the bread you have stolen. By the looks of 'ya, you probably don't got any money, right? Well, there’s a way you can repay your debts\n\nShe then points to a poster on the wall. \n\nYou walk over and read: Attention townsfolk and travelers! Queen Beatrice has mysteriously died on the morning of May 9th, and has not been found since then. Unfortunately, that is all the information we can give you. If you are interested in finding the cause of the murder and the culprit who committed this foul crime, you will be rewarded greatly. Entering may be dangerous so write your name at your own risk.")
typewriter(message)
if players==4: 
  print("\n\nAnabel: I'm not sure about entering, but it seems like we don't have a choice.\n")
  decision1=str(input("\n  (a) Guys, lets enter. I'm in.\n  (b) Sure I guess I will enter.\n"))
  answer(decision1)
  print("\nJuliette: Okay Anabel, you've entered?\nAnabel: Yes I have.")
  decision2=str(input("\n  (a) I'm in.\n  (b) Okay I will join too.\n"))
  answer(decision2)
  print("\nCassian: I see you've both entered.")
  decision3=str(input("\n  (a) I'll enter too. \n  (b) Ugh I guess I will join this.\n"))
  answer(decision3)
  print("Sebastian: Wow you guys all entered, I guess I have to join too.")
  decision4=str(input("\n  (a) I'll join.\n  (b) Lets figure out who murdered the queen.\n"))
  answer(decision4)
elif players==3: 
  print("\n\nAnabel: I'm not sure about entering, but it seems like we don't have a choice.\n")
  decision1=str(input("\n  (a) Guys, lets enter. I'm in.\n  (b) Sure I guess I will enter.\n ")) 
  answer(decision1)
  print("\nJuliette: Okay Anabel, you've entered?\nAnabel: yes I have.")
  decision2=str(input("\n  (a) I'm in.\n  (b) Okay I will join too.\n"))
  answer(decision2)
  print("\nCassian: I see you've both entered.")
  decision3=str(input("\n  (a) I'll enter too. \n  (b) Ugh I guess I will join this.\n"))
  answer(decision3)
  print("\nSebastian: Great guys! Lets figure out this murder.")
elif players==2: 
   print("\n\nAnabel: I'm not sure about entering, but it seems like we don't have a choice.\n")
   decision1=str(input("\n  (a) I'm in.\n  (b) Sure I guess I will enter.\n "))
   answer(decision1)
   print("\nJuliette: Okay Anabel, you've entered?")
   decision2=str(input("\n  (a) I guess I'm in too.\n  (b) Okay I will join too.\n"))
   answer(decision2)
   print("\nCassian: Great, lets find who murdered the queen.")
   print("\nSebastian: Let's do this thing.")
elif players==1: 
  print("\n\nAnabel: I'm not sure about entering, but it seems like I don't have a choice.\n")
  decision1=str(input("\n  (a) I'm in.\n  (b) Sure I guess I will enter.\n ")) 
  answer(decision1)
  print("\nJuliette: Okay Anabel, you've entered?\nAnabel: Yes, I have.")
  print("\nCassian: Great, let's find who murdered the queen.")
  print("\nSebastian: Let's do this thing.")
  
message=("\nGisele: Getting into the castle is going to be hard, but I have connections so I can get you in. Good luck thieves, I hope you catch the culprit so you will be able to pay back your debts. Let's not waste anymore time and get you guys to the castle, once again be careful you cannot trust anyone.\n")
typewriter(message)
typewriter(loading)
entercastle=("You and your friends have entered the castle successfully, there are twelve suspects, you will interview them all. Once all of the suspects have been interviewed, you may vote out who you believe the culprit is along with the 12 suspects. However, voting the wrong person will put them in exile. You may be able to get away the first time voting the wrong person, but it gets riskier as you go on. Good luck")
typewriter(entercastle)
typewriter(loading)

message=("\nKnight Maxim: Greetings travelers! I hope you enjoy your stay here at the castle. \n\nAnabel: *mutters* Yeah if we don't die first. \n\nJuliette: Shh Anabel, we have to keep it quiet, people can't find out we are detectives or else we might get targeted by the killer!")
typewriter(message)
successful=("\nGame: You detectives will be interviewing these twelve members of the court:\n")
typewriter(successful)



count=12
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
def urmom(message): 
  while message!="1": 
    message=str(input("Error. Enter '1' to continue"))



while count!=0: 
  print("You will now be interviewing the castle members")
  for x in range(players): 
      
   
      print("\n\n1 King: EDMUND\n\n2 Seamstress: WINIFRED\n\n3 Maid1: MIRABEL\n\n4 Maid2: CELESTE\n\n5 Cook: NEVILLE\n\n6 Butler: BARTHOLOMEW\n\n7 Doctor: AUGUST\n\n8 Priest: IRVING\n\n9 Knight1: MAXIM\n\n10 Knight2: BARNABAS\n\n11 Gardener: FERDINAND\n\n12 Page: CHRYSANTHA")  
      
      
      count-=1
      print(f"\n\n\n{mdec[x]}, please choose a character to interview and enter the corresponding number from the list (1-12)")
      waterbottle=str(input("\nGame: Enter your answer here: "))
      while waterbottle not in "123456789101112": 
        waterbottle=str(input("\n  Error. Please enter a valid number."))
      while waterbottle=="1" and a>0: 
        waterbottle=str(input("\n  Error. The king has already been spoken to, please choose another castle member"))
      while waterbottle=="2" and b>0: 
        waterbottle=str(input("\n  Error. The seamstress has already been spoken to, please choose another castle member"))
      while waterbottle=="3" and c>0: 
        waterbottle=str(input("\n  Error. The maid, Mirabel, has already been spoken to, please choose another castle member"))
      while waterbottle=="4" and d>0: 
        waterbottle=str(input("\n  Error. The maid, Celeste, has already been spoken to, please choose another castle member"))
      while waterbottle=="5" and e>0: 
        waterbottle=str(input("\n  Error. The the cook has already been spoken to, please choose another castle member"))
      while waterbottle=="6" and f>0: 
        waterbottle=str(input("\n  Error. The butler has already been spoken to, please choose another castle member"))
      while waterbottle=="7" and g>0: 
        waterbottle=str(input("\n  Error. The doctor has already been spoken to, please choose another castle member"))
      while waterbottle=="8" and h>0: 
        waterbottle=str(input("\n  Error. The priest has already been spoken to, please choose another castle member"))
      while waterbottle=="9" and i>0: 
        waterbottle=str(input("\n  Error. The knight, Maxim,  has already been spoken to, please choose another castle member"))
      while waterbottle=="10" and j>0: 
        waterbottle=str(input("\n  Error. The knight, Barnabas, has already been spoken to, please choose another castle member"))
      while waterbottle=="11" and k>0: 
        waterbottle=str(input("\n  Error. The gardener has already been spoken to, please choose another castle member"))
      while waterbottle=="12" and l>0: 
        waterbottle=str(input("\n  Error. The page has already been spoken to, please choose another castle member"))
      if waterbottle=="1": 
        print("\n\n\nYou are interviewing King Edmund")
        Edmund=(f"\n{mdec[x]}: Good evening Your Majesty, my deepest condolences for your loss.\n\nKing 1: Yes. It’s very unfortunate… I guess\n\n{mdec[x]}: What do you mean?\n\nKing 1: We had an arranged marriage, and then she took control of the funds, and since then I’ve had to fix all her mistakes. \n\n{mdec[x]}: I’m sorry things worked out like that, I hope everything will get better.\n\nKing: I do too, it’ll be hard to get the kingdom back on its feet, but I know I can do it.\n\n{mdec[x]}: I believe you can too, have a nice night Your Majesty.\n")
        typewriter(Edmund)
      
        print(f"\n\n\n{mdec[x]}: That was strange, the king didn’t see all that upset did he?\n\nAnabel: I would agree with you.\n\nJuliette: You should inspect his room while you clean.")
        dels=str(input("Do you want to inspect the King's room?\n\n(a) yes\n\n(b) no\n"))
        if dels in "Aa":
            approach=("\n\nGame: You approach the door and knock. No one answers. You quietly open the door and announce yourself. No response. He must be out. You start rummaging through drawers in his desk and search his chests. You find nothing. Finally, you check under the bed. You find a long curved knife. You leave it there but keep a mental note of it. You quietly exit the room without a trace.")
            typewriter(approach)
            mouse=str(input("\n\nEnter '1' to continue"))
            urmom(mouse)
            a+=1
            
        if dels not in "Aa": 
            picklechips=str(input("You did not go to the King's room. Press '1' to continue"))
            urmom(picklechips)
            a+=1
            
      if waterbottle=="2":
        print("\n\n\nYou are interviewing Seamstress Winifred")
        winifred=(f"\n{mdec[x]}: Hello Winifred, sorry to bother you. I was wondering what information you could provide me in relation to the queen’s murder. \n\nWinifred: I wasn’t supposed to come into the castle yesterday, but I had to deliver a note.\n\n{mdec[x]}: At what time did you deliver this note? And to whom?\n\nWinifred: Well the King of course! And I left around 9:30 I think.\n\n{mdec[x]}: What did the note say?\n\nWinifred: I’m sorry, but this information is not relevant to the murder, and is highly confidential.\n\n{mdec[x]}: Are you sure you can’t tell me?\n\nWinifred: Okay fine. I’ll tell you. But only if you are able to solve this riddle. You have three guesses, all lowercase letters.\n")
        typewriter(winifred)
        r1=0
        cges=0
        riddle1=str(input("What goes up but never goes down, answer in all lowercase. You have 3 guesses\n"))
        while r1<3:
          if riddle1.lower()=="age":
            cges+=1
            print("correct!")
            winifred=(f"\n\nWinifred: I found out that the gardener and the Queen were having an affair.\n\n{mdec[x]}: Interesting… Well I appreciate your help.\n\nWinifred: Glad I could help… have a nice day.\n\nWinifred: Too bad I can’t help you. Have a nice day.")
            typewriter(winifred)
            break
          elif r1<2:
            riddle1=str(input("Wrong. Enter again\n"))
            r1+=1
          else: 
            r1+=1
            riddle1=str(input("Wrong, you have failed to answer this riddle\n"))
            lollipop=(f"\n\n{mdec[x]}: Hmmm… that conversation didn’t really get us anywhere.\n\nSebastian: Yeah… we should keep and eye on Winifred")
            typewriter(lollipop)
        b+=1
    
      if waterbottle=="3":
        print("\n\n\nYou are interviewing Maid1: MIRABEL")
        Mirabel=(f"\n\n{mdec[x]}: Hi Mirabel, do you have any information about the day Queen Beatrice died?\n\nMirabel: Hello, yes I do! When I was dusting the house the day before she passed away, I couldn’t help but overhear the king and doctor talking.\n\n{mdec[x]}: What were they talking about?\n\nMirabel: They were talking about how much they hated the Queen, and the King said he just wants to rule the land by himself.\n\n{mdec[x]}: Hmm, interesting. Is that all?\n\nMirabel: I also saw a flash of white in the kitchen near the afternoon.\n\n{mdec[x]}: Oh that is interesting, I’ll have to check in with the cook then! Thank you for the information.\n\nEnd Conversation\n\n{mdec[x]}: The maid gave us some important information.\n\nSebastian: Agreed")
        typewriter(Mirabel)
        c+=1
        
      if waterbottle=="4":
        print("\n\nYou are interviewing Maid2: CELESTE")
        Maid2=(f"\n\n{mdec[x]}: Hello Celeste! How are you today?\n\nGame: Celeste looks distracted…\n\nCeleste: I’m alright, thank you. Just very melancholy about the Queen's death.\n\n{mdec[x]}: Yeah…about that… I was actually wondering if you had any additional information about what happened that day?\n\nCeleste: The night before she died, I noticed the doctor wasn’t in his room. The next day I had afternoon duties so I slept in late. I was woken up by Mirabel around 11 am, and she told me the tragic news. I went for a walk in the castle to find out as much information as I could, when heard a rumor that they don’t know where the Queen’s body is.\n\n{mdec[x]}: Fascinating, thank you for this information Celeste, this is all very helpful.\n\n*End Conversation*\n\n{mdec[x]}: Celeste seems innocent, I think the doctor is suspicious.\n\nAnabel: Agreed, lets keep an eye out for him.")
        typewriter(Maid2)
        d+=1
        
      if waterbottle=="5":
        print("\n\n\nYou are interviewing Cook: NEVILLE")
        Neville=(f"\n\n{mdec[x]}: Hello Neville, I was wondering if you have any information about the day the queen died?\n\nNeville: I was preparing a romantic dinner for my girlfriend, Celeste, and then I heard the tragic news. It was an unfortunate day all around, as I had to cancel my date with Celeste because of the events.\n\n{mdec[x]}: I’m sorry to hear that, did you notice anything strange that day?\n\nNeville: Well I noticed that one of my knives has been missing recently and hasn’t been found yet. I think the killer might have stolen a knife from the kitchen and I bet they must have stolen it during the afternoon because that is the only time I have a break.\n\n{mdec[x]}: Interesting, thanks for sharing.\n\n*End Conversation*")
        typewriter(Neville)
        e+=1
       
      if waterbottle=="6":
        print("\n\n\nYou are interviewing Butler: BARTHOLOMEW")
        Butler=(f"\n\n{mdec[x]}: Hello Bartholemew, do you know anything about the Queen’s death?\n\nBartholomew: Hmm, not really. Actually, I’m not sure if this is related, but there was a broken glass next to an open window near the garden.\n\n{mdec[x]}: That is actually quite important, thank you for your time.\n\nBartholomew: Great! Glad I could help.\n\n*End Conversation*\n\n{mdec[x]}: Could it have been the gardener? Or someone else.\n\nCassian: Hmm… not sure.")
        typewriter(Butler)
        f+=1
       
      if waterbottle=="7":
        print("\n\n\nDoctor: AUGUST")
        doctor=(f"\n\n{mdec[x]}: Hello August, I am here to ask you about what happened on the day of the queens death?\n\nAugust: Well I was caring for the king and queen… they were feeling a bit… under the weather. Later on I reorganized my medicine cabinet")
        typewriter(doctor)
        
        g+=1
        dell=0 
        search=str(input("\n\nGame: Would you like to search the drug cabinet?\n\n(a) Yes\n\n(b) No"))
        if search not in "Aa":
            no=(f"\n\n{mdec[x]}: Interesting… well thanks for talking with me.\n\n")
            typewriter(no)
            ah=str(input("Enter 1 to continue."))
            urmom(ah)
            dell+=1
        if search in "Aa": 
            yes=(f"\n\n{mdec[x]}: Interesting… mind if I take a look?\n\nAugust: Sure… go right ahead.\n\nGame: You walk over to the cabinet and open both doors. At first glance, it looks like the cabinet was organized, but then you start reading some of the labels. Everything was in its wrong place. This didn’t make any sense. You notice a bottle out of place. You take a closer look, the label was ripped off but the first letter looked like an A or a C. The top wasn’t screwed on correctly and you smell a faint scent of an almost almond-like scent. You think this bottle must be poison, however, you are not sure.\n\n{mdec[x]}: What is this bottle of poison doing right here in the front?\n\nAugust: WHAT? POSION? LET ME SEE THIS.\n\n{mdec[x]}: So you admit this is poison!\n\nAugust: It must be… do you notice that distinct scent of cyanide? That is the most common poison I notice when treating patients, I’m practically an expert.\n\nGame: He walks over to the cabinet and picks up the bottle. He inspects it and gives it a quick whiff.\n\nAugust: Yes…this is definitely cyanide, hopefully identifying the poison is helpful, but I swear, I did not put this in here. I’m a doctor, I don’t carry poison.\n\n{mdec[x]}: Well alright… thanks for explaining.\n\n*End Conversation*")
            typewriter(yes)
            ah=str(input("Enter 1 to continue."))
            urmom(ah)
            dell+=1
        
         
      if waterbottle=="8":
        priest=(f"\n\nGame: You walk to the church room, the floors and walls are sparkly clean, it eases you to see that most of the castle is hectic but the church is safe. Maybe you could get some answers from the priest, he must know more information since people come in for confessions often. \n\n{mdec[x]}: Hmm, where is Preist Irving? \n\nGame: You walk to the back of the room where the confessional box is and find the priest on the other side of it. You walk up to it. \n\n{mdec[x]}: Hello Irving, I have some things to ask you.\n\nGame: It takes a few seconds before Irving speaks. You notice his voice is higher-pitched.\n\nIrving: Hello, you must be one of the detectives. I’m glad to see someone taking care of the murder case. I can answer your questions, but as a priest, I am sworn to keep confessions confidential. \n\n{mdec[x]}: I understand your situation, but please your answer could save lives and bring the queens death to justice. \n\nIrving: As a priest, my job could go on the line and I could get seriously punished. However, I do want to help, I can reveal other information that could be helpful. \n\nPlayer: Any bit of information can be helpful, please tell me anything you know. \n\nIrving: Revealing information can be dangerous for me.\n\nPlayer 1: Okay.\n\nGame: Irving walks out with a shiny blue cassock\n\nIrving: Before the Queen’s death, she had been coming in more frequently for confessions. I’ve noticed that instead of turning right towards the Queen’s hallway, she turns left to the east wing. There are only a few places she could go when turning left: the garden, maid’s room, or the knight armory. I’ve also noticed a peculiar fragrance on her. It smelled almost nutty. I am a Priest so I have a lot of free time in the middle of the day when I’m not responding to confessionals, do you want me to help you find the killer? \n\n{mdec[x]}: Thank you for this information, it’s all very helpful. Also, that is our job you don’t need to concern yourself but we appreciate the initiative! \n\nIrving: Alright well have a nice day, I hope you can solve the case!\n\n*End Conversation*")
        typewriter(priest)
        h+=1
      
      if waterbottle=="9": 
        print("\n\n\nYou are interviewing Knight1: MAXIM")
        knight=(f"\n\n{mdec[x]}: Hello Maxim, I was wondering if you could provide me any information about the Queen's murder? I heard you had morning duties that day.\n\nMaxim: Yes, I did have morning duties. When I was looking around the castle that morning I kept hearing footsteps. I would try to run after them, but then they would stopped. At one point I followed the footsteps to the garden. I also noticed the gardener is never there in the morning, although it's the best time to plant crops. But that’s probably irrelevant.\n\n{mdec[x]}: Do you have afternoon duties too?\n\nMaxim: No, I am free during the afternoons so I only have this information, sorry.\n\n{mdec[x]}: Okay, well thank you for your time.")
        typewriter(knight)
        i+=1
        
      if waterbottle=="10": 
        print("\n\n\nYou are interviewing Knight2: BARNABAS")
        barnabas=(f"\n{mdec[x]}: Hello Barnabas, I’m here to ask you about what happened the night before the Queen's death, since you were on night duty.\n\nBarnabas: Well actually, when I went to close the door to the garden, there was a wedge in it, as if someone had wanted to keep it open. And, when I was walking around the castle, one of the windows was open. That was also near the garden.\n\n{mdec[x]}: Did you hear any noise or footsteps while on duty?\n\nBarnabas: No I don’t think so, I did see a glimpse of white at one point, but that could have just been my vision.\n\n{mdec[x]}: Thank you, this is all very helpful.")
        typewriter(barnabas)
        j+=1
     
      if waterbottle=="11": 
        print("\n\n\nYou are interviewing Gardener: FERDINAND")
        gardener=(f"\n\nGame: You begin to walk through the gardens to find Ferdinand, the castle gardener. You walk through rows and rows of gorgeous flowers, until you notice something strange. There are drops of something red near one of the bushes… it almost looks like blood. Weird. You keep on walking and soon find Ferdinand \n\nFerdinand: Hey! What can I help ya’ with?\n\n{mdec[x]}: I actually came to ask about the murder of beloved Queen Beatrice. Is there any information you could give me?\n\nFerdinand: Hmm… I can’t help ya’ too much with that, sorry. Didn’t… uh… know her too well. Let me know if you ever need anything though! Have a nice day.\n\n{mdec[x]}: Before I go, I wanted to ask you about something else… do you know what those red drops are near those bushes a little ways back?\n\nFerdinand: I haven’t been back there in a good while… those bushes don’t need trimmin’ very often. I’ll go check it out later though and see what’s goin’ on.\n\n{mdec[x]}: Alright… well thanks for the help anyways.\n\n*End Conversation*\n\n{mdec[x]}: Those red drops… might have to check them out later.\n\nCassian: I’m thinking that whole conversation was a little suspicious… those bushes looked recently trimmed.")
        typewriter(gardener)
        k+=1
        
      if waterbottle=="12": 
        print("\n\n\nYou are interviewing Page: CHRYSANTHA")
        page=(f"\n{mdec[x]}: Hello Chrysantha, how are you?\n\nChrysantha: I’m… uh… alright. Can I help you!?\n\n{mdec[x]}: Yes actually, can you tell me about the day Queen Beatrice was murdered?\n\nChrysantha: Yes, I noticed traces of blood in the east wing. I’m not sure if it’s the Queen’s blood.\n\n{mdec[x]}: Well who’s blood would it be?\n\nChrysantha: I don't know! But it probably is the Queen’s.\n\n{mdec[x]}: Well where in the east wing was the blood?\n\nChrysantha: On the way out to the garden. Sorry, that’s all the information I can give you. Have a nice day.\n\n{mdec[x]}: Uh okay, bye")
        typewriter(page)
        l+=1

castlem=['King: EDMUND','Seamstress: WINIFRED','Maid1: MIRABEL ','Maid2: CELESTE','Cook: NEVILLE','Butler: BARTHOLOMEW','Doctor: AUGUST','Priest: IRVING','Knight1: MAXIM','Knight2: BARNABAS','Gardener: FERDINAND','Page: CHRYSANTHA'] 

def urmom(message): 
  while message!="1": 
    message=str(input("Error. Enter '1' to continue"))
gathering=("\n\neveryone gathers around the room. The voting will now begin, everyone in this room will place a vote on a secret ballot, these are anonymous\n\n")
typewriter(gathering)

e=0
s=0
m=0
mm=0
c=0
b=0
d=0
p=0
k=0
kk=0
g=0
z=0



 
def list(castlem):
  for character in castlem:
    print(character + "\n")
list(castlem)


for x in range(players):
  vote=str(input(f"\n\n {mdec[x]} please vote who you think the killer is, enter a number corresponding with the list 1-12\n"))
  if vote in "1": 
    print("you have casted your vote for the king")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    e=e+1
  elif vote in "2": 
    print("you have casted your vote for the Seamstress") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    s=s+1
  elif vote in "3":
    print("you have casted your vote for the maid, Mirabel") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    m=m+1
  elif vote in "4":
    print("you have casted your vote for the maid, Celeste") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    mm=mm+1
  elif vote in "5": 
    print("you have casted your vote for the cook") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    c=c+1
  elif vote in "6": 
    print("you have casted your vote for the butler")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    b=b+1
  elif vote in "7":
    print("you have casted your vote for the doctor") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    d=d+1
  elif vote in "8": 
    print("you have casted your vote for the priest")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    p=p+1
  elif vote in "9": 
    print("you have casted your vote for the knight, Maxim") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    k=k+1
  elif vote in "10": 
    print("you have casted your vote for the knight, Barnabas") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    kk=kk+1
  elif vote in "11": 
    print("you have casted your vote for the gardener")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    g=g+1
  elif vote in "12": 
    print("you have casted your vote for the page") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    z=z+1
  else: 
    vote=str(input("Error. Enter a number 1-12 corresponding to the list"))

print("\n\nThe votes have been casted, the gardener had the highest votes with",6+g,"ballots! *to players* although you might not have voted for the gardener, the other castle members overrided your votes")

voting1=("\n\n*gasp* How could you guys vote me! I am completely innocent, never have I once thought of killing my beloved, the Queen. \n\nDoctor: Your beloved, the QUEEN? That only makes you more suspicious, are you having an affair with the queen?\n\nGardener: I admit, having an affair with the queen was bad and I should get punished for it, but I swear I did not kill the Queen!\n\nSeamstress: Do you have any proof you did not kill the Queen? \n\nJuliette: There was blood on the bushes! You must have killed the Queen there and hid the body somewhere. \n\nGardener: I was framed! I promise i have no idea how that got there!\n\nCassian: Then why did you say those bushes were untouched? When we checked they looked freshly trimmed? It seems like you were planning this. \n\nSebastian: Also, you weren’t in your room the night before the Queen died? Explain that \n\nPriest: Yeah Ferdinand! (left a blank space for taylors version)\n\nGardener: Like I said… I was having an affair with the queen\n\nAnabel: Does that explain why the Queen turned to the left which led to the garden? After each confession, was she coming to see you? \n\nGardener: Yes. That is correct\n\nButler: Your affair does not explain why the window was broken next to the Garden though, can you explain that? Was the queen trying to escape when you were killing her! \n\nCassian: But there was no blood next to the window, even if the Gardener did clean up the blood it doesn’t make sense why he would kill the Queen. Aren’t they having an affair because they love each other? There's no reason why the Gardener would kill the Queen if he loved her. \n\nDoctor: The most logical conclusion we can come up with is that the Gardener tried to kill the queen inside the Garden storage room, but she escaped. He tried to chase after her and didn’t notice she bled onto the bushes. When he finally caught up he murdered her and cleaned up the blood around the window. \n\nGame: Alright you cannot change your votes, the Gardener will be exiled regardless.\n\nGardener: No guys you have to believe me-\n\nGame: The Gardener has been voted out…")

typewriter(voting1)
#addloading
queenbody=("\n\nAnabel: Now that the gardener has been eliminated and we don’t know it wasn’t him even though it seemed really obvious that it was him, let’s look in the bushed that he supposedly didn’t touch and we also saw the blood on them.\n\n*walk over to the bushes near the window with blood that the gardener said he didn’t go near but they are freshly cut*\n\nCassian: *screams while noticing the queen's dead body, there were stab wounds over her body*\n\nSebastian: What! So was it the Gardener? If it wasn’t him who would have killed the Queen in the Garden? \n\nGame: You guys walk back to your rooms and catch a glimpse of blue on the way. You notice blood on the east wing. It seems to be the same shade of blood as the one splattered on the bushes. It must be the Queen’s blood. However, there was also a lighter red shade next to the blood. \n\nJuliette: Doesn’t that confirm it's the Gardner. We voted correctly right? The blood was in the east wing, which goes to the Garden storage room. Maybe the queen ran out of the room, instead of going out the window, and he forgot to clean the blood? \n\nCassian: Yes I think we voted correctly")

typewriter(queenbody)
#loading
deadbody=("\n\nGame: Attention detectives, Celeste, the maid has died. Please report to the voting room to vote again who you think the killer is. \n\nGame: Soon everyone gathers around. The Butler and Doctor arrived first looking appalled. then the priest with his white cassock.\n\nJuliet: We found the Queen’s body it was in the Garden\n\nDoctor: Aren’t you guys maids, why did you go outside?\n\nCassian: We were taking a walk\n\nSebastian: Wait, yesterday we found bloodstains next to the east wing, they must have been the Queens. However, we also found a lighter shade of red bloodstains, I assumed it was also the Queens but it must have been Celeste! The Gardener is exiled, it could not have been him. This means it must have been one of the knights since the east wing only leads to the Garden and the Knight room.\n\nGame: You will now start voting.")

typewriter(deadbody)


king=0
seamstress=0
maid2=0
cook=0
butler=0
doctor=0
priest=0
knight=0
knight2=0
page=0

for x in range(players):
  print("\n\n1 King: EDMUND\n\n2 Seamstress: WINIFRED\n\n3 Maid1: MIRABEL\n\n4 Cook: NEVILLE\n\n5 Butler: BARTHOLOMEW\n\n6 Doctor: AUGUST\n\n7 Priest: IRVING\n\n8 Knight1: MAXIM\n\n9 Knight2: BARNABAS\n\n10 Page: CHRYSANTHA")  
  vote=str(input(f"\n\n {mdec[x]} please vote who you think the killer is, enter a number corresponding with the list 1-12\n"))
  if vote in "1": 
    print("you have casted your vote for the king")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    king=king+1
  elif vote in "2": 
    print("you have casted your vote for the Seamstress") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    seamstress=seamstress+1
  elif vote in "3":
    print("you have casted your vote for the maid, Celeste") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    maid2=maid2+1
  elif vote in "4": 
    print("you have casted your vote for the cook") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    cook=cook+1
  elif vote in "5": 
    print("you have casted your vote for the butler")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    butler=butler+1
  elif vote in "6":
    print("you have casted your vote for the doctor") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    doctor=doctor+1
  elif vote in "7": 
    print("you have casted your vote for the priest")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    priest=priest+1
  elif vote in "8": 
    print("you have casted your vote for the knight, Maxim") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    knight=knight+1
  elif vote in "9": 
    print("you have casted your vote for the knight, Barnabas") 
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    knight2=knight2+1
  elif vote in "10": 
    print("you have casted your vote for the page")
    enter=str(input("Enter 1 to continue"))
    urmom(enter)
    page=page+1
  else: 
    vote=str(input("Error. Enter a number 1-12 corresponding to the list"))

print("\n\nThe votes have been casted, the doctor had the highest votes with",3+doctor,"ballots!*to players* although you might not have voted for the doctor, the other castle members overrided your votes")

game=("\n\nIt was a close call but the Doctor had the highest vote\n\nDoctor: How could you guys accuse me! I am a doctor, why would I kill the Queen. I have no motive, someone must be framing me. \n\nButler: Well you would get a hold of poison the easiest!\n\nDoctor: I promise you I didn’t have anything to do with the murder the poison must have gotten here another way?\n\nCassian 2: You acted suspiciously while we were talking and seemed to take a little too long when talking. Also, what is your alibi?\n\nDoctor: Ummm-\n\nJuliet 2: Exactly, you were also quick to accuse the gardener too. Did you frame him?!\n\nDoctor: I’m just really stressed! It made the most sense \n\nPlayer: Wait…when we found the body we noticed a stab wound on it. We think the doctor poisoned the queen but then why did the Queen die by knife? Who has a knife or could get ahold of a knife. \n\nDoctor: My alibi is that I was treating a patient during the night of the Queen’s death, that’s why I wasn’t in my room. You can talk to the patient! I am innocent. \n\nGame: It is too late, the Doctor has already been voted and will be exiled. \n\nGame: The Doctor has been voted out…\n\nPlayer: Wait…but")
typewriter(game)



edmund=0
winifred=0
neville=0
bartholomew=0
irving=0
maxim=0
barnabas=0
chrysantha=0

bank=[]
for x in range(players): 
  bank.append(50)

player1=[]
player2=[]
player3=[]
player4=[]
win=0
loose=0



imcrying=['edmund','winifred','neville','bartholomew','irving','maxim','barnabas','page']

def urmom(message): 
  while message!="1": 
    message=str(input("Error. Enter '1' to continue"))
game=("\n\neveryone gathers around the room ADD MORE ")


rounds=3
moneyo=[100,150,20]
options=['sheriff','convo','mystery']

game=("\n\n...LOADING...\n\nThe castle members will stop voting from this point on, it is clear they have been scheming together to vote out one person. It will just be you detectives voting now, good luck. Note: if there are less than four players, the other npc detective votes will not be added. Also Maid 1, Mirabel has been killed by the killer, please find them fast.Good luck. Voting will keep on going until you find the killer, or the killer finds you...Although first, as an intermission between votes, you can play games and buy items from the store")
typewriter(game)

while rounds>0:
  for x in range(players):
    print("\n\nPlayer",x+1,"You have $",bank[x])
    choice=str(input("\n\nChoose from the options below.\n\n   (a) Rock Paper Scissors\n\n   (b) Flip a coin\n\n   (c) Pick the number\n"))
    
    if choice in "Aa": 
      rockps=['rock','paper','scissors']
      random.shuffle(rockps)
      rps=str(input("Choose, rock, paper, scissors, enter EXACT spelling as listed"))
      win1=0
      loose1=0
      played=0
      
      while played!=1:
        if "scissors" in rps: 
          print("you have choosen scissors")
          if "scissors" in rockps[0]:
            rps=str(input("it was a tie, enter again"))
            random.shuffle(rockps)
          if "rock" in rockps[0]:
            loose1+=1
            played+=1
            print("you lost scissors vs rock")
            
          if "paper" in rockps[0]: 
            win1+=1
            played+=1
            print("you won scissors vs paper")
            
        elif "rock" in rps: 
          print("you have choosen rock")
          if "rock" in rockps[0]:
            rps=str(input("it was a tie, enter again"))
            random.shuffle(rockps)
          if "paper" in rockps[0]:
            loose1+=1
            played+=1
            print("you lost rock vs paper")
            
          if "scissors" in rockps[0]: 
            win1+=1
            played+=1
            print("you won rock vs scissors")
            
        elif "paper" in rps: 
          print("you have choosen paper")
          if "paper" in rockps[0]:
            rps=str(input("it was a tie, enter again"))
            random.shuffle(rockps)
          if "scissors" in rockps[0]:
            loose1+=1
            played+=1
            print("you lost paper vs scissors")
            
          if "rock" in rockps[0]: 
            win1+=1
            played+=1
            print("you won paper vs rock")
            
        else: 
          rps=str(input("Error. Please enter again, write the exact spelling. 'rock' 'paper' 'scissors'"))
      if win1>0: 
        bank[x]+=50
        print("you now have",bank[x])
      if loose1>0:
        bank[x]-=25
        print("you now have",bank[x])
  
    elif choice in "Bb":
      print("Use exact spelling or you will automatically loose $25. Winning will get you $25, loosing means loosing $25")
      headsortails=str(input("\nDo you choose heads or tails?"))
      y = random.randint(1,2)
      if y == 1:
        print("heads")
        if headsortails in "heads": 
          bank[x]+=25
        if headsortails not in "heads":
          bank[x]-=25
        print("you have",bank[x],"now")
      else:
        print("tails")
        if headsortails in "tails": 
          bank[x]+=25
        if headsortails not in "tails":
          bank[x]-=25
        print("you have",bank[x],"now")
    elif choice in "Cc": 
      number=['1','2','3','4','5','6','7','8','9','10',]
      random.shuffle(number)
      print("if you guess in one try you get 100, 2 you get 80, 3 you get 60, 4 you get 40, 5 you get 20, anything after 5 you loose $25")
      guess=str(input("choose a number from 1-10"))
      count=0
      guess=0
      while guess!=number[0]:
        guess=str(input("That is incorrect enter again "))
        count+=1
      if guess==number:
        print("your guess is correct")
        print("it took you",count,"tries to guess")
      if count==1: 
        bank[x]+=100
        
      if count==2: 
        bank[x]+=80
        print("you have",bank[x],"now")
      if count==3: 
        bank[x]+=60
        print("you have",bank[x],"now")
      if count==4: 
        bank[x]+=40
        print("you have",bank[x],"now")
      if count==5:
        bank[x]+=20
        print("you have",bank[x],"now")
      if count>5: 
        bank[x]-=25
        print("you have",bank[x],"now")
    else:
      choice=str(input("error, choose again\n\n   (a) Rock Paper Scissors\n\n   (b) Flip a coin\n\n   (c) Pick the number"))
  
  for x in range(players):
    print("\n\nPlayer",x+1,"Now you can buy something from the store with your money. \nYou have",bank[x],"Do you want to check the store?\n")
    store=str(input("\n\n   (a) yes \n\n   (b) no"))
    if store in "Aa": 
      print("\nYou are 3 things you can buy\n\n(a) $100 Gun to become Sheriff\n\n(b) $20 Secret Convo\n\n(c) $150 Mystery\n\n(d) None\n\nRespectively their prices are 100, 20, 150. Here is what is avaliable",options,"Note the mystery is not avaliable for single players")
      buy=str(input("what do you choose?\n"))
    
      if buy in "Aa":
        if bank[x]>=100:
          if "sheriff" in options:         
            print("\n\nYou have purchased the sheriff spot. This is important, you only have 1 bullet which means you can only kill one castle member. If you guess correctly you will win the game, however the other detectives do not. Good Luck. ")
            bank[x]-=100
            options.remove('sheriff')
            if x==0:
              player1.append('sheriff')
              print("This is your inventory",player1)
            if x==1:
              player2.append('sheriff')
              print("This is your inventory",player2)
            if x==2: 
              player3.append('sheriff')
              print("This is your inventory",player3)
            if x==3: 
              player4.append('sheriff')
              print("This is your inventory",player4)
        
          else: 
            print("sorry this has already been purchased. Try purchasing another item next time")
        else: 
          print("You do not have enough money to buy this")
      elif buy in "Bb":
        if bank[x]>=20:
          
          print("\nGame: You have unlocked a secret outcome…\n\npov: the priest meets barnabus\n\npriest: why is your name barnabas?\n\nbarnabus: my parents really liked to eat barnacles \n\npriest: wow what a cool story! visit the church more often, I haven't been seeing you recently.\n\nbarnabus: I will\n\npriest: yay")
          bank[x]-=20
      elif buy in "Cc":
        
        if players>1: 
          if "mystery" in options: 
            if bank[x]>=150:
              bank[x]-=150
              options.remove('mystery')
              game=("please turn your screen away from the other players, this information can only be given to you...\n...You have purchased the mystery spot. This costed $150 dollars. You now have a new position as Joker instead of the Detective. Your job is to trick the other player/s into loosing so you win the game. The murderer is the priest. Good luck. ")
              typewriter(game)
              if x==0:
                player1.append('mystery')
                print("This is your inventory",player1)
              if x==1:
                player2.append('mystery')
                print("This is your inventory",player2)
              if x==2: 
                player3.append('mystery')
                print("This is your inventory",player3)
              if x==3: 
                player4.append('mystery')
                print("This is your inventory",player4)
              
            else:
              print("you do not have enough money please choose something else next time")
          else:
            print("Sorry this has already been purchased please choose something else next time")
        else: 
          print("you are on solo mode, please choose another option next time")
      elif buy in "Dd": 
        
        print("You have not purchased anything")
      else: 
        buy=str(input("you did not choose the right letter, your turn is now skipped"))
    if store in "Bb": 
      print("you have not purchased anything from the store")
    if store not in "AaBbCc":
      print("you have not purchased anything from the store")



  if "sheriff" in player1: 
    bullet=str(input("\n\n\nPlayer 1 Do you want to kill someone with your gun because you are the sheriff?\n\n(a) yes\n\n(b) no"))
    if bullet in "Aa":
      print("Since you have bought the sheriff, we have shortened your list, the killer is among one of these 4\n\n1 King: EDMUND\n\n2 Priest: IRVING\n\n3 Knight1: MAXIM\n\n4 Page: CHRYSANTHA\n\n")
      killing=str(input("Enter a number 1-4 corresponding to the list to kill"))
      if killing in "1": 
            print("You have killed the king, unfortunatly he was not the killer")
            player1.remove('sheriff')
            imcrying.remove('edmund')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)
      elif killing in "2": 
            print("you have killed the priest, he was the killer you won")
            player1.append('win')
            imcrying.remove('irving')
            dialouge2=("\n\nSebastian: It has got to be the priest right? It only makes sense.\n\nAnabel: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nCassian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nSebastian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nAnabel: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be one. However the queen caught me so I had to kill her, then I had to kill both the maids because they actually caught me")
            typewriter(dialouge2)
            
            win+=1
            break
          
      elif killing in "3":           
            print("you have killed the knight, Maxim. He was not the murderer")
            player1.remove('sheriff')
            imcrying.remove('maxim')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)            
      elif killing in "4": 
          
            print("you have killed the page, the page was not the murderer")
            player1.remove('sheriff')
            imcrying.remove('chrysantha')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)              
      else:
          print("you have not choosen a number between 1-4, you lost your chance at killing a castle member, you can try next round though")
    else:      
        print("you have saved your bullet")

  if "sheriff" in player2: 
    bullet=str(input("\n\n\nPlayer 2 Do you want to kill someone with your gun because you are the sheriff?\n\n(a) yes\n\n(b) no"))
    if bullet in "Aa":
      print("Since you have bought the sheriff, we have shortened your list, the killer is among one of these 4\n\n1 King: EDMUND\n\n2 Priest: IRVING\n\n3 Knight1: MAXIM\n\n4 Page: CHRYSANTHA\n\n")
      killing=str(input("Enter a number 1-4 corresponding to the list to kill"))
      if killing in "1": 
            print("You have killed the king, unfortunatly he was not the killer")
            player2.remove('sheriff')
            imcrying.remove('edmund')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)
      elif killing in "2": 
            print("you have killed the priest, he was the killer you won")
            player2.append('win')
            imcrying.remove('irving')
            dialouge2=("\n\nSebastian: It has got to be the priest right? It only makes sense.\n\nAnabel: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nCassian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nSebastian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nAnabel: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be one. However the queen caught me so I had to kill her, then I had to kill both the maids because they actually caught me")
            typewriter(dialouge2)
            
            rounds-=3
            win+=1
            break
          
      elif killing in "3":           
            print("you have killed the knight, Maxim. He was not the murderer")
            player2.remove('sheriff')
            imcrying.remove('maxim')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)            
      elif killing in "4": 
          
            print("you have killed the page, the page was not the murderer")
            player2.remove('sheriff')
            imcrying.remove('chrysantha')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)              
      else:
          print("you have not choosen a number between 1-4, you lost your chance at killing a castle member, you can try next round though")
    else:      
        print("you have saved your bullet")
  if "sheriff" in player3: 
    bullet=str(input("\n\n\nPlayer 3 Do you want to kill someone with your gun because you are the sheriff?\n\n(a) yes\n\n(b) no"))
    if bullet in "Aa":
      print("Since you have bought the sheriff, we have shortened your list, the killer is among one of these 4\n\n1 King: EDMUND\n\n2 Priest: IRVING\n\n3 Knight1: MAXIM\n\n4 Page: CHRYSANTHA\n\n")
      killing=str(input("Enter a number 1-4 corresponding to the list to kill"))
      if killing in "1": 
            print("You have killed the king, unfortunatly he was not the killer")
            player3.remove('sheriff')
            imcrying.remove('edmund')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)
      elif killing in "2": 
            print("you have killed the priest, he was the killer you won")
            player3.append('win')
            imcrying.remove('irving')
            dialouge2=("\n\nSebastian: It has got to be the priest right? It only makes sense.\n\nAnabel: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nCassian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nSebastian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nAnabel: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be one. However the queen caught me so I had to kill her, then I had to kill both the maids because they actually caught me")
            typewriter(dialouge2)
  
            rounds-=3
            win+=1
            break
      elif killing in "3":           
            print("you have killed the knight, Maxim. He was not the murderer")
            player3.remove('sheriff')
            imcrying.remove('maxim')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)            
      elif killing in "4": 
          
            print("you have killed the page, the page was not the murderer")
            player3.remove('sheriff')
            imcrying.remove('chrysantha')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)              
      else:
          print("you have not choosen a number between 1-4, you lost your chance at killing a castle member, you can try next round though")
    else:      
        print("you have saved your bullet")
  if "sheriff" in player4: 
    bullet=str(input("\n\n\nPlayer 4 Do you want to kill someone with your gun because you are the sheriff?\n\n(a) yes\n\n(b) no"))
    if bullet in "Aa":
      print("Since you have bought the sheriff, we have shortened your list, the killer is among one of these 4\n\n1 King: EDMUND\n\n2 Priest: IRVING\n\n3 Knight1: MAXIM\n\n4 Page: CHRYSANTHA\n\n")
      killing=str(input("Enter a number 1-4 corresponding to the list to kill"))
      if killing in "1": 
            print("You have killed the king, unfortunatly he was not the killer")
            player4.remove('sheriff')
            imcrying.remove('edmund')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)
      elif killing in "2": 
            print("you have killed the priest, he was the killer you won")
            player4.append('win')
            imcrying.remove('irving')
            
            dialouge2=("\n\nSebastian: It has got to be the priest right? It only makes sense.\n\nAnabel: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nCassian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nSebastian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nAnabel: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be one. However the queen caught me so I had to kill her, then I had to kill both the maids because they actually caught me")
            typewriter(dialouge2)
            rounds-=3
            win+=1
            break
      elif killing in "3":           
            print("you have killed the knight, Maxim. He was not the murderer")
            player4.remove('sheriff')
            imcrying.remove('maxim')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)            
      elif killing in "4": 
          
            print("you have killed the page, the page was not the murderer")
            player4.remove('sheriff')
            imcrying.remove('chrysantha')
            enter=str(input("Enter 1 to continue"))
            urmom(enter)              
      else:
          print("you have not choosen a number between 1-4, you lost your chance at killing a castle member, you can try next round though")
    else:      
        print("you have saved your bullet")


  
  
  edmund=0
  winifred=0
  neville=0
  bartholomew=0
  irving=0
  maxim=0
  barnabas=0
  chrysantha=0
   
    
    
  
  
  for x in range(players):
    print("\n\n1 King: EDMUND\n\n2 Seamstress: WINIFRED\n\n3 Cook: NEVILLE\n\n4 Butler: BARTHOLOMEW\n\n5 Priest: IRVING\n\n6 Knight1: MAXIM\n\n7 Knight2: BARNABAS\n\n8 Page: CHRYSANTHA")
    vote3=str(input(f"\n\n {mdec[x]} Please vote who you think the killer is, enter a number corresponding with the list 1-8\n"))  
    vote=1
    while vote!=0:
      if vote3 in "1": 
        if "edmund" in imcrying:
          print("you have casted your vote for the king")
          edmund=edmund+1
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          vote-=1
            
        if "edmund" not in imcrying: 
          vote3=str(input("The king has already been voted out, please choose another castle member from the list"))
      elif vote3 in "2": 
        if "winifred" in imcrying:
          print("you have casted your vote for the Seamstress") 
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          winifred=winifred+1
          vote-=1
              
        if "winifred" not in imcrying:
          vote3=str(input("The seamstress has already been voted out, please choose another castle member from the list"))
              
      elif vote3 in "3": 
        if "neville" in imcrying:
          print("you have casted your vote for the cook") 
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          neville=neville+1
          vote-=1
              
        if "neville" not in imcrying: 
          vote3=str(input("The cook has already been voted out, please choose another castle member from the list"))
      elif vote3 in "4": 
        if "bartholomew" in imcrying:
          print("you have casted your vote for the butler")
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          bartholomew=bartholomew+1
          vote-=1
              
        if "bartholomew" not in imcrying: 
          vote3=str(input("The butler has already been voted out, please choose another castle member from the list"))
      elif vote3 in "5": 
        if "irving" in imcrying: 
          print("you have casted your vote for the priest")
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          irving=irving+1
          vote-=1
              
        if "irving" not in imcrying:
          win=("you have already won you dont need to vote anymore")
          typewriter(win)
      elif vote3 in "6": 
        if "maxim" in imcrying:
          print("you have casted your vote for the knight, Maxim")
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          maxim=maxim+1
          vote-=1
              
        if "maxim" not in imcrying:
          vote3=str(input("Knight 1 has already been voted out, please choose another castle member from the list"))
      elif vote3 in "7": 
        if "barnabas" in imcrying: 
          print("you have casted your vote for the knight, Barnabas") 
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          barnabas=barnabas+1
          vote-=1
              
        if "barnabas" not in imcrying: 
          vote3=str(input("Knight 2 has already been voted out, please choose another castle member from the list"))
      elif vote3 in "8": 
        if "chrysantha" in imcrying: 
          print("you have casted your vote for the page")
          enter=str(input("Enter 1 to continue"))
          urmom(enter)
          chrysantha=chrysantha+1
          vote-=1
              
        if "chrysantha" not in imcrying:
          vote3=str(input("The page has already been voted out, please choose another castle member from the list"))
      else:
        vote3=str(input("Error. Enter a number 1-8 corresponding to the list"))
            
    anotherlist=[]
    anotherlist2=[]  
    
  if players==4: 
    if edmund==4 or edmund==3: 
      dialouge1=("\n\nGame:The king has the highest votes of")
      dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nAnabel: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nCassian: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nSebastian: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nJuliette: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nAnabel: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
      typewriter(dialouge1)
      print(edmund)
      typewriter(dialouge2)
      imcrying.remove('edmund')
    if edmund==2: 
      anotherlist.append("edmund")
        
    if edmund==1: 
      anotherlist2.append("edmund")
       
    if winifred==4 or winifred==3: 
      dialouge1=("\n\nGame:Winifred has the highest votes of")
      dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nCassian:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nSebastian: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
      typewriter(dialouge1)
      print(winifred)
      typewriter(dialouge2)
      imcrying.remove('winifred')
    if winifred==2: 
      anotherlist.append("winifred")
        
    if winifred==1: 
      anotherlist2.append("winifred")
        
    if neville==4 or neville==3: 
      dialouge1=("\n\nGame:The cook has the highest votes of")
      dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nJuliette: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nAnabel: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nCassian: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
      typewriter(dialouge1)
      print(neville)
      typewriter(dialouge2)
      imcrying.remove('neville')
    if neville==2:
      anotherlist.append("neville")
       
    if neville==1: 
      anotherlist2.append("neville")
       
    if bartholomew==4 or bartholomew==3: 
      dialouge1=("\n\nGame:The butler has the highest votes of")
      dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
      typewriter(dialouge1)
      print(bartholomew)
      typewriter(dialouge2)
      imcrying.remove('bartholomew')
    if bartholomew==2: 
      anotherlist.append("bartholomew")
       
    if bartholomew==1: 
      anotherlist2.append("bartholomew")
        
    if irving==4 or irving==3: 
      dialouge1=("\n\nGame:The priest has the highest votes of")
      dialouge2=("\n\nSebastian: It has got to be the priest right? It only makes sense.\n\nJuliette: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nAnabel: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nCassian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nSebastian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nJuliette: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
      typewriter(dialouge1)
      print(irving)
      typewriter(dialouge2)
      imcrying.remove('irving')
      round-=3
    if irving==2: 
      anotherlist.append("irving")
       
    if irving==1: 
      anotherlist2.append("irving")
      
    if maxim==4 or maxim==3: 
      dialouge1=("\n\nGame:The butler has the highest votes of")
      dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nAnabel: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nCassian: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
      typewriter(dialouge1)
      print(maxim)
      typewriter(dialouge2)
      imcrying.remove('maxim')
    if maxim==2: 
      anotherlist.append("maxim")
    if maxim==1: 
      anotherlist2.append("maxim")
       
    if barnabas==4 or barnabas==3: 
      dialouge1=("\n\nGame:The butler has the highest votes of")
      dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nSebastian: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nJuliette: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
      typewriter(dialouge1)
      print(barnabas)
      typewriter(dialouge2)
      imcrying.remove('barnabas')
    if barnabas==2: 
      anotherlist.append("barnabas")
      
    if barnabas==1: 
      anotherlist2.append("barnabas")
        
    if chrysantha==4 or chrysantha==3: 
      dialouge1=("\n\nGame:The page has the highest votes of")
      dialouge2=("\n\nPage: Why did Crysythia get voted out?\n\nAnabel: Your Crysythia\n\nPage: Yes but why did she get voted out!\n\nCassian: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nSebastian: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
      typewriter(dialouge1)
      print(chrysantha)
      typewriter(dialouge2)
      imcrying.remove('neville')
    if chrysantha==2: 
      anotherlist.append("chrysantha")
        
    if chrysantha==1: 
      anotherlist2.append("chrysantha")
    
  if len(anotherlist2)==4: 
    chair=random.randint(1,4)
    game=("\n\nThere is a tie between 4 people")
    typewriter(game)
    print(anotherlist2[0],anotherlist2[1])
    print(anotherlist2[2],anotherlist2[3])
    game=("\n\nOne will randomly get voted out")
    typewriter(game)
    if chair==1: 
      del anotherlist2[3]
      del anotherlist2[2]
      del anotherlist2[1]
    if chair==2: 
      del anotherlist2[3]
      del anotherlist2[2]
      del anotherlist2[0]
    if chair==3: 
      del anotherlist2[3]
      del anotherlist2[1]
      del anotherlist2[0]
    if chair==4: 
      del anotherlist2[2]
      del anotherlist2[1]
      del anotherlist2[0]
    if len(anotherlist2)==1:  
      if anotherlist2[0] in "edmund": 
        dialouge1=("\n\nGame:The king has the highest votes of")
        dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nJuliette: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nAnabel: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nCassian: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nSebastian: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nJuliette: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
        typewriter(dialouge1)
        print(edmund)
        typewriter(dialouge2)
        imcrying.remove('edmund')
      elif anotherlist2[0] in "winifred":
        dialouge1=("\n\nGame:The seamstress has the highest votes of")
        dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nAnabel:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nCassian: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
        typewriter(dialouge1)
        print(winifred)
        typewriter(dialouge2)
        imcrying.remove('winifred')
      elif anotherlist2[0] in "neville":
        dialouge1=("\n\nGame:The cook has the highest votes of")
        dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nSebastian: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nJuliette: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nAnabel: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
        typewriter(dialouge1)
        print(neville)
        typewriter(dialouge2)
        imcrying.remove('neville')
      elif anotherlist2[0] in "bartholomew": 
        dialouge1=("\n\nGame:The butler has the highest votes of")
        dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
        typewriter(dialouge1)
        print(bartholomew)
        typewriter(dialouge2)
        imcrying.remove('bartholomew')
      elif anotherlist2[0] in "irving": 
        dialouge1=("\n\nGame:The priest has the highest votes of")
        dialouge2=("\n\nCassian: It has got to be the priest right? It only makes sense.\n\nSebastian: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nAnabel: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nCassian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nSebastian: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
        typewriter(dialouge1)
        print(irving)
        typewriter(dialouge2)
        imcrying.remove('irving')
        rounds-=3
      elif anotherlist2[0] in 'maxim':
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nJuliette: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nAnabel: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
        typewriter(dialouge1)
        print(maxim)
        typewriter(dialouge2)
        imcrying.remove('maxim')
      elif anotherlist2[0] in 'barnabas': 
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nCassian: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nSebastian: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
        typewriter(dialouge1)
        print(barnabas)
        typewriter(dialouge2)
        imcrying.remove('barnabas')
      elif anotherlist2[0] in 'chrysantha':
        dialouge1=("\n\nGame:The page has the highest votes of")
        dialouge2=("\n\nPage: Why did chrysantha get voted out?\n\nJuliette: Your Crysythia\n\nPage: Yes but why did she get voted out!\n\nAnabel: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nCassian: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
        typewriter(dialouge1)
        print(chrysantha)
        typewriter(dialouge2)
        imcrying.remove('chrysantha')
  if len(anotherlist)==2: 
    game=("\n\nThere has been a tie between")
    hello=("Since there is a tie, one will randomly get voted out")
    typewriter(game)
    print(anotherlist[0],anotherlist[1])
    typewriter(hello)
    number=random.randint(1,2)
    if number==1:   
      del anotherlist[0]
    if number==2: 
      del anotherlist[1]
  if len(anotherlist)==1: 
    if anotherlist[0] in "edmund": 
      dialouge1=("\n\nGame:The king has the highest votes of")
      dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nJuliette: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nAnabel: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nCassian: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nSebastian: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nJuliette: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
      typewriter(dialouge1)
      print(edmund)
      typewriter(dialouge2)
      imcrying.remove('edmund')
    elif anotherlist[0] in "winifred":
      dialouge1=("\n\nGame:The seamstress has the highest votes of")
      dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nAnabel:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nCassian: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
      typewriter(dialouge1)
      print(winifred)
      typewriter(dialouge2)
      imcrying.remove('winifred')
    elif anotherlist[0] in "neville":
      dialouge1=("\n\nGame:The cook has the highest votes of")
      dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nSebastian: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nJuliette: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nAnabel: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
      typewriter(dialouge1)
      print(neville)
      typewriter(dialouge2)
      imcrying.remove('neville')
    elif anotherlist[0] in "bartholomew": 
      dialouge1=("\n\nGame:The butler has the highest votes of")
      dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
      typewriter(dialouge1)
      print(bartholomew)
      typewriter(dialouge2)
      imcrying.remove('bartholomew')
    elif anotherlist[0] in "irving": 
      dialouge1=("\n\nGame:The priest has the highest votes of")
      dialouge2=("\n\nCassian: It has got to be the priest right? It only makes sense.\n\nSebastian: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nAnabel: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nCassian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nSebastian: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
      typewriter(dialouge1)
      print(irving)
      typewriter(dialouge2)
      imcrying.remove('irving')
      rounds-=3
    elif anotherlist[0] in 'maxim':
      dialouge1=("\n\nGame:The knight has the highest votes of")
      dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nJuliette: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nAnabel: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
      typewriter(dialouge1)
      print(maxim)
      typewriter(dialouge2)
      imcrying.remove('maxim')
    elif anotherlist[0] in 'barnabas': 
      dialouge1=("\n\nGame:The knight has the highest votes of")
      dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nCassian: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nSebastian: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
      typewriter(dialouge1)
      print(barnabas)
      typewriter(dialouge2)
      imcrying.remove('barnabas')
    elif anotherlist[0] in 'chrysantha':
      dialouge1=("\n\nGame:The page has the highest votes of")
      dialouge2=("\n\nPage: Why did chrysantha get voted out?\n\nJuliette: Your Crysythia\n\nPage: Yes but why did she get voted out!\n\nAnabel: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nCassian: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
      typewriter(dialouge1)
      print(chrysantha)
      typewriter(dialouge2)
      imcrying.remove('chrysantha')
 
  itsten=[]
  if players==3: 
    if edmund==3 or edmund==2: 
      dialouge1=("\n\nGame:The king has the highest votes of")
      dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nSebastian: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nJuliette: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nAnabel: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nCassian: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nSebastian: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
      typewriter(dialouge1)
      print(edmund)
      typewriter(dialouge2)  
      imcrying.remove('edmund')
    if edmund==1: 
      itsten.append("edmund")
     
    if winifred==3 or winifred==2: 
      dialouge1=("\n\nGame:Winifred has the highest votes of")
      dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nJuliette: But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nAnabel: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
      typewriter(dialouge1)
      print(winifred)
      typewriter(dialouge2)
      imcrying.remove('winifred')
    if winifred==1: 
      itsten.append("winifred")
      
    if neville==3 or neville==2: 
      dialouge1=("\n\nGame:The cook has the highest votes of")
      dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nCassian: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nSebastian: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nJuliette: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
      typewriter(dialouge1)
      print(neville)
      typewriter(dialouge2)
      imcrying.remove('neville')
    if neville==1: 
      itsten.append("neville")
     
    if bartholomew==3 or bartholomew==2: 
      dialouge1=("\n\nGame:The butler has the highest votes of")
      dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
      typewriter(dialouge1)
      print(bartholomew)
      typewriter(dialouge2)
      imcrying.remove('bartholomew')
    if bartholomew==1: 
      itsten.append("bartholomew")
      
    if irving==3 or irving==2: 
      dialouge1=("\n\nGame:The priest has the highest votes of")
      dialouge2=("\n\nAnabel: It has got to be the priest right? It only makes sense.\n\nCassian: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nSebastian: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nJuliette: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nAnabel: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nCassian: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
      typewriter(dialouge1)
      print(irving)
      typewriter(dialouge2)
      imcrying.remove('irving')
      rounds-=3
    if irving==1: 
      itsten.append("irving")
    
    if maxim==3 or maxim==2: 
      dialouge1=("\n\nGame:The knight has the highest votes of")
      dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nSebastian: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nJuliette: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
      typewriter(dialouge1)
      print(maxim)
      typewriter(dialouge2)
      imcrying.remove('maxim')
      
    if maxim==1: 
      itsten.append("maxim")
     
    if barnabas==3 or barnabas==2: 
      dialouge1=("\n\nGame:The knight has the highest votes of")
      dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nAnabel: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nCassian: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
      typewriter(dialouge1)
      print(barnabas)
      typewriter(dialouge2)
      imcrying.remove('barnabas')
      
    if barnabas==1: 
      itsten.append("barnabas")
      
    if chrysantha==3 or chrysantha==2: 
      dialouge1=("\n\nGame:The page has the highest votes of")
      dialouge2=("\n\nPage: Why did Crysythia get voted out?\n\nSebastian: Your Crysythia\n\nPage: Yes but why did she get voted out!\n\nJuliette: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nAnabel: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
      typewriter(dialouge1)
      print(chrysantha)
      typewriter(dialouge2)
      imcrying.remove('chrysantha')
    if chrysantha==1: 
      itsten.append("chrysantha")
  
  if len(itsten)==3: 
    game=("\n\nThere has been a tie between")
    hello=("Since there is a tie, one will randomly get voted out")
    typewriter(game)
    print(itsten[0],itsten[1],itsten[2])
    typewriter(hello)
    number=random.randint(1,3)
    if number==1:   
      del itsten[2]
      del itsten[1]
    if number==2: 
      del itsten[2]
      del itsten[0]
    if number==3:
      del itsten[1]
      del itsten[0]
    if len(itsten)==1:
      if itsten[0] in "edmund": 
        dialouge1=("\n\nGame:The king has the highest votes of")
        dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nCassian: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nSebastian: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nJuliette: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nAnabel: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nCassian: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
        typewriter(dialouge1)
        print(edmund)
        typewriter(dialouge2)
        imcrying.remove('edmund')
      elif itsten[0] in "winifred":
        dialouge1=("\n\nGame:The seamstress has the highest votes of")
        dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nSebastian:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nJuliette: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
        typewriter(dialouge1)
        print(winifred)
        typewriter(dialouge2)
        imcrying.remove('winifred')
      elif itsten[0] in "neville":
        dialouge1=("\n\nGame:The cook has the highest votes of")
        dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nAnabel: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nCassian: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nSebastian: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
        typewriter(dialouge1)
        print(neville)
        typewriter(dialouge2)
        imcrying.remove('neville')
      elif itsten[0] in "bartholomew": 
        dialouge1=("\n\nGame:The butler has the highest votes of")
        dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
        typewriter(dialouge1)
        print(bartholomew)
        typewriter(dialouge2)
        imcrying.remove('bartholomew')
      elif itsten[0] in "irving": 
        dialouge1=("\n\nGame:The priest has the highest votes of")
        dialouge2=("\n\nJuliette: It has got to be the priest right? It only makes sense.\n\nAnabel: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nCassian: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nSebastian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nJuliette: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nAnabel: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
        typewriter(dialouge1)
        print(irving)
        typewriter(dialouge2)
        imcrying.remove('irving')
        rounds-=3
      elif itsten[0] in 'maxim':
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nCassian: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nSebastian: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
        typewriter(dialouge1)
        print(maxim)
        typewriter(dialouge2)
        imcrying.remove('maxim')
      elif itsten[0] in 'barnabas': 
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nJuliette: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nAnabel: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
        typewriter(dialouge1)
        print(barnabas)
        typewriter(dialouge2)
        imcrying.remove('barnabas')
      elif itsten[0] in 'chrysantha':
        dialouge1=("\n\nGame:The page has the highest votes of")
        dialouge2=("\n\nPage: Why did Chrysantha get voted out?\n\nCassian: You're Chrysantha\n\nPage: Yes but why did she get voted out!\n\nAnabel: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nCassian: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
        typewriter(dialouge1)
        print(chrysantha)
        typewriter(dialouge2)
        imcrying.remove('chrysantha')
      
    
  icecream=[]
  if players==2:  
      if edmund==2: 
        dialouge1=("\n\nGame:The king has the highest votes of")
        dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nSebastian: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nJuliette: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nAnabel: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nCassian: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nSebastian: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
        typewriter(dialouge1)
        print(edmund)
        typewriter(dialouge2)  
        imcrying.remove('edmund')
      if edmund==1: 
        icecream.append("edmund")
       
      if winifred==2: 
        dialouge1=("\n\nGame:Winifred has the highest votes of")
        dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nJuliette:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nAnabel: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
        typewriter(dialouge1)
        print(winifred)
        typewriter(dialouge2)
        imcrying.remove('winifred')
      if winifred==1: 
        icecream.append("winifred")
        
      if neville==2: 
        dialouge1=("\n\nGame:The cook has the highest votes of")
        dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nCassian: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nSebastian: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nJuliette: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
        typewriter(dialouge1)
        print(neville)
        typewriter(dialouge2)
        imcrying.remove('neville')
      if neville==1: 
        icecream.append("neville")
       
      if bartholomew==2: 
        dialouge1=("\n\nGame:The butler has the highest votes of")
        dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
        typewriter(dialouge1)
        print(bartholomew)
        typewriter(dialouge2)
        imcrying.remove('bartholomew')
      if bartholomew==1: 
        icecream.append("bartholomew")
        
      if irving==2: 
        dialouge1=("\n\nGame:The priest has the highest votes of")
        dialouge2=("\n\nAnabel: It has got to be the priest right? It only makes sense.\n\nCassian: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nSebastian: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nAnabel: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nJuliette: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nCassian: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
        typewriter(dialouge1)
        print(irving)
        typewriter(dialouge2)
        imcrying.remove('irving')
        rounds-=3
      if irving==1: 
        icecream.append("irving")
      
      if maxim==2: 
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nSebastian: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nAnabel: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
        typewriter(dialouge1)
        print(maxim)
        typewriter(dialouge2)
        imcrying.remove('maxim')
        
      if maxim==1: 
        icecream.append("maxim")
       
      if barnabas==2: 
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nJuliette: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nCassian: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
        typewriter(dialouge1)
        print(barnabas)
        typewriter(dialouge2)
        imcrying.remove('barnabas')
        
      if barnabas==1: 
        icecream.append("barnabas")
        
      if chrysantha==2: 
        dialouge1=("\n\nGame:The page has the highest votes of")
        dialouge2=("\n\nPage: Why did Crysythia get voted out?\n\nSebastian: Your Crysythia\n\nPage: Yes but why did she get voted out!\n\nAnabel: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nJuliette: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
        typewriter(dialouge1)
        print(chrysantha)
        typewriter(dialouge2)
        imcrying.remove('chrysantha')
      if chrysantha==1: 
        icecream.append("chrysantha")
  if len(icecream)==2: 
    game=("\n\nThere has been a tie between")
    hello=("Since there is a tie, one will randomly get voted out")
    typewriter(game)
    print(icecream[0],icecream[1])
    typewriter(hello)
    number=random.randint(1,2)
    if number==1:   
      del icecream[0]
    if number==2: 
      del icecream[1]
    if len(icecream)==1:
      if icecream[0] in "edmund": 
        dialouge1=("\n\nGame:The king has the highest votes of")
        dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nCassian: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nSebastian: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nAnabel: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nJuliette: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nCassian: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
        typewriter(dialouge1)
        print(edmund)
        typewriter(dialouge2)
        imcrying.remove('edmund')
      elif icecream[0] in "winifred":
        dialouge1=("\n\nGame:The seamstress has the highest votes of")
        dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nSebastian:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nAnabel: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
        typewriter(dialouge1)
        print(winifred)
        typewriter(dialouge2)
        imcrying.remove('winifred')
      elif icecream[0] in "neville":
        dialouge1=("\n\nGame:The cook has the highest votes of")
        dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nJuliette: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nCassian: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nSebastian: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
        typewriter(dialouge1)
        print(neville)
        typewriter(dialouge2)
        imcrying.remove('neville')
      elif icecream[0] in "bartholomew": 
        dialouge1=("\n\nGame:The butler has the highest votes of")
        dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
        typewriter(dialouge1)
        print(bartholomew)
        typewriter(dialouge2)
        imcrying.remove('bartholomew')
      elif icecream[0] in "irving": 
        dialouge1=("\n\nGame:The priest has the highest votes of")
        dialouge2=("\n\nAnabel: It has got to be the priest right? It only makes sense.\n\nJuliette: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nCassian: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nSebastian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nAnabel: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nJuliette: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
        typewriter(dialouge1)
        print(irving)
        typewriter(dialouge2)
        imcrying.remove('irving')
        rounds-=3
      elif icecream[0] in 'maxim':
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nCassian: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nSebastian: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
        typewriter(dialouge1)
        print(maxim)
        typewriter(dialouge2)
        imcrying.remove('maxim')
      elif icecream[0] in 'barnabas': 
        dialouge1=("\n\nGame:The knight has the highest votes of")
        dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nAnabel: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nJuliette: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
        typewriter(dialouge1)
        print(barnabas)
        typewriter(dialouge2)
        imcrying.remove('barnabas')
      elif icecream[0] in 'chrysantha':
        dialouge1=("\n\nGame:The page has the highest votes of")
        dialouge2=("\n\nPage: Why did chrysantha get voted out?\n\nCassian: Your Crysythia\n\nPage: Yes but why did she get voted out!\n\nSebastian: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nAnabel: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
        typewriter(dialouge1)
        print(chrysantha)
        typewriter(dialouge2)
        imcrying.remove('chrysantha')
 

  #intermission, maybe add convo between characters, then game summons them


  
  if players==1: 
    if edmund==1: 
        dialouge1=("\n\nGame:The king has the highest vote!")
        dialouge2=("\n\nKing: I am appalled, how could you vote me, the king!\n\nJuliette: You seemed to speak vehemently about the Queen, did you murder her so you wouldn’t have to fix her mistakes? \n\nKing: No I swear, I didn’t like her, but I didn’t hate her. It's immoral for me to kill the queen, I could never do that. \n\nCassian: We also found a knife under your bed! The Queen died because there was a knife mark. \n\nKing: How dare you sneak around my room! Someone must have framed me, who would have easy access and get a knife? I am gone during the afternoon someone must have placed it there. \n\nSebastian: ….Or you snuck out during the afternoon and took the knife from the cook. We heard from the cook that one of his knives was missing during the afternoon. \n\nAnabel: Or maybe the King is telling the truth and the reason why the killer targetted the king was that the king is out during the afternoons. \n\nGame: It is too late the King has been voted out…\n\nJuliette: Maybe the cook was lying and said the knife was gone, or maybe the knight took the knife because he doesn’t have duties on that day. I’m not sure. We still have to keep all the other castle members under suspicion.")
        typewriter(dialouge1)
        
        typewriter(dialouge2)  
        imcrying.remove('edmund')
    
       
    if winifred==1: 
      dialouge1=("\n\nGame:Winifred has the highest votes of")
      dialouge2=("\n\nSeamstress: How could you guys vote for me? I didn’t do anything wrong. I would never kill the Queen, she was always so kind to me.\n\nCassian:But you knew the Queen and the gardener were having an affair, and you seemed quite close with the gardener last time I saw.\n\nSeamstress: WHAT? How could you say that. It’s not like I’m in love with the gardener or anything. \n\nSebastian: Hmmm… okay, I believe you. I do not think you killed the Queen, but I’m not sure what is going on between you and the gardener.\n\nGame: The Seamstress has been voted out….")
      typewriter(dialouge1)
      print(winifred)
      typewriter(dialouge2)
      imcrying.remove('winifred')
     
        
    if neville==1: 
      dialouge1=("\n\nGame:The cook has the highest votes of")
      dialouge2=("\n\nCook: Why would you vote for me? Why would I want to kill the queen and Celeste was my girlfriend I’m heartbroken about her death.\n\nAnabel: Well you could’ve just been using her, you said someone took the knife, was it you? You are out during the afternoons which means you could frame some during that time. Also when we talked to the maid she said you and the priest were in the kitchen and are never there.\n\nCook: No I promise I didn’t take the knife!! I didn’t kill the queen! And I didn’t kill my girlfriend!\n\nJuliette: Hmm…\n\nCook: Curse you\n\nGame: The cook has been voted out…\n\nCassian: Wait. I think I remember Mirabel saying that she saw someone go to the kitchen during the afternoon, I don’t think it was the cook.")
      typewriter(dialouge1)
      print(neville)
      typewriter(dialouge2)
      imcrying.remove('neville')
      
       
    if bartholomew==1: 
      dialouge1=("\n\nGame:The butler has the highest votes of")
      dialouge2=("\n\nButler: *gasp* you think mwa is the killer? I am a Butler, why would I kill the Queen? I had nothing but respect for her. \n\nPlayer: There was broken glass next to the Garden, and we found out it wasn’t the Gardener. So, why was there broken glass? Was someone trying to frame the Gardener, you were the one who delivered this information, which makes you the most suspicious.\n\nButler: I…\n\nPlayer: Exactly, can’t come up with an excuse, huh? \n\nButler: This is unbelievable!!!! \n\nGame: The Butler has been voted out…")
      typewriter(dialouge1)
      print(bartholomew)
      typewriter(dialouge2)
      imcrying.remove('bartholomew')
     
    if irving==1: 
      dialouge1=("\n\nGame:The priest has the highest votes of")
      dialouge2=("\n\nSebastian: It has got to be the priest right? It only makes sense.\n\nAnabel: I can’t think of his motive, but all the clues add up. For example, when we first met with the priest, the priest was wearing a blue cassock. However, priests usually only wear white cassocks, and it is unusual for them to wear blue ones. Theres only one reason the priest would be wearing a blue cassock, because he killed the Queen and her blood stained the bright white cassock. Additionally, many castle members saw flashes of white around the castle, expically on the night of the Queen’s death. \n\nJuliette: Right…when we entered the church it was sparkling clean, he must have cleaned the blood, however, he left the blood stains on the east wing because he forgot to clean that up. The east wing only has 3 places it leads to, garden storage room, knight armory, and the church. We already established it wasn’t the garden. \n\nCassian: He also tried to frame the Doctor! Remember, he said he smelled a nutty scent on the Queen, which was the smell of cyanide. However, we know the death of the Queen was by knife not poison so the priest could not have smelled the poisonous scent on her. That was the flaw. Irving, got poison and framed him. \n\nSebastian: Yes, he also tried to frame the King too. During the afternoon, a maid saw a flash of white, which was the priest. He said he didn’t have anything in the afternoon, the cook, the king along with the knight didn’t either. So, he snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nPriest: *in a high voice* why- *ahem, attempts to speak in a lower voice* why would you accuse me!\n\nAnabel: it has to be the priest, and why is your voice so high?\n\nPriest: I guess it doesn’t matter now that I tell you, but I am actually a women. As you know, priests cannot be woman, so I pretended to be a man to get this job.\n\nGame: The priest has been voted out… ")
      typewriter(dialouge1)
      print(irving)
      typewriter(dialouge2)
      imcrying.remove('irving')
      rounds=-3
      
    if maxim==1: 
      dialouge1=("\n\nGame:The knight has the highest votes of")
      dialouge2=("\n\nKnight: Why would you think I would do such a thing?! I’m a knight, it is my duty to protect the castle at all costs.\n\nJuliette: But you heard the footsteps and followed them, but didn’t find anything? How is that possible?\n\nKnight: Correct, I did follow footsteps, but I never actually followed anyone. I’m not sure why I was voted out.\n\nCassian: Okay, okay, we believe you. We’ll let you go.\n\nGame:Maxum has been voted out")
      typewriter(dialouge1)
      print(maxim)
      typewriter(dialouge2)
      imcrying.remove('maxim')
        
      
    if barnabas==1: 
      dialouge1=("\n\nGame:The knight has the highest votes of")
      dialouge2=("\n\nKnight: I swear I didn’t see anymore than the glimpse of white! If I did, I would have told you, I swear. Please don’t come after me, I’m innocent.\n\nSebastian: Hmm… okay, we believe you. I’m confused by this glimpse of white that you saw.\n\nKnight: Yes, it could have been my vision though, like I said earlier.\n\nAnabel: Okay, interesting. You are now pronounced an innocent person.\n\nGame: its too late the knight has been voted out")
      typewriter(dialouge1)
      print(barnabas)
      typewriter(dialouge2)
      imcrying.remove('barnabas')
        
    
    if chrysantha==1: 
      dialouge1=("\n\nGame:The page has the highest votes of")
      dialouge2=("\n\nPage: Why did Chrysantha get voted out?\n\nJuliette: Your Chrysantha\n\nPage: Yes but why did she get voted out!\n\nCassian: Because you had a very confusing storyline when we talked to you!\n\nPage: She told you she saw blood in the east wing and now your voting her out?\n\nCassian: Yes because you were acting like you didn’t know whose blood it was and it was weird.\n\nPage: Go ask the people in the East Wing!\n\nGame: The page has been voted out…")
      typewriter(dialouge1)
      print(chrysantha)
      typewriter(dialouge2)
      imcrying.remove('chrysantha')
      
  anotherlist.clear()
  anotherlist2.clear()
  itsten.clear()
  icecream.clear()
  rounds-=1

if "irving" in imcrying:
  dying=("\n\n...LOADING...\n\nPreist: i cannot let you detectives continue voting, yes I am the murderer and I must murder you guys now that you have gotten too close to my secret. \n\nAll players: Ahhhhhhhh\n\nPriest: Now that you’ll never see the light of day again I guess I’ll explain what happened to you. So I killed the queen because she realized I was a woman, yes I’m a woman I wanted to become a priest but woman can’t so I pretended to be a man. Then the maids found out so I killed them too and now I’ll kill you guys!\n\nPriest: I was wearing a blue cassock, even though I usually only wear white cassocks. There's only one reason why I was wearing a blue cassock, and it is because I killed the Queen and her blood stained my white cassock. Many castle members saw flashes of white around the castle, especially on the night of the Queen’s death, and it was me. I cleaned the church thouroughly, but I accidently left some blood stains in the east wing. The east wing only has three places it leads to: the garden storage room, the knight armory, and the church.I also tried to frame the Doctor by placing a drop of the nutty scented cyanide on the Queen. However, I killed her with a knife and not poison, making me seem innocent. I placed the bottle of cyanide in the doctor’s medicine cabinet. I also tried to frame the King too. I snuck into the kitchen to steal a knife, murder the queen, and plant it in the King’s room. \n\nAll players: *Scream as they die*")
  
  typewriter(dying)
  game=("\n\n...LOADING...\n\nYou have lost the murder mystery game")
  typewriter(game)
  #addmoredramaticending



if "irving" not in imcrying:
  if "win" in player1:
    game=("congradulations, player 1 has won the game! They purchased the sheriff title and killed the right castle member. Since they won themselves, they get all the money and win the game. The rest of you detectives loose!")
    typewriter(game)
  elif "win" in player2: 
    game=("congradulations, player 2 has won the game! They purchased the sheriff title and killed the right castle member. Since they won themselves, they get all the money and win the game. The rest of you detectives loose!")
    typewriter(game)
  elif "win" in player3: 
    game=("congradulations, player 3 has won the game! They purchased the sheriff title and killed the right castle member. Since they won themselves, they get all the money and win the game. The rest of you detectives loose!")
    typewriter(game)
  elif "win" in player4: 
    game=("congradulations, player 4 has won the game! They purchased the sheriff title and killed the right castle member. Since they won themselves, they get all the money and win the game. The rest of you detectives loose!")
    typewriter(game)
  elif "mystery" in player1:
    game=("Unfortunatly, player 1 was the joker and did not suceed in tricking the rest of the players into voting other castle members. They lost. However, congratulations to the rest ofdetectives! You have found the killer, amongst you all, you will all get to split 200,000 shillings\n\n...LOADING...\n\nBaker: I see you have successfully caught the murderer, actually I didn’t expect that from you guys. Thank you for paying me all the debt you owed, and congratulations on catching the killer. Please come by anytime since you can actually pay me…")
    typewriter(game)
  elif "mystery" in player2: 
    game=("Unfortunatly, player 2 was the joker and did not suceed in tricking the rest of the players into voting other castle members. They lost. However, congratulations to the rest ofdetectives! You have found the killer, amongst you all, you will all get to split 200,000 shillings\n\n...LOADING...\n\nBaker: I see you have successfully caught the murderer, actually I didn’t expect that from you guys. Thank you for paying me all the debt you owed, and congratulations on catching the killer. Please come by anytime since you can actually pay me…")
    typewriter(game)
  elif "mystery" in player3: 
    game=("Unfortunatly, player 3 was the joker and did not suceed in tricking the rest of the players into voting other castle members. They lost. However, congratulations to the rest ofdetectives! You have found the killer, amongst you all, you will all get to split 200,000 shillings\n\n...LOADING...\n\nBaker: I see you have successfully caught the murderer, actually I didn’t expect that from you guys. Thank you for paying me all the debt you owed, and congratulations on catching the killer. Please come by anytime since you can actually pay me…")
    typewriter(game)
  elif "mystery" in player4: 
    game=("Unfortunatly, player 4 was the joker and did not suceed in tricking the rest of the players into voting other castle members. They lost. However, congratulations to the rest ofdetectives! You have found the killer, amongst you all, you will all get to split 200,000 shillings\n\n...LOADING...\n\nBaker: I see you have successfully caught the murderer, actually I didn’t expect that from you guys. Thank you for paying me all the debt you owed, and congratulations on catching the killer. Please come by anytime since you can actually pay me…")
    typewriter(game) 
  else: 
    game=("\nGame: Congratulations detectives! You have found the killer, amongst you 4 you will all get to split 200,000 shillings\n\n...LOADING...\n\nBaker: I see you have successfully caught the murderer, actually I didn’t expect that from you guys. Thank you for paying me all the debt you owed, and congratulations on catching the killer. Please come by anytime since you can actually pay me…")
    typewriter(game)


if "irving" in imcrying: 
  if "mystery" in player1:
    game=("congradulations, player 1 has won the game! They purchased the mystery title and got the role as the joker. Basically, they fooled everyone else into voting the wrong killer, so they win and all the other detectives loose")
    typewriter(game)
  elif "mystery" in player2: 
    game=("congradulations, player 2 has won the game! They purchased the mystery title and got the role as the joker. Basically, they fooled everyone else into voting the wrong killer, so they win and all the other detectives loose")
    typewriter(game)
  elif "mystery" in player3: 
    game=("congradulations, player 3 has won the game! They purchased the mystery title and got the role as the joker. Basically, they fooled everyone else into voting the wrong killer, so they win and all the other detectives loose")
    typewriter(game)
  elif "mystery" in player4: 
    game=("congradulations, player 4 has won the game! They purchased the mystery title and got the role as the joker. Basically, they fooled everyone else into voting the wrong killer, so they win and all the other detectives loose")
    typewriter(game)
  else: 
    game=("\nGame: Unfortunatly all of you detectives did not catch the killer, as a result the priest has killed you all...")
    typewriter(game)