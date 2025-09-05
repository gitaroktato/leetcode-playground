from typing import NamedTuple


def find_min_key(timer_dict):
    min_key = None
    min_value = None
    for key, value in timer_dict.items():
        if not min_value or value < min_value:
            min_value = value
            min_key = key
    return min_key


class CacheContent(NamedTuple):
    key: int
    value: int


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._cache: dict[int, int] = dict()
        self._content: list[CacheContent] = list()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self._cache.get(key, -1)
        if index != -1:
            # Move element to tail
            element = self._content[index]
            del self._content[index]
            self._content.append(element)
            self._cache[key] = len(self._content) - 1
            for others in self._content[index:-1]:
                self._cache[others.key] -= 1
            # Return the value
            return element.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Move new element to tail
        index = self._cache.get(key, -1)
        if index != -1:
            del self._content[index]
            for others in self._content[index:]:
                self._cache[others.key] -= 1
        self._content.append(CacheContent(key, value))
        self._cache[key] = len(self._content) - 1
        if len(self._cache) > self._capacity:
            self.evict()

    def evict(self):
        first = self._content[0]
        del self._content[0]
        del self._cache[first.key]
        for element in self._content:
            self._cache[element.key] -= 1
