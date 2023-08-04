from typing import Callable
from typing import Any
from typing import Generator
from typing import Tuple


Key = Any
Value = Any


class HashMap:
    def __init__(self, func: Callable=None, size: int=2**16):
        self.__len = 0
        self.__size = size
        self.__hash_func = hash if func is None else func
        self.__map = [[] for _ in range(size)]

    def __str__(self):
        string = []

        for arr in self.__map:
            for key, val in arr:
                string.append(f"{key}: {val}")

        if not string:
            return "EmptyHashMap"

        return "\n".join(string)

    def __len__(self):
        return self.__len

    def __get_idx__(self, map_key: Any) -> None:
        return self.__hash_func(map_key) % self.__size

    def get(self, map_key: Any, not_found_value=None) -> Value:
        idx = self.__get_idx__(map_key)
        for key, value in self.__map[idx]:
            if map_key == key:
                return value
        return not_found_value

    def remove(self, map_key: Any) -> None:
        idx = self.__get_idx__(map_key)
        for c, (key, _) in enumerate(self.__map[idx]):
            if map_key == key:
                self.__len -= 1
                self.__map[idx].pop(c)
                return
        raise KeyError("Key not found in HashMap")

    def add(self, map_key: Any, map_value: Any) -> None:
        idx = self.__get_idx__(map_key)
        for c, (key, _) in enumerate(self.__map[idx]):
            if map_key == key:
                self.__map[idx][c] = (map_key, map_value)
                return

        self.__len += 1
        self.__map[idx].append((map_key, map_value))
        if self.__len >= self.__size:
            self.__map.extend([[] for _ in range(self.__size)])
            self.__size *= 2

    def keys(self) -> Generator[Key, None, None]:
        for arr in self.__map:
            for tup in arr:
                yield tup[0]

    def values(self) -> Generator[Value, None, None]:
        for arr in self.__map:
            for tup in arr:
                yield tup[1]

    def items(self) -> Generator[Tuple[Key, Value], None, None]:
        for arr in self.__map:
            for tup in arr:
                yield tup
