import asyncio
import json
from net import (
    AbstractChatClientProtocol,
    AbstractMessageHandler,
    ChatClientProtocol,
    TestProtocol
)

USERNAME = "username"
MESSAGE = "message"


class ChatApp(AbstractMessageHandler):
    _protocol: AbstractChatClientProtocol | None = None
    _username: str | None = None

    def __init__(self, protocol: AbstractChatClientProtocol | None = None) -> None:
        if protocol is None:
            raise ValueError("Cannot continue without a chat protocol")
        self._protocol = protocol
        self._protocol.message_handler = self

    async def onMessageReceived(self, message: str) -> None:
        message = json.loads(message)
        uname: str = message.get(USERNAME)
        msg: str = message.get(MESSAGE)
        uname = f"[{uname}]".ljust(15)
        print(f"{uname}:{msg}")

    async def getMessage(self):
        loop = asyncio.get_event_loop()
        while self._protocol.isConnected:
            message = None
            message = await loop.run_in_executor(None, input, ">>>")
            message = message.strip()
            if message == "q":
                await self._protocol.close()
            else:
                data = {USERNAME: self._username, MESSAGE: message}
                package = json.dumps(data)
                await self._protocol.send(package)

    async def promptUsername(self):
        valid = False
        while not valid:
            self._username = input("Type in a username: ").strip()
            valid = len(self._username) > 0 and len(self._username) <= 13

    async def run(self):
        await self.promptUsername()
        await self._protocol.connect()

        try:
            await self.getMessage()
        except Exception as e:
            print(e)
        finally:
            if self._protocol.isConnected:
                await self._protocol.close()


def runClient(host: str = "127.0.0.1", port: int = 5001, *, test: bool = False, protocolType: str = "basic") -> None:
    async def _runClient(host, port):
        protocol: AbstractChatClientProtocol = None
        if test:
            protocol = TestProtocol()
        else:
            protocol = ChatClientProtocol(host, port)
        app = ChatApp(protocol=protocol)
        await app.run()

    asyncio.run(_runClient(host, port))
