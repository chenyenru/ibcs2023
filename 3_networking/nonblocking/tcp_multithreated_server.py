# 3_networking/nonblocking/tcp_multithreated_server.py
import socket
import threading


def main():
    host = "127.0.0.1"
    port = 5006
    # this is a TCP socket
    s = socket.socket()
    network_host = (host, port)
    s.bind(network_host)
    # can only listen to 10 incoming messages at the same time
    s.listen(10)

    while True:
        conn, addr = s.accept()
        # If there is no response in 5 seconds, close conncetion
        conn.settimeout(5)
        print(f"Conncetion from {addr}")
        # Create a new thread
        #   target = function/method that will be called when the thread starts
        #   args = arguments to pass the target function

        thread = threading.Thread(target=listen_to_client, args=(conn, addr))
        thread.start()


def listen_to_client(conn: socket.socket, addr: socket._RetAddress):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            prompt = (f"Received from {addr}: ").ljust(40)
            print(f"{prompt}: {data}")
            data = data.upper()
            conn.send(data.encode())
        # when it doesn't receive the data after some time
        except socket.timeout as err:
            print(f"Socket from {addr} timed out")
            print(err)
            break
        # IOError is catching the connection close
        except IOError as err:
            print(f"IOError from socket at {addr}")
            print(err)
            break
    conn.close()


if __name__ == "__main__":
    main()
