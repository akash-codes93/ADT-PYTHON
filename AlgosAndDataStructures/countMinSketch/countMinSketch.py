from abc import ABC


class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class HashFunction(ABC):

    def apply_hash(self, value): pass

    def get_name(self): pass


class PythonHashFunction(HashFunction):

    def __init__(self, bins):
        self.name = "python-hash"
        self.bins = bins

    def apply_hash(self, value):
        return hash(value) % self.bins

    def get_name(self):
        return self.name


class NormalHashFunction(HashFunction):

    def __init__(self, bins):
        self.name = "normal-hash"
        self.bins = bins

    def apply_hash(self, value):
        return sum([ord(i) for i in value]) % self.bins

    def get_name(self):
        return self.name


class HashFunctionManager(dict, metaclass=Singleton):

    def __init__(self, bins, *args, **kwargs):
        self.bins = bins
        super().__init__(*args, **kwargs)

    def list_hash_functions(self):
        return list(self.keys())

    def apply_hash(self, hash_name, value):

        if hash_name not in self:
            print("Hash function not present")
            return

        return self[hash_name].apply_hash(value)

    def add_hash_function(self, hash_class):
        obj = hash_class(self.bins)
        if obj.get_name() not in self:
            self[obj.get_name()] = obj
        else:
            print("hash function already present")


class CountMinSketch:

    def __init__(self, bins):
        self._sketch = {}
        self.hash_manager = HashFunctionManager(bins)
        for name in self.hash_manager.list_hash_functions():
            self._sketch.update({
                name: [0] * bins
            })

    def add_value(self, value):
        for name in self.hash_manager.list_hash_functions():
            hash_value = self.hash_manager.apply_hash(name, value)
            self._sketch[name][hash_value] += 1

    def get_frequency(self, value):
        frequencies = []
        for name in self.hash_manager.list_hash_functions():
            hash_value = self.hash_manager.apply_hash(name, value)
            frequencies.append(self._sketch[name][hash_value])
        return min(frequencies)


def driver():
    # hash manager
    hash_manager = HashFunctionManager(6)
    hash_manager.add_hash_function(PythonHashFunction)
    hash_manager.add_hash_function(NormalHashFunction)

    count_min_sketch = CountMinSketch(6)

    count_min_sketch.add_value('A')
    count_min_sketch.add_value('A')
    count_min_sketch.add_value('B')
    count_min_sketch.add_value('A')
    count_min_sketch.add_value('B')
    count_min_sketch.add_value('B')
    count_min_sketch.add_value('B')
    count_min_sketch.add_value('B')
    count_min_sketch.add_value('A')

    fr = count_min_sketch.get_frequency('B')
    print(fr)


driver()

