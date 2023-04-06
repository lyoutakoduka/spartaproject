#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PySpartaSilent:
    def run(self):
        print('run sparta silently')

    def shutdown(self):
        print('shutdown sparta')

    def delete(self):
        print('delete sparta')
        self.still_alive = False

    def __del__(self):
        if self.still_alive:
            self.delete()

    def __init__(self):
        self.still_alive = True


class PySpartaAPI:
    def runOffline(self):
        print('running offline...')

    def __init__(self):
        print('initialing API...')
