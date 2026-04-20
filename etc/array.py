class Array:
    def __init__(self, array: list) -> None:
        self.array = array

    def __repr__(self) -> str:
        return "[" + ", ".join([str(a) for a in self.array]) + "]"

    def __len__(self) -> int:
        return len(self.array)

    def __add__(self, other) -> "Array":
        if isinstance(other, Array):
            if len(self) != len(other):
                raise AttributeError("Other has a wrong number of elements")
            return Array([i + j for i, j in zip(self.array, other.array)])
        elif isinstance(other, (float, int)):
            return Array([i + other for i in self.array])
        else:
            raise TypeError("Other is wrong type")

    def __mul__(self, other) -> "Array":
        if isinstance(other, Array):
            if len(self) != len(other):
                raise AttributeError("Other has a wrong number of elements")
            return Array([i * j for i, j in zip(self.array, other.array)])
        elif isinstance(other, (float, int)):
            return Array([i * other for i in self.array])
        else:
            raise TypeError("Other is wrong type")

    def __sub__(self, other) -> "Array":
        return self + other * -1
