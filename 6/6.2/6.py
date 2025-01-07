# Отчёт успеваемости
from pandas import DataFrame


def best(journal: DataFrame) -> DataFrame:
    new_journal = journal.copy()
    return new_journal[
        (new_journal["maths"] > 3) & (new_journal["physics"] > 3) & (new_journal["computer science"] > 3)]