# Cheri Hansen - han19067@byui.edu
# Program to schedule space invaders modules
# Created 3/23/22
# CSE 210-03 Final Project

import pyray
import time

class Scheduler:

    def __init__(self):
        self._msec250=250
        self._msec100=100


    def playGame(self):
        # Initialize graphics...

        # Setup Timer
        timeStart = int(1000*time.time())
        windowIsOpen = True

        # Start of game loop
        while(windowIsOpen):
            # Setup current time
            timeCurr = int(1000*time.time())

            # Get keyboard inputs... 
            # Note: Won't work until graphics are working
            kb = pyray.get_key_pressed()

            # Validate exit command
            if (self.getExit(kb) == True):
                windowIsOpen = False

            # Output the graphics every 100 milliseconds
            if (((timeCurr-timeStart)%self._msec100)==0):
                # Put graphic command here.
                x = 5 # dummies command to get rid of errors

        # Close screen service...



    # This is to exit the program
    def getExit(self,kb):
        if ((kb > 0) and (kb == pyray.KEY_X)):
            return True
        return False

