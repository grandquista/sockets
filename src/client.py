"""
Construct a socket client.

Construct a socket client that will accept a message from the command line and
send it to a server.

You may need to review the docs for accepting command line arguments when
running a script.  When the server sends a response back, the client should
accumulate the response and print it to the console.
"""

from select import select
from socket import getaddrinfo, socket, SOCK_STREAM
from sys import argv
from time import sleep

ADDR = ('127.0.0.1', 8080)

BUFFER_SIZE = 8


def run_echo(client):
    if len(argv) > 1:
        for msg in argv[1:]:
            writers = []
            while not writers:
                try:
                    writers = select([], [client], [], 10)
                except OSError:
                    return
            client.sendall(msg.encode('utf8'))
            # sleep(10)
            readers = select([client], [], [], 10)
            msg = b''
            while True:
                readers = []
                while not readers:
                    try:
                        readers = select([client], [], [], 10)
                    except OSError:
                        break
                if not readers:
                    break
                try:
                    buffer = client.recv(BUFFER_SIZE)
                except OSError:
                    break
                msg += buffer
                if len(buffer) < BUFFER_SIZE:
                    break
            print(msg.decode('utf8'))
        return
    while True:
        input(': ')


def main():
    info = getaddrinfo(*ADDR)
    info = [i for i in info if i[1] == SOCK_STREAM][0]
    with socket(*info[:3]) as client:
        # client.settimeout(10)
        client.connect(info[-1])
        run_echo(client)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
