# 3_networking/nonblocking/async_chat_server.py
import asyncio
from typing import List

ENCODING = "utf8"


class ChatServerProtocol(asyncio.Protocol):

    def __init__(self, transports: List[asyncio.BaseTransport]):
        super().__init__()
        self._transports = transports
        self._transport: asyncio.BaseTransport = None

    # Called when we accept a new connection
    def connection_made(self, transport: asyncio.BaseTransport):
        peername = transport.get_extra_info('peername')
        print(f'Connection from {peername}')
        self._transport = transport
        self._transports.append(transport)

    # Called when new data is incoming
    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        print('Data received: {message}')

        self.broadcast_message(message)

    def broadcast_message(self, message: str):
        for transport in self._transports:
            # broadcasts the message to everyone except ourselves
            if transport != self._transport:
                transport.write(message.encode(ENCODING))

    #  Called when a connection is closed or there is an error
    #  this will call who we lost connection to
    def connection_lost(self, exc: Exception):
        self._transports.remove(self._transport)
        peername = self._transport.get_extra_info('peername')
        print(f'Lost connection from {peername}.')
        return super().connection_lost(exc)


async def main():
    # Get a reference to the event loop since we are using
    # low-level APIs
    loop = asyncio.get_running_loop()
    host = '127.0.0.1'
    port = 5001

    transports: List[asyncio.BaseTransport] = []
    server = await loop.create_server(
        lambda: ChatServerProtocol(transports),
        host,
        port
    )

    async with server:
        # Start accepting connections until the coroutine is cancelled.
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
