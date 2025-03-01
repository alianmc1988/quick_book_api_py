import os
from dotenv import load_dotenv

env = os.getenv("PY_ENV", "development")
print(f"Before==============================={env}===============================")
if env != "production":
    env = f".{env}"
else:
    env = ""

print(f"After==============================={env}===============================")

file_env_path = os.path.join(os.path.dirname(__file__), f"../.env{env}")

load_dotenv(dotenv_path=file_env_path)


class Settings:
    HOST = os.getenv("HOST", "localhost")
    PORT = int(os.getenv("PORT", "8000"))
    PY_ENV = os.getenv("PY_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True")
    SALT_ROUNDS = int(os.getenv("SALT_ROUNDS", "10"))
    DB_URL = os.getenv("DB_URL")

    @property
    def DATABASE_URL(self):
        return self.DB_URL


settings = Settings()
