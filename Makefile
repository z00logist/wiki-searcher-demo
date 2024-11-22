.PHONY: run prepare

export PYTHONPATH := src

run:
	@echo "Starting the service..."
	poetry run python -m wiki_searcher

prepare:
	@echo "Creating virtual environment..."
	virtualenv -p $(shell which python3.12) .venv
	@echo "Activating virtual environment..."
	@. .venv/bin/activate && \
		echo "Installing environment with Poetry..." && \
		poetry install --no-root

	@echo "Checking env for HF_TOKEN_API..."
	@if [ -z "$(HF_TOKEN_API)" ]; then \
		echo "Error: HF_TOKEN_API is not set. Please set the HF_TOKEN_API environment variable and try again."; \
		exit 1; \
	fi