import math


class Complex:
    """
    Complex type.

    Arguments
    ---------
    real : float
        Real part of a complex number.
    imag : float
        Imaginary part of a complex number.
    """

    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __repr__(self) -> str:
        """Returns str representation on a complex number."""
        return f"Complex [{self.real}, {self.imag}]"

    def __len__(self) -> int:
        """Returns length of a complex number."""
        return 2

    def __add__(self, other: Complex) -> Complex:
        """Adds two complex numbers."""
        return Complex(
            real=self.real + other.real,
            imag=self.imag + other.imag,
        )

    def __sub__(self, other: Complex) -> Complex:
        """Adds two complex numbers."""
        return Complex(
            real=self.real - other.real,
            imag=self.imag - other.imag,
        )

    def __mul__(self, other: Complex) -> Complex:
        """
        [a, b] = a + ib, where i^2 = -1
        [a, b] * [c, d] = (a + ib) * (c + id) = (ac - bd) + i(ad + bc)
        """
        return Complex(
            real=self.real * other.real - self.imag * other.imag,
            imag=self.real * other.imag + self.imag * other.real,
        )

    def __truediv__(self, other: Complex) -> Complex:
        """
        (a + ib) / (c + id) =               * (c - id)
        [(a + ib) * (c - id)] / (c ** 2 + d ** 2) =
        [(ac + bd) + i(bc - ad)] / module() ** 2
        """
        m_sqr = other.module() ** 2
        if m_sqr:
            return Complex(
                real=(self.real * other.real + self.imag * other.imag) / m_sqr,
                imag=(self.imag * other.real - self.real * other.imag) / m_sqr,
            )
        raise ZeroDivisionError()

    def module(self) -> float:
        """
        Returns the module of a complex number.
        Defined as: length of [a, b]
        """
        return math.sqrt(self.real**2 + self.imag**2)

    def angle(self, convert_to_deg=False) -> float:
        """
        Returns the angle for a complex number.
        """
        rad = math.atan(self.imag / self.real)
        if convert_to_deg:
            return math.degrees(rad)
        else:
            return rad
