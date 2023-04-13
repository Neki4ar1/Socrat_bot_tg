# -*- coding: utf8 -*-
"""
Описан класс, слово и его перевод
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Word:
    """
    слова
    word - слово
    translation - перевод слова
    pk - primary key
    """
    word: str = ''
    translation: str = ''
    pk: int = 0
