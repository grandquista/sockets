"""
Construct a socket client.

Construct a socket client that will accept a message from the command line and
send it to a server.

You may need to review the docs for accepting command line arguments when
running a script.  When the server sends a response back, the client should
accumulate the response and print it to the console.
"""

from socket import getaddrinfo, socket, SOCK_STREAM
from sys import argv

BUFFER_SIZE = 1024


def main():
    info = getaddrinfo('127.0.0.1', 8080)
    info = [i for i in info if i[1] == SOCK_STREAM][0]
    with socket(*info[:3]) as client:
        client.connect(info[-1])
        if len(argv) > 1:
            for msg in argv[1:]:
                client.sendall(msg.encode('utf8'))
                size = BUFFER_SIZE
                while size == BUFFER_SIZE:
                    buffer = client.recv(BUFFER_SIZE)
                    print(buffer.decode('utf8'))
                    size = len(buffer)
            return
        while True:
            input(': ')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
