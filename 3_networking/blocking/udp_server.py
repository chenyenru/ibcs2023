# 03_networking/blocking/udp_server.py
import socket


def main():
    host = "211.22.29.241"
    port = 5005
    # remember that in UDP, a packet is called data gram (aka dgram)
    s = socket.socket(type=socket.SOCK_DGRAM)
    network_host = (host, port)
    s.bind(network_host)
    print("Server started...")

    # because this is UDP, there's no handshake part

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print(f"Received from {addr}: {data}")

        # and we may not need to return it. the process is done once we received the data
        data = data.upper()
        print(f"Sending to {addr}: {data}")
        s.sendto(data.encode(), addr)
    s.close()


if __name__ == "__main__":
    main()
