import asyncio
import json
from typing import List

from textual.app import App
import textual.events as events
from textual.layouts.grid import GridLayout
from textual.widgets import ScrollView

# To type things in
from textual_inputs import TextInput

from net import (
    AbstractChatClientProtocol,
    AbstractMessageHandler,
    ChatClientProtocol,
    TestProtocol
)

USERNAME = "username"
MESSAGE = "message"


class ChatApp(App, AbstractMessageHandler):
    _protocol: AbstractChatClientProtocol | None = None
    _username: str | None = None

    def __init__(self, protocol: AbstractChatClientProtocol | None = None) -> None:
        if protocol is None:
            raise ValueError("Cannot continue without a chat protocol")
        self._protocol = protocol
        self._protocol.message_handler = self
    
    async def onLoad(self, event: events.Load) -> None:
        await self._protocol.connect()
        # this is a function defined in App. will listen to these key bindings and quit the event 
        await self.bind("escape", "quit", "Quit")
    async def onMount(self, event: events.Mount) -> None:
        grid: GridLayout = await self.view.dock_grid()

        grid.add_column(name="center", fraction=1)
        grid.add_row(name="top", fraction=1)
        # the text box is always going to be 3 lines so that the text view can resize however it wants as the window size changes
        grid.add_row(name="bottom", size=3)

        # puts things into those areas
        grid.add_areas(chat="center,top", message_input="center,bottom")

        self._chat_scrollview = ScrollView("", name="chat_view")
        self._message_input = TextInput(name="message_input", title="Message", placeholder="Type message here")
        grid.place(chat=self._chat_scrollview, message_input=self._message_input)

        await self._message_input.focus()

    async def onKey(self, event: events.Key) -> None:
        if event.key == "enter":
            value = self._message_input.value
            self._message_input_value = "" # empty the message input
            value = value.strip() # get rid of tab and space
            if len(value) == 0:
                return
            if self._protocol is None:
                return
            data = {USERNAME: self._username, MESSAGE: value}
            package = json.dumps(data)
            await self._protocol.send(package)

    # Tells our protocol that we're exiting
    async def onShutdownRequest(self, event: events.ShutdownRequest):
        await self._protocol.close()
        return await super().onShutdownRequest(event)

    async def onMessageReceived(self, message: str) -> None:
        message = json.loads(message)
        await self.add_message(message)

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


def runClient(host: str = "127.0.0.1", port: int = 5001, *, test: bool = False, protocolType: str = "basic") -> None:
    async def _runClient(host, port):
        protocol: AbstractChatClientProtocol = None
        protocol = TestProtocol() if test else ChatClientProtocol(host, port)
        app = ChatApp(protocol=protocol)
        # starts looking at the queue awaiting for message to come in
        await app.process_messages()

    asyncio.run(_runClient(host, port))
