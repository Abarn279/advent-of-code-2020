v2Cache = {}
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cached_string = f'{self.x},{self.y}'
    @staticmethod
    def create(x, y):
        if (x, y) in v2Cache:
            return v2Cache[(x, y)]
        v = Vector2(x, y)
        v2Cache[(x, y)] = v
        return v
    def to_tuple(self):
        return (self.x, self.y)
    def to_yx_tuple(self):
        return (self.y, self.x)
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    def sqr_magnitude(self):
        return self.x ** 2 + self.y ** 2
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash(self.cached_string)
    def __repr__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)
    def __str__(self):
        return self.__repr__()

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def to_tuple(self):
        return (self.x, self.y, self.z)
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
    def clone(self):
        return Vector3(self.x, self.y, self.z)
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x * other, self.y * other, self.z * other)
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __hash__(self):
        return hash(f'{self.x},{self.y},{self.z}')
    def __repr__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y) + ', z: ' + str(self.z)
    def __str__(self):
        return self.__repr__()

class Vector4(Vector3):
    def __init__(self, x, y, z, t):
        self.t = t
        super().__init__(x, y, z)
    def to_tuple(self):
        return (self.x, self.y, self.z, self.t)
    def manhattan_distance(self, other):
        return super().manhattan_distance(other) + abs(self.t - other.t)
    def __repr__(self):
        return super().__repr__() + ', t: ' + str(self.t)

def id_gen(start_at):
    while True:
        yield start_at
        start_at += 1