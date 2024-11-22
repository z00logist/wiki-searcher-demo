# Wiki-Searcher-Demo

## Overview

Wiki-Searcher is a tool for retrieving Wikipedia URLs based on a specific topic, with an optional feature to summarize the content. It serves as a sub-tool for [Wiki-Helper](https://github.com/z00logist/wiki-helper), a Q&A system designed for exploring and understanding Wikipedia articles. Use Wiki-Searcher to locate relevant articles for your topic of interest, then seamlessly integrate them into your browsing experience with Wiki-Helper.

## How to Use

1. **Run the Application**:
   - **Option 1:** Use the online version on [HuggingFace Space](https://huggingface.co/spaces/z00logist/wiki-searcher).
   - **Option 2:** Run the service locally:
     ```bash
     # Set up the environment
     make prepare
     
     # Start the application
     make run
     ```
     Ensure the `HF_TOKEN_API` environment variable is set before running the service.

2. **Search for a Topic**:
   - Enter your topic in the input box.
   - Choose between:
     - **Getting article URLs** for quick results.
     - **Requesting summaries**, which provides a concise overview along with the article links.

3. **Enhance Your Experience** *(Optional)*:
   - Install the [Wiki-Helper](https://github.com/z00logist/wiki-helper) extension for an enriched browsing experience, making it easier to explore and understand the retrieved articles.

---

With Wiki-Searcher, finding relevant Wikipedia articles has never been simpler!
