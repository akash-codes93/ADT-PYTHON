from abc import ABC, abstractmethod


class FileSystem(ABC):

    @abstractmethod
    def ls(self):
        pass


class File(FileSystem):

    def __init__(self, name):
        self.name = name

    def ls(self):
        print("  file: ", self.name)


class Directory(list, FileSystem):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def add(self, child):
        self.append(child)

    def ls(self):
        print("Directory: ", self.name)

        for file in self:
            file.ls()


if __name__ == '__main__':
    dir1 = Directory("Movies")
    action = Directory("action")
    romantic = Directory("romantic")

    dir1.add(action)
    dir1.add(romantic)

    pathaan = File("pathaan")
    don = File("don")
    action.add(pathaan)
    action.add(don)

    kkhh = File("kuch kuch hota hai")
    romantic.add(kkhh)

    dir1.ls()
