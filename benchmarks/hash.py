# -*- coding: utf-8 -*-

'''
10000 entries have been set in 0.638624906539917 seconds. Average time per entry is 6.38624906539917e-05 seconds
10000 entries get in 0.5721719264984131 seconds. Average time per entry is 5.721719264984131e-05 seconds
10000 entries deleted in 0.573521614074707 seconds. Average time per entry is 5.7352161407470705e-05 seconds

Tested on: Intel(R) Core(TM) i7-2630QM CPU @ 2.00GHz
'''

from time import time

__author__ = 'goran'

from settings import r

HASH_NAME = 'hash_test'
ENTRIES_COUNT = 10000

keys_values = [('key{}'.format(i), 'value{}'.format(i)) for i in range(ENTRIES_COUNT)]

# benchmark hset
before = time()
for k, v in keys_values:
    r.hset(HASH_NAME, k, v)
after = time()
time_diff = after - before
print('{} entries have been set in {} seconds. Average time per entry is {} seconds'.format(ENTRIES_COUNT, time_diff, time_diff / ENTRIES_COUNT))


# benchmark hget
before = time()
for k, v in keys_values:
    r.hget(HASH_NAME, k)
after = time()
time_diff = after - before
print('{} entries get in {} seconds. Average time per entry is {} seconds'.format(ENTRIES_COUNT, time_diff, time_diff / ENTRIES_COUNT))


# benchmark hdel
before = time()
for k, v in keys_values:
    r.hdel(HASH_NAME, k)
after = time()
time_diff = after - before
print('{} entries deleted in {} seconds. Average time per entry is {} seconds'.format(ENTRIES_COUNT, time_diff, time_diff / ENTRIES_COUNT))

r.delete(HASH_NAME)