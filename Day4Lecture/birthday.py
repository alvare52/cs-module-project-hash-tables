import random
import hashlib

# make a bunch of random keys
# hash them
# track the as we go
# stop when we get a collision

def hash_func(key):
    return int(hashlib.sha256(f"{key}".encode()).hexdigest(), 16)

def how_many_before_collision(array_size):
    previous_keys = set()
    successful_hashes = 0

    while True:
        random_key = random.random()
        hashed_key = hash_func(random_key) % array_size

        if hashed_key not in previous_keys:
            previous_keys.add(hashed_key)
            successful_hashes += 1
        # collision
        else:
            break
    print(f'buckets: {array_size}, tries: {successful_hashes} before collision, {successful_hashes / array_size * 100}% full')

how_many_before_collision(8)
how_many_before_collision(16)
how_many_before_collision(32)
how_many_before_collision(64)
how_many_before_collision(128)
how_many_before_collision(256)
