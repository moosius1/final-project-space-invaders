# Cheri Hansen - han19067@byui.edu
# Program to start space invaders
# Created 3/23/22
# CSE 210-03 Final Project

from game.scheduler import Scheduler

# main function that starts program
def main():
    scheduler = Scheduler()
    scheduler.playGame()

# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()