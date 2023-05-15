# ファイル indentbserver.py
from observer import Observer
from entry import Entry

class IndentObserver(Observer[Entry]):
  def print_entries(self, e: Entry, depth: int):
    for i in range(depth):
      print("  ",end='')
    print(e.get_name())
    if len(e.get_children()) == 0:
      return
    for e in e.get_children():
      self.print_entries(e, depth+1)

  
  def update(self, e: Entry) -> None:
    self.print_entries(e, 0)