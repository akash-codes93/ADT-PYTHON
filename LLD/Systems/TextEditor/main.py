import copy


class Memento:

    def __init__(self, content):
        self.content = content


class TextEditor:

    def __init__(self):

        self.content = []
        self.changes = [Memento(self.content)]
        self.clipboard = []
        self.current = 0

    def display(self, n=None, m=None):

        def print_content(start, end):
            for i in range(start, end):
                print(f'{i}.) {self.content[i]}')

        if m is None and n is None:
            print_content(0, len(self.content))
        else:
            print_content(m, n)

    def insert(self, n, text):
        self.content.insert(n, text)
        self.current += 1
        self.changes.append(Memento(copy.deepcopy(self.content)))

    def delete(self, n, m=None):
        if m is None:
            del self.content[n]
        else:
            self.content = self.content[:n] + self.content[m + 1:]

        # print(self.content)
        self.current += 1
        self.changes.append(Memento(copy.deepcopy(self.content)))

    def copy(self, n, m):
        pass

    def paste(self, n):
        pass

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.content = m.content
            return m
        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.content = m.content
            return m
        return None


text_editor = TextEditor()
text_editor.insert(0, "This is the first line written to this editor")
text_editor.insert(1, "This is a beautiful day")
text_editor.insert(2, "Some tasks needs to be finished today")
text_editor.display()
print("-" * 10)
text_editor.delete(2)
text_editor.display()
print("-" * 10)
text_editor.undo()
text_editor.display()
print("-" * 10)
text_editor.redo()
text_editor.display()
