"""
You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        person = Person(self.id, name)
        self.id += 1
        return person


person_factory = PersonFactory()
_person = person_factory.create_person("akash")
_person1 = person_factory.create_person("akash_other")
