import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_very_secret_999'
    
    # --- APP VERSION (used as cache-buster for static assets) ---
    # Bump this on every deploy to force Cloudflare, browser, and PWA
    # caches to fetch fresh JS/CSS instead of serving stale cached copies.
    APP_VERSION = '1.7.1'

    # --- DATABASE CONFIG ---
    DB_DRIVER = os.environ.get('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')
    DB_SERVER = os.environ.get('DB_SERVER')
    DB_UID = os.environ.get('DB_UID')
    DB_PWD = os.environ.get('DB_PWD')
    
    DB_AUTH = os.environ.get('DB_AUTH', 'PRO12')     # Inventory & Users
    DB_ORDERS = os.environ.get('DB_ORDERS', 'PRO05') # Sales Orders

    # --- SYSTEM SETTINGS ---
    # Set to False to actually UPDATE inventory and orders (LIVE MODE).
    # Set to True to only validate logic without changing data (TEST MODE).
    SIMULATION_MODE = True