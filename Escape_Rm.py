"""
Program: Assesment A, Escape Room
Author Name: Mike Wycoff
Last Date Modified: 9/26/21

This program is a word game to try to get out of a room.
"""

#imports
from time import strftime

#boolean variables
play = True

open_door     = False
open_desk     = False
open_book     = False
take_guitar   = False
take_book     = False
take_key      = False
take_painting = False
take_keycard  = False
book          = False
break_window  = False
play_piano    = False

sack = 0

greetings = "Greetings from 'THE ESCAPE ROOM'! Search the room to find the objects needed to escape the room.  If possible.  Good Luck My Friend."
room_description = "You find yourself alone in a room. You look around and see a bookshelf, a desk, and a single chair.  There also appears to be an old piano and a guitar.  You notice that on the four walls there is a clock on one, a painting on another, and on the last two, one has a door, and the other has a window."
words_of_wisdom = "Although the room is fairly empty, you can take your time. Enjoy yourself. Remember, it's only a game."
basic_command = "Type 'menu' to see a menu. Type 'quit' to exit the game." 

print(greetings)
print(room_description)
print(words_of_wisdom)
print(basic_command)

while(play):
    command = input("Type Command: ")

    if(command == 'quit'):
        play = False
#Menu
    elif(command == 'menu'):
        print("*"*56)
        print("**             Commands Used In This Game             **")
        print("**----------------------------------------------------**")
        print("** menu      - To see this menu                       **")
        print("** look      - To examine objects in the room         **")
        print("** take      - To place an object in your inventory   **")
        print("** sack      - To view items in your inventory        **")
        print("** use       - To use an object                       **")
        print("** open      - To open an object                      **")
        print("** break     - To break an object                     **")
        print("** quit      - To exit the game                       **")
        print("*"*56)
        print("**                Interaction Commands                **")
        print("**----------------------------------------------------**")
        print("** bookshelf - To interact with a bookshelf           **")
        print("** desk      - To interact with a desk                **")
        print("** chair     - To interact with a chair               **")
        print("** clock     - To interact with a clock               **")
        print("** guitar    - To interact with a guitar              **")
        print("** piano     - To interact with a piano               **")
        print("** window    - To interact with a window              **")
        print("** door      - To interact with a door                **")
        print("** painting  - To interact with a painting            **")
        print("** book      - To interact with a book                **")
        print("** keycard   - To interact with a keycard             **")
        print("** key       - To interact with a key                 **")
        print("**----------------------------------------------------**")
        print("**        Note: Feel free to enter any word           **")
        print("**               and see what happens.                **")  
        print("*"*56)
#Sack(Inventory)
    elif(command == 'sack'):
        print("*"*31)
        print("**    Items In Your Sack     **")
        print("**---------------------------**")
        if(take_guitar):
            sack +=1
            print("** guitar                    **")
        if(take_book):
            sack +=1
            print("** book                      **")
        if(take_key):
            sack +=1
            print("** key                       **")
        if(take_painting):
            sack +=1
            print("** painting                  **")
        if(take_keycard):
            sack +=1
            print("** keycard                   **")
        if(sack == 0):
            print("**         -Empty-           **")
        print("**---------------------------**")
        print("*"*31)
#Open
    elif(command == 'open'):
        command_open = input("What do you want to Open? ")
        if(command_open == 'bookshelf'):
            print("Bookshelf cannot be opened.")
        elif(command_open == 'desk'):
            if(take_key == True):
                print("You reach into your sack and notice the key.  You should use it to see if it opens the desk.")
            else:
                print("Desk will not open. It appears to be locked.  Maybe there's a key somewhere?")
        elif(command_open == 'book'):
            if(book == True):
                open_book = True
                print("You found a key!  What could it open?  You should put it in your sack so you can use it.")
            else:
                print("You can't even get the book from the bookshelf. How are you supposed to open it?")
        elif(command_open == 'chair'):
            print("Chair cannot be opened.")
        elif(command_open == 'clock'):
            print("Clock cannot be opened") 
        elif(command_open == 'guitar'):
            print("Guitar cannot be opened.")
        elif(command_open == 'piano'):
            print("You see the strings and key hammers in the piano. There is nothing of interest.")
        elif(command_open == 'window'):
            print("Window is stuck and will not open. There doesn't even seem to be a way to unlock it.")
        elif(command_open == 'door'):
            print("Door will not open. It appears to need a keycard.")
        elif(command_open == 'painting'):
            print("Painting cannot be opened")
        else:
            print("Be Careful!  You can't do that.") 
