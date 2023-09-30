class Vector:
    def __init__(self, *args):
        import numbers

        if not all(isinstance(arg, numbers.Number) for arg in args):
            raise ValueError("Input should be a sequence of numbers")
        self._val = tuple(args)

    @property
    def dim(self):
        return len(self._val)

    def __add__(self, other):
        if not self._conformable(other):
            return NotImplemented
        return Vector(*[a + b for a, b in zip(self, other)])

    def __mul__(self, other):
        import numbers

        if not isinstance(other, numbers.Number):
            return NotImplemented
        return Vector(*[a * other for a in self._val])

    def __len__(self):
        return len(self._val)

    def __eq__(self, other):
        if self._conformable(other):
            return all(a == b for a, b in zip(self, other))
        return False

    def dot(self, other):
        if not self._conformable(other):
            raise ValueError("cannot dot product with a non-vector")
        return sum(a * b for a, b in zip(self, other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        return iter(self._val)

    def __getitem__(self, i):
        return self._val[i]

    def __str__(self):
        return "(" + ", ".join(str(x) for x in self._val) + ")"

    def _conformable(self, other):
        return isinstance(other, Vector) and self.dim == other.dim
