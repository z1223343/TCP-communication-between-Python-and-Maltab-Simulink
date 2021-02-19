clc;
clear;
close all;
open_system('tcp_server')

sim_time_step = 0.01;

% start the simulation and pause the simulation, waiting for singal from python
set_param(gcs,'SimulationCommand','start','SimulationCommand','pause');

% open a server, it will block until a client connect to it
s = tcpip('127.0.0.1', 54320,  'NetworkRole', 'server');
fopen(s);

all_data = [];
count=0;
% main loop
while count<120 % just run for 120 steps for demo   
    while(1) %loop, until read some data
        nBytes = get(s,'BytesAvailable');
        if nBytes>0
            break;
        end
    end
    command = fread(s,nBytes); % fread() will read binary as str
    
    data=str2num(char(command')); % tranform str into numerical matrix
    
    all_data = [all_data;data]; % store history data
    if isempty(data)
        data=[0,0,0];
    end
    data1 = data(1); 
    data2 = data(2); 
    data3 = data(3); % separate each data in the matrix
    
    % set a paramter in the simulink model using the data get from python
    set_param('tcp_server/K1','Gain',num2str(data1))
    set_param('tcp_server/K2','Gain',num2str(data2))
    set_param('tcp_server/K3','Gain',num2str(data3))
    % run the simulink model for one step
    set_param(gcs, 'SimulationCommand', 'step');  
    
    u=states.data(end,:); % read the last data in the result array 
    fwrite(s, jsonencode(u)); % encode data using json
    count=count+1;
end
fclose(s);
set_param(gcs,'SimulationCommand','stop');