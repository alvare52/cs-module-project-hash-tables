class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < 8:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        # self.capacity = capacity
        self.container = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.container)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        string_bytes = key.encode()

        total = 0

        for byte in string_bytes:
            total += byte
            # NEW (clamp to 32 bits)
            total &= 0xffffffff
        
        return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        self.container[index] = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        if self.get(key) is None:
            print("Key not found")
            return None
        
        else:
            valueRemoved = self.get(key)
            self.put(key, None)
            return valueRemoved
        



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        return self.container[index]


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

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    
    # Lecture Notes Day 3
    
    # Fibonacci 

    cache = {}
    def fib(n):
        if n <= 1:
            return n


        # if n not in cache:
            # cache[n] = fib(n-1) + fib(n-2)

        # or just this
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n - 1) + fib(n - 2)
        #    
        
        return cache[n]

    print(fib(3))
    print(fib(5))
    print(fib(6))
    print(fib(7))
    print(fib(50))

    # Cache 

    import math

    lookup_table = {}

    def inverse_root(n):
        return 1 / math.sqrt(n)

    def build_lookup_table():
        for i in range(1, 1000):
            lookup_table[i] = inverse_root(i)
    
    build_lookup_table()

    print(lookup_table[556])
    print(lookup_table[99])
    print(lookup_table[999])

    # lazily = just in time, only when we need it

    # dictionaries aren't in order because everything hashes differently

    # Sorting

    # lists keep things in order
    # my_list = []
    # my_list.append(1)
    # my_list.append(2)
    # my_list.append(3)
    # my_list.append(4)
    # my_list.append(5)
    # ​
    # # why are dictionaries not in order? i.e., order is not guaranteed
    # ## everything hashes differently
    # ## don't know what index the hash function will return
    # ​
    # my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]
    # ​
    # d = {
    #     'Austin': 12,
    #     'Michael': 24,
    #     'Troy': 35,
    #     'Jorge': 99,
    #     'David': 42
    # }
    # ​
    # # how can we sort our dictionary?
    # ​
    # # turn into a list
    # for pair in d.items():
    #     print(pair)
    # ​
    # # d.items().sort()
    # ​
    # print(sorted(d.items()))
    # ​
    # sorted_list_of_items = list(d.items())
    # ​
    # def anon_function(pair):
    #     return pair[1]
    # ​
    # # sorted_list_of_items.sort(reverse=True, key=anon_function)
    # sorted_list_of_items.sort(reverse=True, key=lambda pair: pair[1])
    # ​
    # print(sorted_list_of_items)
    # ​
    # # Erik's way with list comprehension: sorted([(v, k) for k, v in d.items()])
    # ​
    # # const my_func = x => x * 2
    # ​
    # something = list(map(lambda x, y:
    #     x * 2, [1, 2, 3]))

    # Print Letter Count

    # # Understand
    # # given a string
    # ## return every letter and how many times it occurs in this string
    # ## sorted by frequence of occurrence
    # ​
    # # Planning 
    # # iterate through our string
    # # tally the count using a dictionary
    # # sort our dictionary by the value (i.e. the count of each letter)
    # ​
    # # upper- or lower-case everything
    # # handle spaces
    # ​
    # # should we turn the string into a list first?
    # ​
    # # Execute
    # def print_letter_count(s):
    #     tally = {}
    # ​
    #     s = s.lower()
    #     for character in s:
    #         # if not char.isspace():
    #         # if char != " ":
    #         if character >= 'a' and character <= 'z':
    #             if character not in tally:
    #                 tally[character] = 1
    #             else:
    #                 tally[character] += 1
    # ​
    #     # print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
    #     # sorted gives back a new function
    # ​
    #     # sort works in place
    #     tally_list = list(tally.items())
    #     tally_list.sort(key=lambda x: x[1], reverse=True)
    # ​
    #     # alternate way to reverse sort
    #     # tally_list.sort(key = lambda x: (-(x[1]))
    # ​
    #     for pair in tally_list:
    #         print(f'Count: {pair[1]}, letter: {pair[0]}')
    # ​
    # ​
    # ​
    # print_letter_count("bunny hop")
    # print_letter_count("The quick brown fox jumps over the lazy dog")