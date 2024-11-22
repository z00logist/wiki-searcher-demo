import abc
import typing as t

TI = t.TypeVar("TI")
TO = t.TypeVar("TO")


class SearcherError(Exception):
    pass


class Searcher(t.Generic[TI, TO], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_info(self, key: TI) -> TO:
        raise NotImplementedError
