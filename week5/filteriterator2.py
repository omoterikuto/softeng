from typing import  Iterator
from state import State
from afterspace import AfterSpace
from state import Context

class FilterIterator2(Iterator[str], Context):
    _original: Iterator[str]
    _state: State

    def __init__(self, original: Iterator[str]) -> None:
        super().__init__()
        self._original = original
        self._state = AfterSpace.get_instance()
    
    def set_state(self, new_state: State):
        self._state = new_state

    def __next__(self) -> str:
        ch = next(self._original)
        return self._state.process_char(self, ch)

if __name__ == "__main__":
    for ch in FilterIterator2(iter("The quick brown fox jumps over a lazy dull dog.\n")):
        print(ch, end="")
