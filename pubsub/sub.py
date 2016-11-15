# -*- coding: utf-8 -*-

__author__ = 'goran'

from settings import r

if __name__ == '__main__':
    channel = input('Enter the channel to which you want to subscribe: ')

    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print('Listening to {channel}'.format(**locals()))

    while True:
        for item in pubsub.listen():
            print(item['data'])

