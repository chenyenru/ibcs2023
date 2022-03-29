# 3_networking/nonblocking/tcp_selector_server.py

import socket
import threading
import selectors
from multiprocessing.pool import ThreadPool

TIMEOUT = 60
MAX_CONNECTIONS = 10
pool = ThreadPool(5)

def main():
    host = "127.0.0.1"
    port = 5006
    network_host = (host, port)

    s = socket.socket()
    s.bind(network_host)
    s.listen(MAX_CONNECTIONS)

    # Create a selector. This is the object that listens
    # for new events
    selector = selectors.DefaultSelector()

    # Register some object that can create events
    #   Parameters:
    #       the object that originates the event
    #       the type of event to listen for
    #       the function/method to call when that event is detected
    selector.register(s, selectors.EVENT_READ, accept)

    print("Server has started......")

    # Create a loop that handles events
    while True:
        for key, mask in selector.select(): # this will ask the selector if there's new events since last time
            # key.data = function to call on event
            # key.fileobj = object that created event
            handler = key.data
            handler(selector, key.fileobj)


def accept(selector: selectors.DefaultSelector, s: socket.socket):
    conn, addr = s.accept()
    conn.setblocking(False) # "don't block on this connection"
    conn.settimeout(TIMEOUT)
    print("Server has started......")

    selector.register(conn, selectors.EVENT_READ, start_thread)

def start_thread(selector, conn):
    print("Creating new thread...")
    pool.apply_async(read_from_socket, (selector, conn))
    # pool.map(read_from_socket, (selector, conn))
    # thread = threading.Thread(target=read_from_socket, args=(selector, conn))
    # thread.start()

def read_from_socket(selector, conn):
    try:
        data = conn.recv(1024)
        if not data:
            unregister(selector, conn)
        data = data.decode()
        print(f"Received: {data}")
        data = data.upper()
        conn.send(data.encode("utf-8"))
    # when it doesn't receive the data after some time
    except socket.timeout as err:
        print(f"Socket timed out")
        print(err)
        unregister(selector, conn)
    # IOError is catching the connection close
    except IOError as err:
        print(f"IOError from socket")
        print(err)
        unregister(selector, conn)

def unregister(selector, fileobj):
    try:
        selector.unregister(fileobj)
    except KeyError:
        pass
    except ValueError:
        pass
    finally:
        fileobj.close()

if __name__ == "__main__":
    main()