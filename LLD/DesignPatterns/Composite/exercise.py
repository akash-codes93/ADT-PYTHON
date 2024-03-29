"""
Consider the code presented below. We have two classes called SingleValue and ManyValues.
SingleValue stores just one numeric value, but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values
that the object contains. Please ensure that there is only a single method that realizes the property sum,
not multiple methods.
"""
import unittest


class SingleValue:
    def __init__(self, value):
        self.value = value

    @property
    def sum(self):
        return self.value


class ManyValues(list):

    def append(self, value):
        if isinstance(value, SingleValue):
            super().append(value.sum)
        elif isinstance(value, ManyValues):
            for o in value:
                self.append(o)
        else:
            super().append(value)

    @property
    def sum(self):
        _sum = 0
        for o in self:
            _sum += o
        return _sum


# class FirstTestSuite(unittest.TestCase):
#     def test(self):
single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)
# make a list of all values
all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)
# self.assertEqual(
print(all_values.sum)
# , 66)

