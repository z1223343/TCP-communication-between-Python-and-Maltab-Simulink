[image1]: ./roadrunner_carla.png

# TCP communication bewteen Python and Matlab/Simulink
**This repository is to give an example and instruction for TCP communication between Python and Matlab&Simulink**

## Why Did I Do This

In one of my project, there is a communication system between python script and Simulink model. 

In detail, our team developed a multi-vehicle control simulator called RoadRunner for eco-driving study of connected and automated vehicles (CAVs), and I linked it to Carla, an open-source 3D visual simulator for autonomous driving research. In the end, one or multiple vehicles in Carla environment can be controled by eco-driving controller in RoadRunner's Simulink model.


![RoadRunner_and_Carla][image1]

Since the communication accuracy is critical in my case introduced above, TCP communication structure is demonstrated here in this example. But UDP will also work if you want.


## Solutions:

Obviously, there are two solutions for the communication:
  * Set TCP server in Maltab, and set TCP client in Python.
    Notice: In this case, MathWorks `Instrument Control Toolbox` is needed.
    Pros: Since there can be multiple clients with one server, you can control multiple Python agents with one Matlab/Simulink model.
  * Set TCP client in Matlab, and set TCP server in Python.
    Pros: You don't need additional toolbox.
    
I have built the communication in both ways successfully. Here in this example, only first solution is shown. I may provide the code for the second solution in the future.


## This Repo Includes:

1. This README.md
2. `tcp_client.py`:  work as one client
3. `tcp_server.m`:   work as server of this TCP communication system
4. `tcp_server.slx`: this simulink will be controlled by the Matlab code above
5. `result.jpg`:     show the expected result during this TCP communication

The codes are well commented to explain every steps. 

## Instruction to Run:

1. Make sure you have `python3` and `MATLAB / Simulink` installed 
2. To start the communication system, first run the MATLAB codes, and then run the python client.
3. If everything goes well, you will get something like `result.jpg`.

## Reference Materials:

1. Python officical document.
2. Matlab tcpip() function document.

