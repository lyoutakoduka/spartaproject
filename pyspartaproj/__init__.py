#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PySpartaSilent:
    still_alive: bool

    def run(self) -> None:
        print('run sparta silently')

    def shutdown(self) -> None:
        print('shutdown sparta')

    def delete(self) -> None:
        print('delete sparta')
        self.still_alive = False

    def __del__(self) -> None:
        if self.still_alive:
            self.delete()

    def __init__(self) -> None:
        self.still_alive = True


class PySpartaAPI:
    def create_silent_sparta(
        self,
        online: bool = True,
        offline: bool = True
    ) -> PySpartaSilent:

        silent_app = PySpartaSilent()

        return silent_app


def __main():
    sparta_api = PySpartaAPI()

    sparta_instance = sparta_api.create_silent_sparta(online=True)
    sparta_instance.run()
    sparta_instance.shutdown()
    sparta_instance.delete()


if __name__ == '__main__':
    __main()
