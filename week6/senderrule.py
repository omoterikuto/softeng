from rule import Rule
from command import Command
from message import Message


class SenderRule(Rule):
    _senderName: str
    def __init__(self, command: Command, name: str) -> None:
        self._senderName = name
        super().__init__(command)

    def check(self, msg: Message) -> bool:
        return msg.sender == self._senderName