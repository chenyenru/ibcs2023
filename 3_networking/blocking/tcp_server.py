# networking/blocking/tcp_server.py

import socket


def main():
    host = "127.0.0.1"  # this is a local host ip address
    port = 5000

    # create a new socket
    s = socket.socket()

    # create a tuple for host and port
    network_host = (host, port)

    # tell socket to use host and port
    s.bind(network_host)


if __name__ == "__main__":
    main()