#Look
    elif(command == 'look'):
        command_look = input("What would you like to examine? ")
        if(command_look == 'bookshelf'):
            if(play_piano == True):
                print("You see an old book that appears to be out of place. You notice it has come loose.  Maybe you should take it and/or open it.  If you use the book, maybe you could learn something.  I bet people tell you that you should read more often anyway.")
            elif(take_book == True):
                book = True
                print("The book is no longer on the shelf.  You probably dropped it on the floor.  Did you put it in your sack.  If you didn't, then you probably should so you can use it.") 
            else:
                print("You see an old book that appears to be out of place.  It is stuck.")
        elif(command_look == 'floor'):
            if(book == True):
                print("Did you drop the book on the floor? Pick it up and put it in your sack!  That way you can use it.")
            else:
                print("Why are you stairing at a dirty floor?  There's nothing to see there.")
        elif(command_look == 'desk'):
            print("You notice that their is nothing on top of the desk.  There is a drawer that won't open. It appears to need a key. If only you could get it open.  Then you could see what is inside of it.")
        elif(command_look == 'chair'):
            print("The chair is brown, but appears to have nothing of interest. How ever it might make a creeking sound if you rock it.")
        elif(command_look == 'clock'):
            clock_hour   = int(strftime("%H"))
            clock_minute = int(strftime("%M"))
            clock_tag    = "AM"
            if(clock_minute < 10):
                clock_minute = "0"+str(clock_minute)
            if(clock_hour > 11):
                clock_tag = "PM"
            if(clock_hour > 12):
                clock_hour -= 12
            if(clock_hour == 0):
                clock_hour = 12
            print("The time on the clock reads "+str(clock_hour)+":"+str(clock_minute)+" "+clock_tag+" You really should try to find a way out.")
        elif(command_look == 'guitar'):
            print("It seems like you could strum the guitars strings.")
        elif(command_look == 'piano'):
            print("The piano seems a little dusty, but maybe you should play it anyway.")
        elif(command_look == 'window'):
            print("The window glass is fogged up and you can't see what's on the otherside.  Maybe you should try to find a way to open it.")
        elif(command_look == 'door'):
            print("It appears to be a metal door.  You could try to open it, although it appears to need a keycard. Maybe you could break it with something?")
        elif(command_look == 'painting'):
            print("The painting appears to be of an old farmstead being ripped apart by a tornado.  Why would someone paint that?")
        elif(command_look == 'room'):
            if(take_guitar == True):
                print("You look around and see a bookshelf, a desk, and a single chair.  There also appears to be an old piano.  The guitar is no longer in it's spot since you have placed it in your sack.  You notice that on the four walls there is a clock on one, a painting on another, and on the last two, one has a door, and the other has a window.")
            elif(take_painting == True):
                print("You look around and see a bookshelf, a desk, and a single chair.  There also appears to be an old piano and a guitar.  You notice that on the four walls there is a clock on one, a shadowed spot where a painting used to hang on the other because some THIEF decided to place it in their sack, and on the last two, one has a door, and the other has a window.") 
            elif(take_guitar == True and take_painting == True):
                print("You look around and see a bookshelf, a desk, and a single chair.  There also appears to be an old piano.  The guitar is no longer in it's spot since you have placed it in your sack.  You notice that on the four walls there is a clock on one, a shadowed spot where a painting used to hang on the other because some THIEF decided to place it in their sack, and on the last two, one has a door, and the other has a window.")
            else:
                print(room_description)
        else:
            print("You probably don't want to see that.  Check something else.  Besides, there's nothing to see there anyway.")
