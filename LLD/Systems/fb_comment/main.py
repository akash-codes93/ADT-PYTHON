class User:

    def __init__(self, name):
        self.name = name
        self.__posts = []

    def create_posts(self, description):
        post = Posts(description)
        self.__posts.append(post)
        return post

    def get_posts(self):
        return self.__posts

    def create_comment(self, post, comment_value, parent_comment=None):
        return post.create_comment(self, comment_value, parent_comment)

    def __str__(self):
        return self.name


class Posts:
    def __init__(self, description):
        self.description = description
        self.__comments = []

    def create_comment(self, user, value, parent_comment=None):
        if parent_comment is None:
            comment = Comment(user, value, 1)
            self.__comments.append(comment)
        else:
            comment = Comment(user, value, parent_comment.depth + 1)
            parent_comment.add_sub_comment(comment)

        return comment

    def get_comments(self):
        return self.__comments

    def __str__(self):
        return " " + self.description


class Comment:
    MAX_DEPTH = 2

    def __init__(self, user, value, depth):
        self.value = value
        self.user = user

        if depth > Comment.MAX_DEPTH:
            raise Exception("Comment depth exceeded")

        self.depth = depth
        self.__comments = []

    def add_sub_comment(self, comment):
        self.__comments.append(comment)

    def get_sub_comments(self):
        return self.__comments

    def __str__(self):
        return 4 * self.depth * ' ' + self.value


def print_wall(user):
    print(f"{user}'s wall")
    for post in user.get_posts():
        print(post)
        for comment in post.get_comments():
            print(comment)
            for sub in comment.get_sub_comments():
                print(sub)


john = User('john')
jane = User('jane')

birthday_jane_post = jane.create_posts("Today is my birthday")
john_comment = john.create_comment(birthday_jane_post, "happy birthday")
jane_reply = jane.create_comment(birthday_jane_post, "Thanksyou", john_comment)
john1_comment = john.create_comment(birthday_jane_post, "Where is the party")

print_wall(jane)


