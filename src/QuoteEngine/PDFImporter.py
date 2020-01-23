from .IngestorInterface import IngestorInterface
import subprocess
import random

from typing import List
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path : str) -> List[QuoteModel]:
        quotes = []

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        for line in file_ref.readlines():
            if line != "":
                parse = line.text.split('-')
                new_quote = QuoteModel(parse[1], parse[0])
                quotes.append(new_quote)
        return quotes
