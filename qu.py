"""
Queue.
@author:James
@License:MIT
"""

__all__ = ["Queue"]


class NoElementInQueryError:
    def __init__(self):
        pass


class Queue:
    def __init__(self, length: int = 0):
        self.__lst = []
        for self.__i in range(length):
            self.__lst.append("")

    def __str__(self):
        return "[Object queue]"

    def addQuery(self, value):
        self.__lst.insert(0, value)

    def popQuery(self):
        if len(self.__lst) > 0:
            return self.__lst.pop()
        else:
            raise NoElementInQueryError

    def getLen(self):
        return len(self.__lst)
