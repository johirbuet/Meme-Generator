
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TxtImporter import TXTImporter
from typing import List
from .QuoteModel import QuoteModel
class Ingestor:

    ingestors = [CSVImporter, DocxImporter, PDFImporter, TXTImporter]


    @classmethod
    def parse(cls, path : str) -> List[QuoteModel]:
        for ing in cls.ingestors:
            if ing.can_ingest(path):
                return ing.parse(path)