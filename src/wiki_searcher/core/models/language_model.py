import abc


class LanguageModelError(Exception):
    pass


class LanguageModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate(self, text: str) -> str:
        raise NotImplementedError
