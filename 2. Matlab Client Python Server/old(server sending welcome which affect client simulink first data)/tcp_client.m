% matlab works as client, while Python works as server

open_system('tcp_client');
% start simulation and pause simulation, waiting for signal from python
set_param(gcs,'SimulationCommand','start','SimulationCommand','pause');

% open a client
t = tcpclient('127.0.0.1',9999);
all_data = [];
count = 0;
while count<120 % just run for 120 steps for demo
    while(1) % loop, until getting some data
        nBytes = get(t,'BytesAvailable');
        if nBytes > 0
            break;
        end
    end
    command_rev = read(t,nBytes); % read() will read binary as str
    data = str2num(char(command_rev)); % transform str into numerical matrix
    all_data = [all_data;data]; % store history data
    if isempty(data)
        data = [0,0,0,0];
    end
    data1 = data(1);
    data2 = data(2);
    data3 = data(3);
    data4 = data(4); % separate each data in the matrix
    
    % set parameter in the simulink model using the data from python
    set_param('tcp_client/K1','Gain',num2str(data1));
    set_param('tcp_client/K2','Gain',num2str(data2));
    set_param('tcp_client/K3','Gain',num2str(data3));
    set_param('tcp_client/K4','Gain',num2str(data4));
    % run the simulink model for one step
    set_param(gcs, 'SimulationCommand','step');
    
    u1 = out.states.data(end,:);
    u2 = out.states1.data(end,:);
    u3 = out.states2.data(end,:);
    u4 = out.states3.data(end,:);
    v = [u1,u2,u3,u4];
    write(t,v);
    
    count = count + 1
end
set_param('tcp_client/K1','Gain',num2str(0));
set_param('tcp_client/K2','Gain',num2str(0));
set_param('tcp_client/K3','Gain',num2str(0));
set_param('tcp_client/K4','Gain',num2str(0));
set_param(gcs,'SimulationCommand','stop');
    