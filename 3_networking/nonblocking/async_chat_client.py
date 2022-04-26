# 3_networking/nonblocking/async_chat_client.py
import asyncio
import json

ENCODING = "utf8"
USERNAME = "username"
MESSAGE = "message"


class ChatClientProtocol(asyncio.Protocol):
    """
    Handles the connection
    """

    def __init__(self, on_conn_lost):
        self.username = None

        # We need the loop later so we can execute some
        # extra code on the loop
        self.loop = asyncio.get_running_loop()

        # Future that we will use to inform main that we have quitted
        self.on_conn_lost = on_conn_lost
        self.is_connnected = False
        self._transport = None
        self.on_data_received: callable = None

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        self._transport = transport
        self.is_connected = True
        peername = transport.get_extra_info('peername')
        print(f'Connected to {peername}')

    def connection_lost(self, exc: Exception) -> None:
        self.is_connected = False
        print("Connection has been closed")
        self.on_conn_lost.set_result(True)
        super().connection_lost(exc)

    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        print(f'Message received: {message}')
        if self.on_data_received:
            self.on_data_received(message)

    def send(self, data: str):
        if data:
            message = data.encode(ENCODING)
            self._transport.write(message)

    def close(self):
        self._transport.close()
        self.is_connected = False


class ChatApp():
    def __init__(self) -> None:
        self._username = None

        # Create a future to listen to later so we can
        # detect the closing of the client
        self.loop = asyncio.get_running_loop()
        self.on_conn_lost = self.loop.create_future()

        # Create an instance of the EchoClientProtocol
        self.echo_client_protocol = ChatClientProtocol(
            self.on_conn_lost)

        self.echo_client_protocol.on_data_received = self.on_data_received

    @ property
    def username(self) -> str:
        return self._username

    @ username.setter
    def username(self, username: str) -> str:
        self._username = username

    async def get_message(self, loop: asyncio.BaseEventLoop):
        while self.echo_client_protocol.is_connected:
            message = await loop.run_in_executor(None, input, '>>>')
            message = message.strip()
            if message == 'q':
                self.echo_client_protocol.is_connected = False
                self.echo_client_protocol.close()
            else:
                json_packet = {
                    USERNAME: self.username,
                    MESSAGE: message
                }
                # turn json packet into string with json.dumps()
                package = json.dumps(json_packet)
                self.echo_client_protocol.send(package)

    def on_data_received(self, message):
        data = json.loads(message)
        uname: str = data.get(USERNAME)
        msg: str = data.get(MESSAGE)
        uname = f'[{uname}]'.ljust(15)
        print(f'{uname}: {msg}')

    async def prompt_username(self):
        self.username = input("Type in a username: ")

    async def run(self, host: str, port: int):

        await self.prompt_username()
        # Create connection
        transport, protocol = await self.loop.create_connection(
            lambda: self.echo_client_protocol,
            host,
            port
        )

        # Start event loop that listens for input messages
        # check other coroutines and see if each of them have something to do
        await self.get_message(self.loop)

        # handle cleanup when client closes
        try:
            await self.on_conn_lost
        finally:
            transport.close()


async def main():
    # Get a reference to the event loop since we are using
    # low-level APIs
    host = '127.0.0.1'
    port = 5001

    app = ChatApp()
    await app.run(host, port)

if __name__ == "__main__":
    asyncio.run(main())
