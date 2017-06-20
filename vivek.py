#import details of spy from file spy_details
from spy_details import spy,Spy,ChatMessage,friends
#to use steganography module
from steganography.steganography import Steganography
from datetime import datetime
import string
from termcolor import *
import colorama
colorama.init()
message_word_list=[]


STATUS_MESSAGES=["HOLA","NEW TO SPY CHAT","BORED"]


#function to add a status
def add_status():
    updated_status_message=None
    if spy.current_status_message!=None:
        print"your current status message is %s \n"%(spy.current_status_message)
    else:
        print"you dont have current status message \n "


    default=raw_input("Do you want to select from previously used status (Y/N)?")

    if default.upper()=="N":
        #entering a new status
        new_status_message=raw_input("Enter the new status: \n")
        if len(new_status_message)>0:
            #add status to list of status you have used previously
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message=new_status_message


    elif default.upper()=="Y":
        #search in the old status you had put
        item_position=1

        for message in STATUS_MESSAGES:
            print"%d  . %s "%(item_position,message)
            item_position=item_position+1
        message_selection=int(raw_input("Choose the serial number of status you want to put as your status"))

        if len(STATUS_MESSAGES)>=message_selection:
            #suppose there are 3 entries then message selection is not greater than 3 else an error will occur
            updated_status_message=STATUS_MESSAGES[message_selection-1]


    else:
        print"The option you choose is not valid"
    if updated_status_message:
        print"Your updated status message is %s"%(updated_status_message)
    else:
        print"You didn't update your status"


    return updated_status_message


#function to edit your information
def update_info():
    print"YOU CAN UPDATE THESE?"
    print" 1. SPY NAME"
    print" 2. SPY AGE"
    print" 3. SPY RATING"
    menu_choices = "What would you like to update?"
    menu_choice = int(raw_input(menu_choices))
    #enter choice in integer

    if menu_choice == 1:
        spy.name = raw_input("enter new name")
        spy.salutation = raw_input("may we call you Mr. or Miss ?")
        spy.name = spy.salutation + " " + spy.name

    elif menu_choice == 2:
        spy.age = int(raw_input("enter new age"))

    elif menu_choice == 3:
        spy.rating = float(raw_input("enter new rating"))
    else:
        print"wrong choice"
    print"after updating!!!!!!!!!!!!!"
    print"%s \nage: %d \nrating : %.2f " % (spy.name, spy.age, spy.rating)



#function to add a friend
def add_friend():
    new_friend=Spy("","",0,0.0)

    #enter data of friend
    new_friend.name=raw_input("Enter the name of the friend : ")
    new_friend.salutation=raw_input("Enter salutation of your friend : ")
    new_friend.name=new_friend.salutation + " " + new_friend.name
    new_friend.age=int(raw_input("Enter the age of your friend : "))
    new_friend.rating=float(raw_input("Enter the rating of your friend : "))


    #condition to be a spy friend
    if len(new_friend.name)>0 and new_friend.age>12 and new_friend.age<50:
        friends.append(new_friend)
        print"You are now friend with %s"%(new_friend.name)
    else:
        print"Friend with this data can not be added"
    return len(friends)



#function to select among all the friends
def select_a_friend():
    item_number=1

    for friend in friends:
        print"%d. %s %s aged %d and rating %.2f"%(item_number,friend.salutation,friend.name,friend.age,friend.rating)
        item_number=item_number+1

    #choosing a friend
    friend_choice=raw_input("Enter serial number of friend you want to choose")
    friend_choice_position=int(friend_choice)-1
    #one is reduced because of zero indexing

    return friend_choice_position


