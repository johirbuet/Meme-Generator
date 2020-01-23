from .IngestorInterface import IngestorInterface
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

"""
This file is responsible for reading txt files and returning quotes from txt file
"""

class TXTImporter(IngestorInterface):
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path : str) -> List[QuoteModel]:

        quotes = []
        with open(path, 'r') as file:
            for line in file.readlines():
                if line != "":
                    parse = line.split("-")
                    new_quote = QuoteModel(parse[1], parse[0])
                    quotes.append(new_quote)
        return quotes