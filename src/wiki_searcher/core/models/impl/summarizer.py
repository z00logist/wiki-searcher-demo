import logging

from wiki_searcher.api.client import Client, ClientError
from wiki_searcher.core.models.language_model import LanguageModel, LanguageModelError

LOGGER = logging.getLogger(__name__)


class SummarizingLanguageModel(LanguageModel):
    def __init__(self, client: Client) -> None:
        self.__client = client
        self.__prompt = "Summarize the following text:\n\n{text}\n\nSummary:"

    def generate(self, text: str) -> str:
        try:
            response = self.__client.send_request(self.__prompt.format(text=text))
            return response
        except ClientError as error:
            raise LanguageModelError(
                f"Failed to generate summary because of error: '{error}'"
            ) from error