#function to send a message
def send_message():
    #call a function select_a_friend which returns a specific selected friend
    friend_choice=select_a_friend()

    #enter the path of image in which message is to be encoded
    original_image=raw_input("Enter the name of image?")

    #enter the name of image in which input image and text encoded is stored
    output_path="output1.jpg"

    #text to be encoded
    text=raw_input("Enter the message")
    if len(text)>0:
        #when u really enter a secret text


        #steganography module to perform its task
        Steganography.encode(original_image,output_path,text)

        #chat with label send by me
        new_chat=ChatMessage(text,True)

        friends[friend_choice].chats.append(new_chat)
        #chat saved to a particular friend chat
        print"your secret message is ready"
    else:
        print"u didnt put a message "

#function to decode a message
def read_message():

    #select a friend
    sender=select_a_friend()
    #select the image in which the message is to be decoded
    output_path=raw_input("What is the name of file")

    #module to decode the text
    secret_text=Steganography.decode(output_path)
    message_word_list=secret_text.split()
    if len(message_word_list)>200:
        #if he speak too much
        friends.pop(sender)
        #remove him
        print "you speak too much .... hence removed "
    if message_word_list.count("sos")>=1 or message_word_list.count("save")>=1 or message_word_list.count("help")>=1 or message_word_list.count("SOS"):
        print"the is an emergency"

    new_chat=ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    #chat saved
    print"Your secret message has been saved"


#function to read chat history of a friend
def read_chat_history():
    #select a friend
    read_for=select_a_friend()

    #printing a chat
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)

        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)



#start chat function
def start_chat(spy):

    spy.name=spy.salutation+" "+spy.name
    if spy.age>12 and spy.age<50:
        #conditions of a spy
        print"********************Welcome********************"
        print"%s \nage: %d \nrating : %.2f " % (spy.name, spy.age, spy.rating)
        show_menu=True
        #until it is true menu will be shown
        while show_menu:
            print"Enter the serial number of task you want to perform :"
            menu_choices="1.Update information \n2.Add a status update \n3. Add a friend \n4. Send a secret message \n5. Read a secret message \n6. Read Chats from a user \n7. Close Application \n"
            menu_choice=raw_input(menu_choices)
            #according to choice a action is performed
            if len(menu_choice)>0:
                menu_choice=int(menu_choice)
                if menu_choice==1:
                    update_info()
                elif menu_choice==2:
                    spy.current_status_message=add_status()
                elif menu_choice==3:
                    no_of_friends=add_friend()
                    print "Your total friends: " + str(no_of_friends)
                elif menu_choice==4:
                    send_message()
                elif menu_choice==5:
                    read_message()
                elif menu_choice==6:
                    read_chat_history()
                else:
                    show_menu=False
                    #to stop showing menu
    else:
        print"You are not of correct age to be spy"


def start():
    question = "Is it " + spy.salutation + spy.name + " (Y/N)?"
    # asks if you want to continue with the same spy with detail in spy_detail or add new spy
    existing = raw_input(question)
    if (existing.upper() == 'Y'):
        # same person
        print "WELCOME BACK"
        spy.name = spy.salutation + " " + spy.name
        spy_password = raw_input("enter your password please")
        #password so that no one else can log in
        if spy_password == "asdf":
            start_chat(spy)
        else:
            print"wrong password"

    else:
        # enter new name
        name = raw_input("welcome to spy chat , Enter your name :")
        try:
            assert any([char not in string.ascii_letters for char in name]) is False

            if len(name) > 0:
                print "welcome " + name
                spy.name=name
                spy.salutation = raw_input("should i call u Mr.  or Miss? ")
                spy.name = spy.salutation + " " + spy.name
                print " Okay , Welcome " + spy.name
                spy.age = int(raw_input("what is your age? "))

                if (spy.age > 12 and spy.age < 50):
                    print "age valid"
                    spy.rating = float(raw_input("Enter the rating:"))
                    spy.is_online = True

                else:
                    print"invalid age"
                start_chat(spy)
            else:
                print" "

        except AssertionError:
            print"your name must contain letters only"
            start()
        else:
            print " you need to fill your name "


start()

