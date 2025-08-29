def find_min_key(timer_dict):
    min_key = None
    min_value = None
    for key, value in timer_dict.items():
        if not min_value or value < min_value:
            min_value = value
            min_key = key
    return min_key


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._cache = dict()
        self._ages = dict()
        self._timer = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self._timer += 1
        value = self._cache.get(key, -1)
        if value != -1:
            self._ages[key] = self._timer
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self._timer += 1
        self._cache[key] = value
        self._ages[key] = self._timer
        if len(self._cache) > self._capacity:
            self.evict()

    def evict(self):
        min_key = find_min_key(self._ages)
        del self._cache[min_key]
        del self._ages[min_key]
