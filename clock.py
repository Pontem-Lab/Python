#----------------------------------------
#---------- Scedule ---------------------
# This program about the week planning 
# exams, but it is can use for another
# purpose.
# import library about date and browser,
# becouse me take week day give x variable
# and then compare with all week days
# Open browser and open google.com
# This program is very simple, consisted of 
# three part.
# First part functions week day 
#----------------------------------------

import webbrowser
import datetime

x = y= z  = datetime.datetime.now()
print(x.strftime("WEEK .... ""%A"))
print(y.strftime("MONTH ... ""%x"))
print(z.strftime("HOUR .... ""%X"))
print("------- SCHEDULE --------")
x=x.strftime("%A")

def Mondey():
    print("English ..... 09:00 - 12:30")
    print("Istigate .... 13:00 - 18:00")

def Tuesday():
    print("Mathematic ..... 09:00 - 12:30")
    print("Python ......... 13:00 - 14:30")
    print("Istigate ....... 14:30 - 16:00")
    print("Communication .. 16:00 - 18:00")

def Wednesday():
    print("Python ..... 09:00 - 10:30")
    print("Python ..... 11:00 - 12:30")
    print("Skhemotekh . 13:00 - 18:00")

def Thursday():
    print("Mathematic .... 09:00 - 12:30")
    print("Python ........ 13:00 - 14:30")
    print("Istigate ...... 14:30 - 15:15")
    print("English ....... 15:25 - 18:00")

def Friday():
    print("English ........ 09:00 - 12:30")
    print("Python ......... 13:00 - 14:30")
    print("Presentation ... 14:30 - 15:30")
    print("Python Tutorial  15:30 - 16:30")


# Second part compare x for all day and find today
# show me tday exam and clock

Saturday=0
if x == "Saturday" or x == "Sunday":
    print("Homeworks")
else:
    if x == "Monday":
        Mondey()

    elif x == "Tuesday":
        Tuesday()

    elif x == "Wednesday":
        Wednesday()

    elif x == "Thursday":
        Thursday()

    else:
        Friday()


# Third open browser

webbrowser.open("https://w3schools.com")
webbrowser.open("https://translate.google.com")
webbrowser.open("https://google.com")













