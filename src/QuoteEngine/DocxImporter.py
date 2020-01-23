
from .IngestorInterface import IngestorInterface
import docx
from typing import List
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    allowed_extensions = ["docx"]


    @classmethod
    def parse(cls, path : str) -> List[QuoteModel]:
        doc = docx.Document(path)
        quotes = []
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[1], parse[0])
                quotes.append(new_quote)

        return quotes
