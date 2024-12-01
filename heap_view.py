from guppy import hpy
from guppy.etc import Glue
from typing import Any, ClassVar


class HeapView:
    hp: ClassVar[Any] = hpy()

    @classmethod
    def get_heap_view(cls) -> str:
        result: str = ""
        h = cls.hp.heap()
        result = str(h.bytype)
        result += "\n"
        result += str(h[0].byrcs)
        del h
        cls.hp.setrelheap()
        return result


if __name__ == "__main__":
    HeapView.hp.setrelheap()
    print(HeapView.get_heap_view())
