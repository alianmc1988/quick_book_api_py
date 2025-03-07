import os
from dotenv import load_dotenv

env = os.getenv("PY_ENV")

if env != "production" or env is not None:
    if env == "test":
        file_env_path = os.path.join(os.path.dirname(__file__), "../.env.test")
    else:
        file_env_path = os.path.join(os.path.dirname(__file__), "../.env")

    load_dotenv(dotenv_path=file_env_path)

settings = {
    "HOST": os.getenv("HOST", "localhost"),
    "PORT": int(os.getenv("PORT", "8000")),
    "PY_ENV": os.getenv("PY_ENV"),
    "DEBUG": os.getenv("DEBUG", False),
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
    "SALT_ROUNDS": int(os.getenv("SALT_ROUNDS", "10")),
    "DB_URL": os.getenv("DB_URL"),
    "ALGORITHM": os.getenv("ALGORITHM", "HS256"),
    "ACCESS_TOKEN_EXPIRE_MINUTES": int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")),
}


HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "8000"))
PY_ENV = os.getenv("PY_ENV")
DEBUG = os.getenv("DEBUG", False)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
SALT_ROUNDS = int(os.getenv("SALT_ROUNDS", "10"))
DB_URL = os.getenv("DB_URL")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


def uvicorn_config():
    return {
        "reload": DEBUG,
        "host": HOST,
        "port": PORT,
        "app": "main:app",
        "env_file": file_env_path,
    }
