"""
Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(),
return the second instance.
"""


class TwistedSingleton(type):
    _even_instances = {}
    _odd_instances = {}
    odd = True

    def __call__(cls, *args, **kwargs):

        if cls.odd:
            instances = cls._odd_instances
            cls.odd = False
        else:
            instances = cls._even_instances
            cls.odd = True

        if cls not in instances:
            instances[cls] = super().__call__(*args, **kwargs)

        return instances[cls]


class Test(metaclass=TwistedSingleton):
    pass


t1 = Test()
t2 = Test()

t3 = Test()
t4 = Test()

print(t1 == t3)
print(t2 == t4)

print(t1 == t2)
print(t3 == t4)
print(t1 == t4)
print(t2 == t3)


