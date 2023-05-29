# ファイル discardcommand.py
from command import Command
from message import Message


class PrintCommand(Command):
    def run(self, msg: Message) -> None:
        print("From: " + msg.sender + ", To: " + msg.recipient + ", Body: " + msg.body)