import os
from dotenv import load_dotenv

# Project root = one level up from this file (backend/config.py -> project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, ".env.development"))

# Resolve DB_PATH relative to the project root, no matter where the
# server is launched from (fixes blank data after moving files into backend/)
_raw_db_path = os.getenv("DB_PATH", "database/palette_forecast.db")
DB_PATH = os.path.join(BASE_DIR, _raw_db_path)
