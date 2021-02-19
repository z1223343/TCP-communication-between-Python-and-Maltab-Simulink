#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket
import time
import json
import numpy as np

# above are the python package that are needed installed correctly in your environment
# socket is for establishing and setting TCP
# time is for reading system time
# json is for encoding & decoding message
# numpy is for processing data matrix


# below is the main function that we use TCP

def tcp_sim():
    sever_port = ('127.0.0.1', 54320)
    # Here we assign the IP address and port number. They should be as same as them of server side (in MATLAB)

    # Since the client and server will all be in the same machine, the local IP address is 127.0.0.1, and port number
    # is a random port that is set by me.

    try:
        # create an AF_INET, STREAM socket (TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # sock is a virtual object. we use socket to start a network communication. To establish a socket object, the
        # IP address, port number and protocol type should be determined.

    except:
        print('Failed to create a socket. ')
        sys.exit()
    print('Socket Created :)')

    sock.connect(sever_port)
    print("start a client")
    time.sleep(0.01)

    # If everything is going correctly, here we should have already establish the client successfully

    # Since in the TCP protocol, the client must first send a message to server, we will send a "start" string message
    # to the server. Then Server can send back messages after receiving client's message. Let's do it in the following.

    s = "start"
    s = bytes(s,encoding='utf8')
    sock.send(s)
    print(s)

    # Here we run a loop to receive and send messages to the server. It will keep running until you stop the program.
    count = 0

    while count<120:

        buf = sock.recv(1000)
        # receive the maximum of 1k bytes at one time

        # save the data in a buffer

        print('#############################')
        print(buf)
        # print the data on the screen

        buf_l = json.loads(buf)
        print(buf_l)
        # use json to decoding the data and print on the screen

        control_signal1 = buf_l[0] * 0.4
        control_signal2 = control_signal1*2
        control_signal3 = control_signal1*4
        # to demo, we give 3 different magnification to the received data

        control_signal = np.array([control_signal1, control_signal2, control_signal3], float)
        # we send back the 3 different magnified data. To send multiple data in one time, a matrix should be created.

        s = str(control_signal)
        # transform data into string format

        s_1 = bytes(s,encoding='utf8')
        # using utf8 to encoding data

        sock.send(s_1)
        # send the encoded data to the server

        print(s)
        print(s_1)
        # show the results on the screen
        count = count + 1
        print(count)

    sock.close()
    # close the socket object after the communication is finished


if __name__ == '__main__':
    tcp_sim()