# 3_networking/nonblocking/async_chat_client.py
import asyncio

ENCODING = "utf8"


class ChatClientProtocol(asyncio.Protocol):

    def __init__(self, on_conn_lost, loop):

        # We need the loop later so we can execute some
        # extra code on the loop
        self._loop = loop

        # Future that we will use to inform main that we have quitted
        self.on_conn_lost = on_conn_lost
        self.is_connnected = False
        self._transport = None

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

    def send(self, data: str):
        if data:
            message = data.encode(ENCODING)
            self._transport.write(message)

    async def get_message(self, loop: asyncio.BaseEventLoop):
        while self.is_connected:
            message = await loop.run_in_executor(None, input, '>>>')
            message = message.strip()
            if message == 'q':
                self.is_connected = False
                self._transport.close()
            else:
                self.send(message)


async def main():
    # Get a reference to the event loop since we are using
    # low-level APIs
    loop = asyncio.get_running_loop()
    host = '127.0.0.1'
    port = 5001

    # Create a future to listen to later so we can
    # detect the closing of the client
    on_conn_lost = loop.create_future

    # Create an instance of the EchoClientProtocol
    echo_client_protocol = ChatClientProtocol(on_conn_lost, loop)

    # Create connection
    transport, protocol = await loop.create_connection(
        lambda: echo_client_protocol,
        host,
        port
    )

    # Start event loop that listens for input messages
    # check other coroutines and see if each of them have something to do
    await echo_client_protocol.get_message(loop)

    # handle cleanup when client closes
    try:
        await on_conn_lost
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())
