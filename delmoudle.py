"""
@author:James
"""
__all__ = ["delete"]


def delete(*name):
    for i in name:
        exec("del " + i)
