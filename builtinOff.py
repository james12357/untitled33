class list(list):
    def __truediv__(self, other):
        return self[0] if len(self) > 0 else (other[0] if len(other) > 0 else None)


print(list() / list())
