# 03_networking/blocking/tcp_server.py

import socket


def main():
    host = "127.0.0.1"  # this is a local host ip address
    port = 5003

    # create a new socket
    s = socket.socket()

    # create a tuple for host and port
    #   to say that no other one can use this port
    network_host = (host, port)

    # tell socket to use host and port
    #   reserves the port
    s.bind(network_host)

    # client vs server. client sends request. server listens

    # start listening for requests
    s.listen()

    # accept incoming connctions
    conn, addr = s.accept()  # start waiting right here
    print(f"Accepted conncetion from {addr}")

    # We're a server. We never stop listening :D
    # We're also not providing a graceful way to exit :\

    # until we receive data
    while True:
        # receive BINARY data
        # it'll stop and wait right here!
        data = conn.recv(1024)
        if not data:
            break

        # this is an echo server. receives data and sends it right back
        # convert BINARY data into a string
        data = data.decode()
        print(f"From connection: {data}")
        data = data.upper()
        # return data to client
        print(f"Sending back to client: {data} ")
        # change it back into binary
        conn.send(data.encode())
    conn.close()  # closes connection


if __name__ == "__main__":
    main()
