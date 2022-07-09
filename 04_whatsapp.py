import pywhatkit

#phone_number = input("Enter phone number: ")
phone_number = "+6014-3414547"
pywhatkit.sendwhatmsg(phone_number, "This is a test msg sent by a Python script!", 11, 29)