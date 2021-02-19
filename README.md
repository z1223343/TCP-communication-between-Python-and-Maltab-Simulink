[image1]: ./roadrunner_carla.png

# TCP communication bewteen Python and Matlab&Simulink
**This repository is to give an example and instruction for TCP communication between Python and Matlab&Simulink. UDP will be similar.**

## When to apply this

In some projects, we may want to make co-simulation or data exchange between a Python tool and Simulink/Maltab model. TCP can be a efficient and reliable way to achieve linkage between Python and Maltab&Simulink.

Take one example: Our team developed a vehicle driving simulator called RoadRunner for eco-driving study of connected and automated vehicles (CAVs), and which will be linked to Carla, an open-source 3D visual simulator for autonomous driving research. Using this TCP communication repo, one or multiple vehicles in Carla environment can be controled by eco-driving controller in the RoadRunner's Simulink model.


![RoadRunner_and_Carla][image1]

Since the communication accuracy is critical in my case introduced above, TCP communication structure is demonstrated here in this example. But UDP will also work if you want.

This repo's solutions allow users sending several variables in both communication direction (Matlab -> Python, Python -> Matlab).

## Solutions:

Obviously, there are two solutions for the communication:
  * Set TCP server in Maltab, and set TCP client in Python. (folder 1)
    Notice: In this case, MathWorks `Instrument Control Toolbox` is needed.
    Pros: Since there can be multiple clients with one server, you can control multiple Python agents with one Matlab/Simulink model.
  * Set TCP client in Matlab, and set TCP server in Python. (folder 2)
    Pros: You don't need additional toolbox.
    
Looks like Python socket can only send data as binary format, while Matlab tcp function can send data directly as string format.


## This Repo Includes:

1. This README.md
2. Solution 1 (Maltab Server Python Client)
3. Solution 2 (Maltab Client Python Server)

In each solution (take folder 1 as an example):
1. `tcp_client.py`:  work as one client
2. `tcp_server.m`:   work as server of this TCP communication system
3. `tcp_server.slx`: this simulink will be controlled by the Matlab code above
4. `result.jpg`:     show the expected result during this TCP communication

The codes are well commented to explain every steps. 

## Instruction to Run:

1. Make sure you have `python3` and `MATLAB / Simulink` installed 
2. To start the communication system, first run server side, and then run the client side.
3. If everything goes well, you will get something like `result.jpg`.

## Reference Materials:

1. Python officical document.
2. Matlab tcpip() function document.

