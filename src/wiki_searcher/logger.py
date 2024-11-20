import logging
import logging.config


def setup_logger() -> logging.Logger:
    logging.basicConfig(level=logging.INFO)

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "INFO",
                },
            },
            "formatters": {
                "default": {
                    "format": "%(asctime)s %(levelname)s %(lineno)d:%(filename)s(%(process)d) - %(message)s",
                },
            },
            "loggers": {
                "": {
                    "handlers": ["console"],
                    "level": "INFO",
                },
                "wikipediaapi": {
                    "level": "WARNING",
                    "handlers": ["console"],
                    "propagate": False,
                },
                "wikipedia": {
                    "level": "WARNING",
                    "handlers": ["console"],
                    "propagate": False,
                },
            },
        }
    )

    logger = logging.getLogger(__name__)

    return logger
