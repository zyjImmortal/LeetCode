
from socket import socket, AF_INET, SOCK_STREAM

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 20000))
    s.send(b'hello')

if __name__ == '__main__':
    main()