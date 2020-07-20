from datetime import datetime


class Node:

    def __init__(self, value, _next):
        self.value = value
        self.timestamp = datetime.now()

        if isinstance(_next, Node) or _next is None:
            self.next = _next
        else:
            raise ValueError("Parameter next can be none or Node Type")

    def __iter__(self):
        self.travel = self
        return self

    def __next__(self):

        if self.travel.next is not None:
            self.travel = self.travel.next
            return self.travel
        else:
            raise StopIteration


class PPDict(dict):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

        super(PPDict, self).__init__()

    def __getitem__(self, item):
        node = super(PPDict, self).__getitem__(item)
        return node.value

    def __setitem__(self, key, value):

        if key in self:
            old_node = super(PPDict, self).__getitem__(key)
            node = Node(value, old_node)
        else:
            node = Node(value, None)

        super(PPDict, self).__setitem__(key, node)

    def update(self, *args, **kwargs):

        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, "
                                "got %d" % len(args))
            other = dict(args[0])

            for key in other:
                if key in self:
                    old_node = super(PPDict, self).__getitem__(key)
                    node = Node(other[key], old_node)
                else:
                    node = Node(other[key], None)

                self[key] = node

        for key in kwargs:
            if key in self:
                old_node = super(PPDict, self).__getitem__(key)
                node = Node(kwargs[key], old_node)
            else:
                node = Node(kwargs[key], None)

            self[key] = node

    def setdefault(self, key, value=None):

        if key in self:
            old_node = super(PPDict, self).__getitem__(key)
            node = Node(value, old_node)
        else:
            node = Node(value, None)

        super(PPDict, self).setdefault(key, node)

    def get(self, key, default_value=None):

        node = super(PPDict, self).get(key, default_value)

        if isinstance(node, Node):
            node = node.value

        return node

    def values(self):

        values = super(PPDict, self).values()
        new_values = []

        for node in values:
            new_values.append(node.value)

        return new_values

    def items(self):

        items = super(PPDict, self).items()
        new_items = []

        for key, node in items:
            new_items.append((key, node.value))

        return new_items

    def __repr__(self):

        new_repr = {}

        for key, node in self.items():
            new_repr[key] = node

        return repr(new_repr)

    def historic_read(self, key, timestamp):

        try:
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError('Incorrect datetime format, valid-format: %Y-%m-%d %H:%M:%S')

        node = super(PPDict, self).__getitem__(key)

        node_iter = iter(node)

        while True:
            try:
                if node.timestamp <= timestamp:
                    return node.value
                else:
                    node = next(node_iter)

            except StopIteration:
                break
        return node.value
