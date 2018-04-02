"""
Construct a socket server.

Construct a socket server that will accumulate a message from some client and
return that exact message back to the client.

When the server first starts, a message should be printed to the console of the
format "--- Starting server on port 8888 at 12:43:08 29/01/2018 ---".  When the
server is stopped, the user shouldn't see any error message.  When the server
is stopped, a message should be printed to the console of the format
"--- Stopping server on port 8888 at 12:43:39 29/01/2018 ---".  Whenever a
message is received by the server, the server prints to the console a log of
that message. It doesn't have to match this exactly, but it should be something
like: [12:43:10 29/01/2018] Echoed: 'Hello, world!'
"""

from datetime.datetime import now


SERVER_START = '--- Starting server on port {port} at {date} ---'
SERVER_ECHO = '[{date}] Echoed: {msg}'
SERVER_END = '--- Stopping server on port {port} at {date} ---'


def main():
    print(SERVER_START.format(port=8888, date=now()))
    try:
        pass
    finally:
        print(SERVER_END.format(port=8888, date=now()))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
