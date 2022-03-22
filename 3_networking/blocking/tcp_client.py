# 03_networking/blocking/tcp_client.py

import socket


def main():
    host = "172.16.12.226"
    port = 5005

    s = socket.socket()
    network_host = (host, port)

    # connect to server
    s.connect(network_host)

    # get input from user
    message = input(">>>")
    # while we do not want to quit:
    while message not in ['q', 'quit']:
        try:
            if len(message) > 0:
                # send message to server
                s.send(message.encode())

                # listen for echo response
                data = s.recv(1024)
                print(f"Received from server: {data.decode()}")
                message = input(">>>")

        except IOError as err:
            print(f"Server closed connection: {err}")
            break
    s.close()


if __name__ == "__main__":
    main()
