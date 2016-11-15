# -*- coding: utf-8 -*-

__author__ = 'goran'

from settings import r

if __name__ == '__main__':
    name = input('Enter your username: ')
    channel = input('Enter the name of the channel in which you want to publish: ')

    print('Welcome to {channel}'.format(**locals()))

    while True:
        message = input('Enter a message: ')

        if message.lower() == 'exit':
            break

        message = '{name} says: {message}'.format(**locals())

        r.publish(channel, message)

