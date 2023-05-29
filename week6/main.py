from rule import Rule
from message import Message
from senderrule import SenderRule
from anyrule import AnyRule
from savecommand import SaveCommand
from discardcommand import DiscardCommand
from printcommand import PrintCommand

# ここでルールを組み立てる．
rule = SenderRule(SaveCommand(),"alice")
rule2 = SenderRule(DiscardCommand(),"bob")
rule3 = AnyRule(PrintCommand())
rule.set_next(rule2).set_next(rule3)

msgs = [
    Message("alice", "me", "Hello, this is Alice."),
    Message("bob", "me", "Hello from Bob."),
    Message("charlie", "me", "Hi, it's Charlie.")
]

for m in msgs:
    rule.handle(m)