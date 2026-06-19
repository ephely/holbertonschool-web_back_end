#!/usr/bin/env python3
Cache = __import__('exercise').Cache
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay = __import__('exercise').replay
replay(cache.store)
