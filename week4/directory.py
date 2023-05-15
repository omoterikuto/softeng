# ファイル directory.py
from typing import List
from entry import Entry
from observer import Observer

class Directory(Entry):
  _children: List[Entry]
  _observer: List[Observer]
  
  def __init__(self, name: str) -> None:
    super().__init__(name)
    self._children = []
    self._observer = []

  def get_children(self) -> List[Entry]:
    return self._children
  
  def add(self, e: Entry) -> None:
    self._children.append(e)
    self.notify_observers(self)

  def add_observer(self, o: Observer) -> None:
    self._observer.append(o)

  def notify_observers(self,e: Entry) -> None:
    for o in self._observer:
      o.update(e)