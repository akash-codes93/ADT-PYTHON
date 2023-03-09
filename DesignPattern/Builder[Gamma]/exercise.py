"""
Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
Please observe the same placement of spaces and indentation.
"""


class CodeElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self):
        code = [self.name + " " + self.text + ':']

        if not self.elements:
            code.append(' ' * self.indent_size + "pass")
        else:
            code.append(
                ' ' * self.indent_size + "def __init__(self):"
            )

        element_intend = self.indent_size * 2
        for element in self.elements:
            code.append(
                ' ' * element_intend + "self." + element.name + " = " + str(element.text)
            )

        return '\n'.join(code)

    def __str__(self):
        return self.__str()


class CodeBuilder:
    __root = CodeElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = "class"
        self.__root.text = root_name

    def add_field(self, type, name):
        self.__root.elements.append(
            CodeElement(type, name)
        )
        return self

    def __str__(self):
        return str(self.__root)


cb = CodeBuilder('Person')
print(cb)

""" Other way """


class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.fields:
                lines.append('    %s' % f)
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()
