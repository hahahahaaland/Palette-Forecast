import os
from dotenv import load_dotenv

load_dotenv(".env.development")

DB_PATH = os.getenv("DB_PATH")