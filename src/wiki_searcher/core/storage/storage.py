import abc
import typing as t

TI = t.TypeVar("TI")
TO = t.TypeVar("TO")


class StorageError(Exception):
    pass


class Storage(t.Generic[TI, TO], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch(self, key: TI) -> TO:
        raise NotImplementedError
