#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import os

from twilio.rest import Client#TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)#TwilioRestClient(account_sid, auth_token)

GPIO.setmode(GPIO.BOARD)

#GPIO setup as outputs
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT)  
GPIO.setup(15, GPIO.OUT)

#GPIO setup as inputs
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

try:
    while True:
        buttonPressed = False
        if GPIO.input(12) == False:
            GPIO.output(7, False)
            os.system("date >> /home/pi/SSS400S/status.log")
            os.system("echo info >> /home/pi/SSS400S/status.log")
            os.system("echo >> /home/pi/SSS400S/status.log")
            os.system("sudo python /home/pi/SSS400S/uploadToGit.py")
            my_msg = "info"
            print "Message Sent."
            buttonPressed = True
        else:
            GPIO.output(7, True)
            
        if GPIO.input(16) == False:
            GPIO.output(11, False)
            os.system("date >> /home/pi/SSS400S/status.log")
            os.system("echo warning >> /home/pi/SSS400S/status.log")
            os.system("echo >> /home/pi/SSS400S/status.log")
            os.system("sudo python /home/pi/SSS400S/uploadToGit.py")
            my_msg = "warning"
            print "Message Sent."
            buttonPressed = True
        else:
            GPIO.output(11, True)
            
        if GPIO.input(18) == False:
            GPIO.output(13, False)
            os.system("date >> /home/pi/SSS400S/status.log")
            os.system("echo major fault >> /home/pi/SSS400S/status.log")
            os.system("echo >> /home/pi/SSS400S/status.log")
            os.system("sudo python /home/pi/SSS400S/uploadToGit.py")
            my_msg = "major fault"
            print "Message Sent."
            buttonPressed = True
        else:
            GPIO.output(13, True)
            
        if GPIO.input(22) == False:
            GPIO.output(15, False)
            os.system("date >> /home/pi/SSS400S/status.log")
            os.system("echo critical error >> /home/pi/SSS400S/status.log")
            os.system("echo >> /home/pi/SSS400S/status.log")
            os.system("sudo python /home/pi/SSS400S/uploadToGit.py")
            my_msg = "critical error"
            print "Message Sent."
            buttonPressed = True
        else:
            GPIO.output(15, True)
        
        if buttonPressed == True:
            message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
            #os.system("echo IT WORKS!!! >> /home/pi/SSS400S/status.log")
            #pass
        
        sleep(0.15)
            
except KeyboardInterrupt:
    print "\nKeyboard interrupt detected."
    #GPIO.cleanup()

except:
    print "Unforseen error occured!"
    #GPIO.cleanup()

finally:
    print "Closing Program..."
    GPIO.cleanup()
