import abc


class ClientError(Exception):
    pass


class Client(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send_request(self, query: str) -> str:
        raise NotImplementedError
