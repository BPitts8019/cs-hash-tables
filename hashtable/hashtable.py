class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HTEntry: ({self.key}, {self.value}) -> {self.next}"

    def __str__(self):
        return f"HTEntry: ({self.key}, {self.value}) -> {self.next}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
MAX_32_BITS = 0xFFFFFFFF
MAX_64_BITS = 0xFFFFFFFFFFFFFFFF


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.size = 0
        self.storage = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_OFFSET = 0xcbf29ce484222325
        FNV_PRIME = 0x00000100000001B3
        encoded_key = key.encode()

        index = FNV_OFFSET
        for val in encoded_key:
            index = index * FNV_PRIME
            index = index ^ val

        return index & MAX_64_BITS

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        encoded_key = key.encode()
        index = 5381
        for val in encoded_key:
            index = ((index << 5) + index) + val
            # index * 33 + val #

        return index & MAX_32_BITS

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # TODO Check Load Factor and resize if necessary

        index = self.hash_index(key)
        cur_entry = self._get_entry(key)

        # Insert the new item #
        if cur_entry is None and self.storage[index] is not None:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self._insert(new_entry, index)
        else:
            self._insert(HashTableEntry(key, value), index)

    def _insert(self, entry, index):
        self.storage[index] = entry
        self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.storage[self.hash_index(key)] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        entry = self._get_entry(key)
        return entry.value if entry is not None else None

    def _get_entry(self, key):
        index = self.hash_index(key)
        cur_entry = self.storage[index]

        while cur_entry is not None:
            if cur_entry.key == key:
                return cur_entry
            else:
                cur_entry = cur_entry.next

        return cur_entry

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print(ht.get("line_2"))
    print(ht.get("line_10"))
    print(ht.get("line_42"))

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
