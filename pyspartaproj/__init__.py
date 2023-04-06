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
    def create_silent_sparta(
        self,
        online: bool = True,
        offline: bool = True
    ) -> PySpartaSilent:

        silent_app = PySpartaSilent()

        return silent_app
