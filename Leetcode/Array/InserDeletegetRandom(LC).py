#LEETCODE (medium)

"""Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.

    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
        false otherwise.

    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
        false otherwise.

    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element
        exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity."""

import random
class RandomizedSet:
    def __init__(self):
        self.data=[] #array
        self.index_map={} #hash map

    def Insert(self, val):
        if val in self.index_map:
            return False
        self.data.append(val) #adding value in the array
        self.index_map[val]=len(self.data)-1 #changing the index of the hash map
        return True

    def Remove(self, val):
        if val not in self.index_map:
            return False
        index=self.index_map[val] #Finding the index of the value to be removed
        last_element=self.data[-1] #swapping the element to be removed with the last element
        self.data[index]=last_element
        self.index_map[last_element]=index
        self.data.pop() #removing the last element from the list and the map
        del self.index_map[val]

    def getRandom(self):
        return random.choice(self.data)