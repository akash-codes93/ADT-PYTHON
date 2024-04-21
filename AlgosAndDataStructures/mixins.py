import json


class DictMixin:

    def to_dict(self):
        attrs = [a for a in vars(self) if not a.startswith('_')]
        obj_dict = {}
        for attr in attrs:
            obj_dict[attr] = getattr(self, attr)

        return obj_dict


class JSONMixin:

    def to_json(self):
        obj_dict = self.to_dict()
        try:
            return json.dumps(obj_dict)
        except Exception:
            raise TypeError("Object is not JSON serializable")


class MyClass(DictMixin, JSONMixin):

    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret


class MyClass1(DictMixin):

    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret


obj = MyClass("abc", 10, "secret")
obj1 = MyClass1("abc", 10, "secret")


print(obj.to_dict())
print(obj1.to_dict())
print(obj.to_json())
