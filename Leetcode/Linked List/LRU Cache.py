# LRU Cache (Least Recently Used)

"""Least Recently Used Cache is a key-value storage that has some capacity and a specific key eviction policy. Whenever 
it's specified in Gb, percentage of RAM or number of keys, the cache capacity is useful to prevent the storage from overflowing 
the available memory resources and shutting down unexpectedly.


But what can we do when we are about to reach our capacity limits?
This is where eviction is helpful. In the case of LRU policy, we can just remove key-values that were not accessed for the longest time 
a.k.a least-recently-used items. This is a pretty natural things to do and it's commonly used in such popular key-value storages as Redis.

Another part to pay attention to is cache. Cache is a kind of storage that is usually optimized for reading and retrieving information that 
would be time- or resource-consuming to calculate or collect without the cache.


Problem Framing:
Now we have a broad context around LRU cache use cases and we are ready to formulate the challenge.

We want to design a class that represents LRU cache and has the following APIs:

    LRUCache(capacity: int): class should be initialized with a capacity of the storage where the capacity is simply 
    a number of keys that storage can hold.
    
    get(key: int): method which can retrieve the value by key in constant time (O(1)).
    
    put(key: int, value: int): method which stores key-value pair in the cache in constant time (O(1)). If a key is already in the storage, 
    we need to replace its value with a new one. put() method should be constrained by capacity value and should not exceed it. 
    When capacity restriction is about to be reached, we need to evict the least-recently-used item to put a new key-value pair to the storage.

Since we are trying to design a cache storage, pretty much every operation should be done in constant time execution on average to keep it 
practically useful. This means that key eviction should also happen in O(1) complexity range.


Solutions:

When I think about cache, dictionaries or hashmaps come to my mind.
key 1 = value 1
key 2 = value 2
'
'
key n = value n
(Cache based on a hashmap)

Hashmaps allow to read and write key-value pairs in constant time with high probability.

The problem with dictionaries is that they usually don't guarantee order in which they manage keys. So we don't have a way to quickly 
remove least-recently-used items. 

We could introduce a notion of last-used timestamps for each item in the hashmap and update these timestamps during accessing the keys in 
get() method.

key 1 = value 1  <- 12345          timestamps require sequential search for LRU items
key 2 = value 2  <- 12346
'
'
key n = value n  <- nnnnn

Timestamps won't help us because of sequential search we need to do on the hashmap

However, it would still take us O(n) in order to find items to evict by timestamps. It's too time-consuming to meet our requirements.

Let's not get hung up on hashmaps. The problem with tracking item usage can be solved with linked lists.

    Linked List as LRUcache

    key 1     ->      value 1   -> Most recently used item on top
      |                 |       -> movement 
    key 2     ->      value 2
      |                 |
    key 3     ->      value 3
      |                 |
    key 4     ->      value 4
      |                 |
    key n     ->      value n   -> Least recently used item on bottom

    Cache based a linked list

With linked lists, we could keep track of item usages in constant time. We could simply move the item we currently access to the top of 
the list. In a natural way, least used items end up being at the very bottom of the list and we would get a list ordered by item usage as 
we go. Since we need to relink our items, it would be helpful to have reference to the previous and next items on the list.

Nevertheless, linked lists don't meet our requirements completely. It would take us O(n) in order to find and retrieve item by key. This is a 
sad complexity for cache storages.

To sum up, hashmaps luck the advantages of linked lists and linked lists luck advantages of hashmaps. We find to find a way to combine hashmaps 
and linked lists such that we meet our LRU cache requirements.
"""