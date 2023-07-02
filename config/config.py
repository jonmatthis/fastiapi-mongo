import os
from typing import Optional

from beanie import init_beanie
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

import models as models


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None

    # JWT
    SECRET_KEY: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev.dev"
        orm_mode = True


async def initiate_database():

    load_dotenv()

    client = AsyncIOMotorClient(os.getenv("DATABASE_URL"))
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )
