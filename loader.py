from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.connection_configs import ConnectionConfig
from utils.db_api.db_api import PostgresDataBaseManager
from aiogram import Bot, Dispatcher, types
from data import config


scheduler = AsyncIOScheduler()
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
postgres_manager = PostgresDataBaseManager(ConnectionConfig.get_postgres_connection_config())
