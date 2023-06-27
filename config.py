import os
from dotenv import load_dotenv

load_dotenv()
ENTS_BASE_URL = os.getenv('ENTS_BASE_URL')
CENSUS_BASE_URL = os.getenv('CENSUS_BASE_URL')
GEO_SERVER_URL = os.getenv('GEO_SERVER_URL')

API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')
