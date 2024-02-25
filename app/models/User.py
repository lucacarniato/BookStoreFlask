class User:
    def __init__(self, username, author_pseudonym):
        self.username = username
        self.author_pseudonym = author_pseudonym

    def serialize(self):
        return {
            'username': self.username,
            'author_pseudonym': self.author_pseudonym
        }