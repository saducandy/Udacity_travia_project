from dotenv import load_dotenv
import os
load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
