import logging


def get_logger(name: str, log_file: str, level: int) -> logging.Logger:
    """
    Setup a logger with a file handler and a specific logging level.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger
