import asyncio
import logging
import functools

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def logger_decorator(func):
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        logging.info(f"Comenzando la ejecución de {func.__name__}...")
        result = await func(*args, **kwargs)
        logging.info(f"Finalizó la ejecución de {func.__name__} satisfactoriamente.")
        return result

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        logging.info(f"Comenzando la ejecución de {func.__name__}...")
        result = func(*args, **kwargs)
        logging.info(f"Finalizó la ejecución de {func.__name__} satisfactoriamente.")
        return result

    # Detectamos si la función es asíncrona o no
    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
