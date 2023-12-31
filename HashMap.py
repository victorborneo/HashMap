from typing import Callable
from typing import Any
from typing import Generator
from typing import Tuple


Key = Any
Value = Any


class HashMap:
    def __init__(self, func: Callable=None, size: int=2**16):
        self._len = 0
        self._size = size
        self._hash_func = hash if func is None else func
        self._map = [[] for _ in range(size)]

    def __str__(self):
        string = []

        for arr in self._map:
            for key, val in arr:
                string.append(f"{key}: {val}")

        if not string:
            return "EmptyHashMap"

        return "\n".join(string)

    def __len__(self):
        return self._len

    def _get_idx(self, map_key: Any) -> None:
        return self._hash_func(map_key) % self._size

    def get(self, map_key: Any, not_found_value=None) -> Value:
        idx = self._get_idx(map_key)
        for key, value in self._map[idx]:
            if map_key == key:
                return value
        return not_found_value

    def remove(self, map_key: Any) -> None:
        idx = self._get_idx(map_key)
        for c, (key, _) in enumerate(self._map[idx]):
            if map_key == key:
                self._len -= 1
                self._map[idx].pop(c)
                return
        raise KeyError("Key not found in HashMap")

    def add(self, map_key: Any, map_value: Any) -> None:
        idx = self._get_idx(map_key)
        for c, (key, _) in enumerate(self._map[idx]):
            if map_key == key:
                self._map[idx][c] = (map_key, map_value)
                return

        self._len += 1
        self._map[idx].append((map_key, map_value))
        if self._len >= self._size:
            self._map.extend([[] for _ in range(self._size)])
            self._size *= 2

    def keys(self) -> Generator[Key, None, None]:
        for arr in self._map:
            for tup in arr:
                yield tup[0]

    def values(self) -> Generator[Value, None, None]:
        for arr in self._map:
            for tup in arr:
                yield tup[1]

    def items(self) -> Generator[Tuple[Key, Value], None, None]:
        for arr in self._map:
            for tup in arr:
                yield tup
