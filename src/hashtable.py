# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # Hash the key to find the index
        index = self._hash_mod(key)
        # Check if there's already a value in the bucket
        if self.storage[index] is not None:
            # if there is throw a warning and overwrite the value (if the key matches, part 2)
            print("Warning! Overwriting content. Hash Collision occurred.")
        # if there isn't create a new pair
        else:
            new_node = LinkedPair(key, value)
            self.storage[index] = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # find the hashed value of the key
        index = self._hash_mod(key)
        # if the index exists and the key matches
        if self.storage[index] is not None and key == self.storage[index].key:
            # remove the value stored with the given key
            self.storage[index].value = None
        # else print a warning that the key doesn't exist
        else:
            print("Key Error: Key doesn't exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash the key to find the index
        index = self._hash_mod(key)
        # if there is a value at that index
        if self.storage[index] is not None:
            # return that value at that index
            return self.storage[index].value
        else:
            # return none if no key is found at index
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # make a copy of the storage list
        old_capacity = self.storage
        # double the capacity of the hashtable
        self.capacity *= 2
        # reset all items in array back to None's
        self.storage = self.capacity * [None]
        # iterate through the copied list and hash all the keys again
        for item in old_capacity:
            if item is not None:
                # insert each item back into the storage list
                self.insert(item.key, item.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
