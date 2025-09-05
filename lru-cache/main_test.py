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


def test_case_1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_case_2():
    cache = LRUCache(2)
    assert cache.get(2) == -1
    cache.put(2, 6)
    assert cache.get(1) == -1
    cache.put(1, 5)
    cache.put(1, 2)
    assert cache.get(1) == 2
    assert cache.get(2) == 6


def test_case_3():
    cache = LRUCache(10)
    cache.put(7, 28)
    cache.put(7, 1)
    cache.put(8, 15)
    assert cache.get(6) == -1
    cache.put(10, 27)
    cache.put(8, 10)
    assert cache.get(8) == 10
    cache.put(6, 29)
    cache.put(1, 9)
    assert cache.get(6) == 29
    cache.put(10, 7)
    assert cache.get(1) == 9
    assert cache.get(2) == -1
    assert cache.get(13) == -1
    cache.put(8, 39)
    cache.put(1, 5)
    assert cache.get(1) == 5
    cache.put(13, 2)
    assert cache.get(12) == -1
