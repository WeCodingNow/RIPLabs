# Итератор для удаления дубликатов
import itertools

from setuptools.package_index import unique_everseen


class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.counter = 0
        if not "ignore_case" in kwargs:
            kwargs["ignore_case"] = False
        if "ignore_case" not in kwargs:
            self.bass = list(unique_everseen(items, str.lower))
            pass
        else:
            self.bass = list(unique_everseen(items))



    def __next__(self):
        if self.counter != len(self.bass):
            self.counter += 1
            return self.bass[self.counter - 1]
        else:
            raise StopIteration
        pass

    def __iter__(self):
        return self
