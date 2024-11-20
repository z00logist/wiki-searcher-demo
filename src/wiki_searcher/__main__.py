import logging

import gradio as gr

from wiki_searcher.api.impl.hugging_face_client import HuggingFaceAPIClient
from wiki_searcher.api.parameters import Parameters
from wiki_searcher.configuration import Configuration
from wiki_searcher.core.models.impl.summarizer import SummarizingLanguageModel
from wiki_searcher.core.models.language_model import LanguageModel
from wiki_searcher.core.searcher.impl.external import ExternalSearcher
from wiki_searcher.core.searcher.searcher import SearcherError
from wiki_searcher.core.storage.impl.external import ArticlesByTopicStorage
from wiki_searcher.logger import setup_logger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _build_api_client(configuration: Configuration) -> HuggingFaceAPIClient:
    return HuggingFaceAPIClient(
        model=configuration.MODEL_REPO_ID,
        token=configuration.HF_API_TOKEN,
        model_parameters=Parameters(),
    )


def _build_model(client: HuggingFaceAPIClient) -> LanguageModel:
    return SummarizingLanguageModel(client=client)


def _build_storage() -> ArticlesByTopicStorage:
    return ArticlesByTopicStorage()


def _build_searcher(
    model: LanguageModel, storage: ArticlesByTopicStorage
) -> ExternalSearcher:
    return ExternalSearcher(model, storage)


def get_articles(topic: str, searcher: ExternalSearcher) -> str:
    try:
        articles = searcher.get_info(topic)
        return "\n".join(str(url) for url in articles.keys())
    except SearcherError as error:
        logger.error(f"Error fetching article URLs for topic '{topic}': {error}")
        return f"Error: {error}"


def summarize_articles(topic: str, searcher: ExternalSearcher) -> str:
    try:
        articles = searcher.get_info(topic)
        summaries = [f"{url}:\n{summary}" for url, summary in articles.items()]
        return "\n\n".join(summaries)
    except SearcherError as error:
        logger.error(f"Error summarizing articles for topic '{topic}': {error}")
        return f"Error: {error}"


def main() -> None:
    setup_logger()
    logger.info("Initializing API client and model...")

    api_client = _build_api_client(Configuration())
    language_model = _build_model(api_client)
    storage = _build_storage()
    articles_storage = _build_searcher(language_model, storage)

    logger.info("Setting up Gradio interface...")
    with gr.Blocks() as app:
        gr.Markdown("# 📚 Wikipedia Article Summarizer")
        topic_input = gr.Textbox(
            label="Enter a Topic", placeholder="e.g., Quantum Computing"
        )

        with gr.Row():
            get_urls_button = gr.Button("Get Article URLs")
            summarize_button = gr.Button("Summarize Articles")

        urls_output = gr.Textbox(label="Article URLs")
        summary_output = gr.Textbox(label="Article Summaries", lines=20)

        get_urls_button.click(
            fn=lambda topic: get_articles(topic, articles_storage),
            inputs=topic_input,
            outputs=urls_output,
        )
        summarize_button.click(
            fn=lambda topic: summarize_articles(topic, articles_storage),
            inputs=topic_input,
            outputs=summary_output,
        )

    logger.info("Launching the application...")
    app.launch()


if __name__ == "__main__":
    main()
