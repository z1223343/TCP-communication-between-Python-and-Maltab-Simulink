import socket
import json
import struct
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connection...')
sock, addr = s.accept()
sock.send(b'welcomewwwwwwwwww')
count = 0

while count<120:
    buf = sock.recv(1000)
    buf_1 = buf
    buf_2 = struct.unpack('dddd', buf_1[0:32])
    state1 = buf_2[0]
    state2 = buf_2[1]
    state3 = buf_2[0]*2
    state4 = buf_2[1]*2
    print(buf_2)

    control_signal1 = state1
    control_signal2 = state2
    control_signal3 = state3
    control_signal4 = state4

    control_signal = np.array([control_signal1, control_signal2, control_signal3, control_signal4], float)
    s = str(control_signal)
    s_l = bytes(s, encoding='utf8')
    sock.send(s_l)
    print(s)

    count = count + 1
    print(count)

sock.close()