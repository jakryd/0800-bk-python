# An example coded during classes


class Array:
    def __init__(self, array: list) -> None:
        self._array = array

    def __repr__(self) -> str:
        return "[" + ", ".join([str(a) for a in self._array]) + "]"

    def __len__(self) -> int:
        return len(self._array)

    def __add__(self, other) -> "Array":
        if isinstance(other, Array):
            if len(self) != len(other):
                raise AttributeError("Other has a wrong number of elements")
            return Array([i + j for i, j in zip(self._array, other._array)])
        elif isinstance(other, (float, int)):
            return Array([i + other for i in self._array])
        else:
            raise TypeError("Other is wrong type")

    def __mul__(self, other) -> "Array":
        if isinstance(other, Array):
            if len(self) != len(other):
                raise AttributeError("Other has a wrong number of elements")
            return Array([i * j for i, j in zip(self._array, other._array)])
        elif isinstance(other, (float, int)):
            return Array([i * other for i in self._array])
        else:
            raise TypeError("Other is wrong type")

    def __sub__(self, other) -> "Array":
        return self + other * -1

    def __truediv__(self, other) -> "Array":
        if isinstance(other, Array):
            if len(self) != len(other):
                raise AttributeError("Other has a wrong number of elements")
            return Array([i / j for i, j in zip(self._array, other._array)])
        elif isinstance(other, (float, int)):
            return Array([i / other for i in self._array])
        else:
            raise TypeError("Other is wrong type")

    def __pow__(self, other) -> "Array":
        if isinstance(other, Array):
            if len(self) != len(other):
                raise AttributeError("Other has a wrong number of elements")
            return Array([i**j for i, j in zip(self._array, other._array)])
        elif isinstance(other, (float, int)):
            return Array([i**other for i in self._array])
        else:
            raise TypeError("Other is wrong type")

    def __neg__(self) -> "Array":
        return self * -1

    def sum(self) -> float:
        return sum(self._array)

    def mean(self) -> float:
        return self.sum() / len(self)

    def var(self) -> float:
        """
        var(array) = (sum_i (mean(array) - array_i) ** 2) / N
        """
        return ((self - self.mean()) ** 2).mean()

    def std(self) -> float:
        return self.var() ** 0.5

    def __getitem__(self, subscript) -> float:
        return self._array[subscript]

    # getter
    @property
    def array(self):
        return self._array

    # setter
    @array.setter
    def array(self, arr):
        if isinstance(arr, list):
            self._array = arr
        else:
            raise TypeError("arr is wrong type")
