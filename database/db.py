from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from configurations.config import settings

debug = settings.get("DEBUG")
uri = settings["DB_URL"]


engine = create_async_engine(
    uri,
    echo=bool(debug),
    future=True,
    pool_size=10,  # Number of connections to keep open
    max_overflow=20,
    pool_pre_ping=True,
)
async_session = sessionmaker(
    engine, class_=AsyncSession, autoflush=False, expire_on_commit=False
)

Base = declarative_base()


async def init_db() -> None:
    async with engine.begin() as conn:
        pass
    await engine.dispose()


async def get_db():
    async with async_session() as db:
        try:
            yield db
        except Exception as e:
            await db.rollback()
            raise e
        finally:
            await db.close()