#Play
    elif(command == 'play'):
        command_play = input("Want to make some music? What would you like to play? ")
        if(command_play == 'bookshelf'):
            print("How is it even possible to play a bookshelf? Play something else!")
        elif(command_play == 'desk'):
            print("Really? You're trying to play a desk?")
        elif(command_play == 'chair'):
            print("You rock the chair. It makes a creeking sound.")
        elif(command_play == 'clock'):
            print("It's a clock, not an instument, Why don't you try to put it in your sack?")
        elif(command_play == 'guitar'):
            print("You Strum the Guitar. It sounds out of tune. Maybe you should put it in your sack.  It might be useful for something else.")
        elif(command_play == 'piano'):
            play_piano = True
            book = True
            print("You hit some keys on the piano. It surprisingly sounds good. Maybe you should play the piano more often.  You seem to be pretty good at it.  With some practice people might even pay you to play it for them. I see that smile on your face.  PAY ATTENTION! You need to get out of here first.  It seems like a book on the shelf has come loose.  You should look at the bookshelf.")
        elif(command_play == 'window'):
            print("What do you think you're doing?  Nothing happens.")
        elif(command_play == 'door'):
            print("IT'S A DOOR!  You can't play it.")
        elif(command_play == 'painting'):
            print("It's not possible to play a painting.")
        else:
            print("YOU CAN'T PLAY THAT!  Stop screwing around.")
#Take
    elif(command == 'take'):
        command_take = input("Let's put stuff in your sack.  What do you want to put there? ")
        if(command_take == 'bookshelf'):
            print("The bookshelf is too big to fit in your sack.")
        elif(command_take == 'balls'):
            print("There are no balls to put in your sack.")
        elif(command_take == 'desk'):
            print("The desk is too big to fit in your sack")
        elif(command_take == 'keycard'):
            if(open_desk == True):
                print("You take the keycard out of the desk and place it in your sack.")     
            else:
                print("You can't take something you haven't found yet!  You don't even know if one is in the room yet.")
        elif(command_take == 'chair'):
            print("You cannot place the chair in you sack.")
        elif(command_take == 'clock'):
            print("The clock is stuck to the wall.  You can't put it in your sack.")
        elif(command_take == 'guitar'):
            take_guitar = True
            print("You put the guitar in you sack.  Maybe you can use it for something later.")
        elif(command_take == 'piano'):
            print("Your sack isn't big enough to place the piano in it.  You could play the piano instead.")
        elif(command_take == 'window'):
            print("The window cannot be removed from the wall. Maybe it's an exit")
        elif(command_take == 'door'):
            print("How do you even expect to place a door in your sack?  You can't put the door there.")
        elif(command_take == 'painting'):
            take_painting = True
            print("STOP THIEF!  Oh well.  It appears you have put the painting in your sack.  Why would you even want that?  Have you seen it?")
        elif(command_take == 'book'):
            if(book == True):
                take_book = True
                print("You have successfully placed the book from the bookshelf in your sack.  Good things happen when you play the piano. You should open the book too.  Perhaps if you use it, you might find some useful information.")
            else:
                print("You can't take the book.  It's stuck on the bookshelf.")
        elif(command_take == 'key'):
            if(open_book == True):
                take_key = True
                print("You have placed the key in your sack.  See if it unlocks something")
            else:
                print("You don't have a key to place in your sack.")
        elif(command_take == 'keycard'):
            take_keycard = True
            open_desk = True
            print("You now have a keycard in your sack.  Was there somthing you could use that for?")
        else:
            print("I'm watching you. Don't even think about putting that in your sack!")
#Break
    elif(command == 'break'):
        command_break = input("You want to show your destructive side. What would you like to break? ")
        if(command_break == 'bookshelf'):
            if(take_book == True):
                print("You have destroyed the bookshelf.  I'm not sure why you did that, but you didn't need it anymore anyway.")
            else:
                print("You don't break the bookshelf.  There might be something of use on it.")
        elif(command_break == 'desk'):
            print("You've made a few dents, but you are unable to break the desk.")
        elif(command_break == 'chair'):
            print("You start ripping at the chair, but you soon get tired and deside not to break the chair, but to sit in it and rest instead.")
        elif(command_break == 'clock'):
            print("You decide that you would rather be able to see what the time is than to break the clock.  You should look at the clock instead.")
        elif(command_break == 'guitar'):
            print("You try and try to break the guitar, but it seems to be indestructable.  What's it made out of anyway?")
        elif(command_break == 'piano'):
            print("That seems like more effort then it's worth.  The piano remains unbroken.")
        elif(command_break == 'window'):
            print("You decide it's time to get out of here now!  You pick up the guitar and begin bashing it recklessly into the window.  Although the guitar remains unharmed, the window is shattered into tiney little pieces.  As you turn to see the light beeming through the broken window, you hear a loud explosion and everthing goes dark.")
            break_window = True
            if(break_window == True):
                play = False
        elif(command_break =='door'):
            print("The door cannot be broken.  It looks like you need a keycard to open it.")
        elif(command_break == 'painting'):
            print("Why would you want to break such a valuable piece of art? Just look at it.")
        else:
            print("You probably shouldn't break that.  You never know what might happen.")
