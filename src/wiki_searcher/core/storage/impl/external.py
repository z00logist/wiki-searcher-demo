import logging
import typing as t

import wikipedia
from yarl import URL

from wiki_searcher.core.storage.storage import Storage, StorageError

LOGGER = logging.getLogger(__name__)


class ArticlesByTopicStorage(Storage[str, t.Mapping[URL, str]]):
    def fetch(self, key: str) -> t.Mapping[URL, str]:
        try:
            search_entities = wikipedia.search(key, results=5)
        except (
            wikipedia.exceptions.HTTPTimeoutError,
            wikipedia.exceptions.WikipediaException,
        ) as error:
            raise StorageError(
                f"Got unexpected error while searching for topic: '{error}'"
            ) from error

        if search_entities == []:
            raise StorageError(f"No articles found for topic: '{key}'")

        articles: t.MutableMapping[URL, str] = {}

        for title in search_entities:
            try:
                page = wikipedia.page(title)
                url = URL(page.url)

                articles[url] = page.content

            except (
                wikipedia.exceptions.DisambiguationError,
                wikipedia.exceptions.PageError,
            ):
                LOGGER.warning(f"Skipping disambiguation page: '{title}'")
                continue
        return articles
