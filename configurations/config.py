import os
from dotenv import load_dotenv

env = os.getenv("PY_ENV")

file_env_path: str = ""
if env == "test":
    file_env_path = os.path.join(os.path.dirname(__file__), f"../.env.test")
else:
    file_env_path = os.path.join(os.path.dirname(__file__), f"../.env")


load_dotenv(dotenv_path=file_env_path)

settings = {
    "HOST": os.getenv("HOST", "localhost"),
    "PORT": int(os.getenv("PORT", "8000")),
    "PY_ENV": os.getenv("PY_ENV"),
    "DEBUG": os.getenv("DEBUG", "False"),
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
    "SALT_ROUNDS": int(os.getenv("SALT_ROUNDS", "10")),
    "DB_URL": os.getenv("DB_URL"),
}


def uvicorn_config():
    return {
        "reload": settings["DEBUG"],
        "host": settings["HOST"],
        "port": settings["PORT"],
        "app": "main:app",
        "env_file": file_env_path,
    }
