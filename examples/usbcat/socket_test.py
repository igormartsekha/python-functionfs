import socket

def run_aa_socket_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.107', 5277))
    s.sendall(bytearray([0, 3, 0, 6, 0, 1, 0, 1, 0, 2]))
    data = s.recv(12)
    print(data)
    s.close()

if __name__ == '__main__':
    run_aa_socket_connection()