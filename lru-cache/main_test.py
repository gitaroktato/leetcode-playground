from main import LRUCache, find_min_key


def test_basic_functions():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(3) == 3


def test_find_min_value():
    timer = {1: 5, 2: 3, 3: 1, 4: 2}
    assert find_min_key(timer) == 3


def test_eviction():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    # Least recent is 2
    assert cache.get(2) == -1
