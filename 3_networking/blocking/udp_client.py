# 03_networking/blocking/udp_client.py
import socket


def main():
    host = "172.16.13.147"
    print(host)
    port = 5006

    s = socket.socket(type=socket.SOCK_DGRAM)
    network_host = (host, port)

    # doing a DNS lookup
    data = socket.gethostbyname_ex("brentmparker.com")
    print(data)
    server_host = data[2][0]
    server = (server_host, 9001)
    s.bind(network_host)

    message = input(">>>")
    while message not in ["q", "quit"]:
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print(f"Received from server ({addr}): {data}")
        message = input(">>>")
    s.close()


if __name__ == "__main__":
    main()
