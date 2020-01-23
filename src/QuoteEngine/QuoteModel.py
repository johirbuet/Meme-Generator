
"""
This is the class that defines the quote model.
"""
class QuoteModel:
    def __init__(self, author, body):
        self.author = author
        self.body = body


    def __repr__(self):
        return f'{self.body} by {self.author}'


