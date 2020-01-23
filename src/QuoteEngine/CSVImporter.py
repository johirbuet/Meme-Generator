

from .IngestorInterface import IngestorInterface
import pandas as pd
from typing import List
from .QuoteModel import QuoteModel
class CSVImporter(IngestorInterface):
    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        df = pd.read_csv(path)
        quotes = []
        for i in range(len(df)):
            q = QuoteModel(df.iloc[i, 1], df.iloc[i, 0])
            quotes.append(q)
        return quotes

