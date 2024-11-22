import typing as t

from yarl import URL

from wiki_searcher.core.models.language_model import LanguageModel, LanguageModelError
from wiki_searcher.core.searcher.searcher import Searcher, SearcherError
from wiki_searcher.core.storage.storage import Storage, StorageError


class ExternalSearcher(Searcher[str, t.Mapping[URL, str]]):
    def __init__(
        self, language_model: LanguageModel, storage: Storage[str, t.Mapping[URL, str]]
    ):
        self.__language_model = language_model
        self.__storage = storage

    def get_info(self, key: str) -> t.Mapping[URL, str]:
        try:
            aricles = self.__storage.fetch(key)
        except StorageError as error:
            raise SearcherError(
                f"Failed to fetch articles for topic: '{key}' because of error: '{error}'"
            ) from error
        try:
            return {
                url: self.__language_model.generate(content)
                for url, content in aricles.items()
            }
        except LanguageModelError as error:
            raise SearcherError(
                f"Failed to generate summary for topic: '{key}' because of error: '{error}'"
            ) from error
