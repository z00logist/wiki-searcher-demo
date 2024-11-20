import logging

from huggingface_hub import (
    InferenceClient,
)
from huggingface_hub.errors import (
    HfHubHTTPError,
    RepositoryNotFoundError,
)

from wiki_searcher.api.client import Client, ClientError
from wiki_searcher.api.parameters import Parameters

LOGGER = logging.getLogger(__name__)


class HuggingFaceAPIClient(Client):
    def __init__(self, model: str, token: str, model_parameters: Parameters) -> None:
        LOGGER.info("Initializing HF Client with remote model.", extra={"model": model})
        try:
            self.__client = InferenceClient(model=model, token=token)
            self.__model_parameters = model_parameters
        except (HfHubHTTPError, RepositoryNotFoundError) as error:
            raise ClientError(
                f"Failed to initialize HF Client with remote model because of error: '{error}'"
            ) from error

    def send_request(self, prompt: str) -> str:
        LOGGER.info(
            "Sending request to the HuggingFace API",
            extra={"prompt_preview": prompt[:50]},
        )
        response = self.__client.text_generation(
            prompt, max_new_tokens=self.__model_parameters.max_new_tokens
        )
        if response and len(response) > 0:
            return str(response)
        else:
            raise ClientError("Received empty response from HuggingFace API.")
