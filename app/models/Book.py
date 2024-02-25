class Book:
    def __init__(self, title, description, author, cover_image, price):
        self.title = title
        self.description = description
        self.author = author
        self.cover_image = cover_image
        self.price = price

    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'author': self.author.serialize(),
            'cover_image': self.cover_image,
            'price': f'{self.price:.2f}'
        }