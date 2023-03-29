from queue import PriorityQueue


class Book:

    def __init__(self, name, author, category, publisher=None, published_year=None, price=0):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.published_year = published_year
        self.category = category
        self.price = price
        self.sold = 0

    def __str__(self):
        return f"Name: {self.name} \n" \
               f"Author: {self.author} \n" \
               f"Publisher: {self.publisher} \n" \
               f"Year: {self.published_year} \n" \
               f"Category: {self.category} \n" \
               f"Price: {self.price} \n" \
               f"sold: {self.sold} \n"

    def sell_book(self, qty=1):
        self.sold += qty

    def __gt__(self, other):
        return self.sold < other.sold

    def __lt__(self, other):
        return self.sold > other.sold


"""
We can use priority Queue instead inside a dict because of the requirement
that says we need to fetch k elements
"""


class Catalog(list):

    def __init__(self):
        super().__init__()
        self.author = {}
        self.category = {}

    def add(self, name, author, category, publisher=None, published_year=None, price=0):
        book = Book(name, author, category, publisher, published_year, price)
        self.append(
            book
        )
        if author in self.author:
            self.author[author].put(book)
        else:
            p = PriorityQueue()
            p.put(book)
            self.author[author] = p

        if category in self.category:
            self.category[category].put(book)
        else:
            p = PriorityQueue()
            p.put(book)
            self.category[category] = p

    def search_by_name(self, name):
        for book in self:
            if book.name == name:
                return book

        for book in self:
            if name in book.name:
                return book

        return None

    def search_by_author(self, author):
        for book in self:
            if book.author == author:
                return book

        for book in self:
            if author in book.author:
                return book

        return None

    def most_sold_by_author(self, author, limit=float('inf')):
        # simple approach
        # books = sorted(filter(lambda book: book.author == author, self), key=lambda book: book.sold, reverse=True)
        #
        # if limit:
        #     return list(books)[:limit]
        # else:
        #     return list(books)

        if author not in self.author:
            print("Author not present in catalogue, Please add a book.")

        books = []
        author_queue = self.author[author]
        while (not author_queue.empty()) and limit != 0:
            books.append(
                author_queue.get()
            )
            limit -= 1
        return books

    def most_sold_by_category(self, category, limit=float('inf')):
        if category not in self.category:
            print("Category not present in catalogue, Please add a book.")

        books = []
        category_queue = self.category[category]
        while (not category_queue.empty()) and limit > 0:
            category_book = category_queue.get()
            books.append(
                category_book
            )
            limit -= 1
        return books

    @staticmethod
    def update_queue(queue_name):
        new_queue = PriorityQueue()
        while not queue_name.empty():
            _book = queue_name.get()
            new_queue.put(_book)
        return new_queue

    def sell(self, name, qty=1):
        book = list(filter(lambda b: b.name == name, self))[0]
        book.sell_book(qty)

        # self.author[book.author] = self.update_queue(self.author[book.author])
        self.category[book.category] = self.update_queue(self.category[book.category])


def print_books(books):
    for book in books:
        print(book)


c = Catalog()

c.add("b1", "akash", "drama")
c.add("b2", "akash", "suspense")
c.add("b3", "akash", "suspense")

bk = c.search_by_author('akash')
print(bk)
print("-----")


# most_sold_bks = c.most_sold_by_category("suspense")
# print_books(most_sold_bks)
# print("-----")

c.sell("b3", 10)

print("-----")
most_sold_bks = c.most_sold_by_category("suspense", 1)
print_books(most_sold_bks)
print("-----")
