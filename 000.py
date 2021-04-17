import turtle
from typing import Any, Callable

tur: Callable[[Any, Any], Any] = lambda x, y: exec("turtle.%s(%d)" % (x, y))
tur("forward", 100)