#Use
    elif(command == 'use'):
        command_use = input("The use of tools. What would you like to use? ")
        if(command_use == 'bookshelf'):
            print("How do you expect to use a bookshelf?  You can't use it.")
        elif(command_use == 'desk'):
            print("If only you could see what was inside the desk.")
        elif(command_use == 'key'):
            if(take_key == True):
                open_desk = True
                take_keycard = True
                print("You go to the desk and attempt to use the key to open it.  First you miss putting the key in the key hole. 'Hopefully no one's watching. You feel a little embarrassed at your sudden lack of depth perception'.  You try again.  This time it works.  You open the desk to find a keycard.  You should put it in your sack.")
            elif(open_book == True):
                print("You should put the key in your sack.  That way you can use it if you need it.")
            elif(take_book == True):
                print("What are you trying to do? You don't have a key!  Did you try to open the book?")
            else:
                print("What are you trying to do? You don't have a key!")
        elif(command_use == 'chair'):
            print("You sit in the chair. Then you remember that you need to find a way out of the room. You stand up again.")
        elif(command_use == 'clock'):
            print("You should look at the clock instead.")
        elif(command_use == 'guitar'):
            print("What else can you use a guitar for besides playing it?")
        elif(command_use == 'piano'):
            print("Play me a song you're the piano man or woman")
        elif(command_use == 'window'):
            print("Now how do you expect to use a window?  If only there were another way.")
        elif(command_use == 'door'):
            if(take_keycard == True):
                print("There's a keycard in your sack. You should see if it unlocks the door.")  
            else:
                print("You can't use a door!  It appears that you need to find a keycard first.")
        elif(command_use == 'keycard'):
            if(take_keycard == True):
                print("You swipe the keycard in the door.  It beeps and a green light flashes.  You hear the latch unlock.  As you reach for the handle you think, 'Maybe I should take the piano with?', but you decide against it.  It's too heavy anyway.  You turn back to the now unlocked door.  You open it and proceed through.  You see a sign on the wall that says 'CONGRATULATIONS!!  You've Escaped?'.  At that point the door closes shut behind you and you realized you are in another room.  Only this one is empty.  The only exeption is it has the now locked door behind you and a sign that reads, 'CONGRATULATIONS!! You've Escaped?'.")
                play = False
            else:
                print("Quit screwing around! You can't use something you don't have!")
        elif(command_use == 'painting'):
            print("I'm not even sure what you're thinking.  I mean have you ever even 'used' a painting before?  You probably shouldn't do that.")
        elif(command_use == 'book'):
            if(take_book == True):
                print("Chapter 1 'ESCAPE!'  By now it's a safe assumtion that you are trapped in a room.  How did you manage that?  That's beside the point by now anyway.  If you've gotten to this point, you've already played the piano.  I hope you were better then the last person.  They obviosly had no musical skill and for their sake, tone def.  If you're reading me, you should have the key.  Otherwise you should open me.  It will unlock the desk.  A little hint to help you, DON'T BREAK THE WINDOW!")
            else:
                print("You want to read?  Did you forget that you're trying to get out of here?  Although if you insist.  You should have a book in your sack first.  Then you would have something to read.")
        elif(command_use == 'sack'):
            print("Quit playing with that!  You need to put things in it.")
        else:
            print("That's what you want to use?  You can't do that.")
    else:
       print("You Can't Do That Yet!")

print("GAME OVER")
        
