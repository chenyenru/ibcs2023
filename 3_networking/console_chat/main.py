import argparse
from ast import arguments
from os import chdir, curdir, path
import sys

from net.server_protocol import run_server
from chat_client import runClient


def main(args: argparse.Namespace):
    # main.py to start client
    # main.py -s to start server
    host = args.host if args.host else "127.0.0.1"
    port = args.post if args.port else 5001
    test = args.test

    if args.server:
        print("Starting server:")
        run_server(host, port)
        return

    runClient(host=host, port=port, test=test)


if __name__ == "__main__":
    # chdir(): changes directory
    # path.dirname: gives me the directory name that contains a file
    # path.abspath(__file__): gives me the absolute path of this file
    chdir(path.dirname(path.abspath(__file__)))

    # set up command line arguments
    # python main.py -s to start server
    # python main.py -t to start client in testing mode

    parser = argparse.ArgumentParser()
    parser.add_argument("--server", "-s", default=False,
                        action="store_true",
                        help="Start chat server")
    parser.add_argument("--host", type=str,
                        help="Specify hostname for client/server")
    parser.add_argument("--port", "-p", type=int,
                        help="Specify port for client/server")
    parser.add_argument("--test", "-t", default=False,
                        action="store_true", help="Start chat client in testing mode")

    # this parse things after main.py
    # because the first element is main.py
    arguments = parser.parse_args(sys.argv[1:])
    main(args=arguments)
