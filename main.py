import tello
import os
import time
import subprocess
import multiprocessing
import gui

def main():
    os.system("clear")

    # Connect to tello via Wifi
    tello.connect_routine("tello")

    # initialise
    tello.send_command("command",False)
    tello.send_command("streamon",False)

    videop = multiprocessing.Process(target=tello.get_video)
    videop.start()

    # launch gui
    guip = multiprocessing.Process(target=gui.get_command)
    guip.start()

if __name__ == '__main__':

    mainp = multiprocessing.Process(target=main)
    mainp.start()
