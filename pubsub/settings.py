# -*- coding: utf-8 -*-

__author__ = 'goran'

import redis

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

r = redis.StrictRedis(**config)