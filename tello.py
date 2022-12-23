import os
import socket
import cv2
import subprocess
import time
import sys
import numpy as np

def send_command(cmd, gui=True):
    tello_address = ("192.168.10.1", 8889)
    local_address = ("0.0.0.0", 8889)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(local_address)

    sock.sendto(cmd.encode('utf-8'), tello_address)
    response, addr = sock.recvfrom(2048)

    if gui: # suppress return value when calling to init in main func
        decoded_response = response.decode("utf-8").strip("\n")
        return decoded_response

def get_state():
    state_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    state_sock.bind(("", 8890))
    response, addr = state_sock.recvfrom(2048)
    raw_state = response.decode("utf-8")
    states = raw_state.split(";")
    return states

def get_video():
    video = cv2.VideoCapture("udp://@0.0.0.0:11111")
    while video.isOpened():
        ret, frame = video.read()
        if ret :
            cv2.imshow('Tello', resize_frame(frame, 30))

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    video.release()
    cv2.destroyAllWindows()
    exit()

def resize_frame(frm, per):
    scale_percent = per # percent of original size
    width = int(frm.shape[1] * scale_percent / 100)
    height = int(frm.shape[0] * scale_percent / 100)
    return cv2.resize(frm, (width, height))

def shutdown():
    # reset wifi
    os.system("networksetup -setairportpower en0 off")
    os.system("networksetup -setairportpower en0 on")
    print("Shutting down...")
    os.system("clear")
    exit()

def connect_routine(ssid):
    connected = False
    while not connected :
        try:
            print("Connecting...")
            time.sleep(1)
            out = subprocess.check_output(['networksetup','-setairportnetwork','en0',ssid])
            output = out.decode('utf-8')
            if output == '':
                connected = True
                print("Connected to " + ssid)
                break
        except KeyboardInterrupt:
            tello.shutdown()
